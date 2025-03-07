import os
from contextlib import suppress
from pathlib import Path

import pytest
from PIL import Image
from PySide6.QtCore import QByteArray
from src.qt.widgets.preview.preview_thumb import PreviewThumb


class DummyResourceManager:
    def __init__(self):
        # Create empty QByteArrays for the required icons
        self.play_icon = QByteArray()
        self.pause_icon = QByteArray()
        self.volume_icon = QByteArray()
        self.volume_mute_icon = QByteArray()

    def get_path(self, name):
        return Path("/tmp/dummy/resource")


class DummyDriver:
    def __init__(self):
        self.deleted = False
        self.deleted_file = None
        self.settings = DummySettings()
        # Add the resource manager with required icons
        self.rm = DummyResourceManager()

    def delete_files_callback(self, filepath):
        self.deleted = True
        self.deleted_file = filepath
        return True

    def remove_file(self, path):  # Renamed from 'rm' to avoid conflict
        try:
            os.remove(path)
            return True
        except OSError:
            return False


class DummySettings:
    def __init__(self, initial_values=None):
        self._values = initial_values or {}

    def value(self, key, default_value=None, type_=None, **kwargs):
        # Support calls using 'defaultValue' as well as 'default_value'
        if "defaultValue" in kwargs:
            default_value = kwargs.pop("defaultValue")
        result = self._values.get(key, default_value)
        if type_ is not None:
            with suppress(Exception):
                result = type_(result)
        return result


class DummyLibrary:
    def __init__(self, library_dir: Path = None):
        if library_dir is None:
            library_dir = Path("/tmp/dummy_library")
        self.library_dir = library_dir
        # Ensure the expected thumbs directory exists:
        thumbs_dir = self.library_dir / ".TagStudio" / "thumbs"
        thumbs_dir.mkdir(parents=True, exist_ok=True)


# --- Fixtures ---


@pytest.fixture
def dummy_driver():
    return DummyDriver()


@pytest.fixture
def preview_thumb(qtbot, dummy_driver):
    """Returns a PreviewThumb widget with a dummy library and driver."""
    widget = PreviewThumb(DummyLibrary(), dummy_driver)
    qtbot.addWidget(widget)
    return widget


# --- Helper Functions to Create Test Files ---


def create_animated_gif(tmp_path: Path, filename="test_anim.gif") -> Path:
    """
    Create a simple animated GIF (2 frames) using Pillow.
    """
    path = tmp_path / filename
    frames = []
    for i in range(2):
        # Create two frames with slightly different colors.
        img = Image.new("RGB", (100, 100), color=(i * 120, i * 60, i * 30))
        frames.append(img)
    frames[0].save(path, save_all=True, append_images=frames[1:], loop=0, duration=100)
    return path


def create_animated_webp(tmp_path: Path, filename="test_anim.webp") -> Path:
    """
    Create a simple animated WebP (2 frames) using Pillow.
    Requires that your Pillow installation supports animated WebP.
    """
    path = tmp_path / filename
    frames = []
    for i in range(2):
        # Create two frames with different colors.
        img = Image.new("RGB", (100, 100), color=(i * 120, i * 60, i * 30))
        frames.append(img)
    # Save as animated WebP (if supported).
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        loop=0,
        duration=100,
        format="WEBP",
    )
    return path


def create_static_image(tmp_path: Path, filename="test_static.jpg") -> Path:
    """
    Create a static JPEG image using Pillow.
    """
    path = tmp_path / filename
    img = Image.new("RGB", (200, 150), color="blue")
    img.save(path, format="JPEG")
    return path


# --- Mock for MediaPlayer if necessary ---
# If the MediaPlayer class in PreviewThumb still causes issues, you can use this mock


class MockMediaPlayer:
    def __init__(self, driver):
        self.player = MockMediaPlayerInstance()

    def show(self):
        pass

    def hide(self):
        pass

    def stop(self):
        pass

    def play(self, filepath):
        pass


class MockMediaPlayerInstance:
    def duration(self):
        return 10  # Return a dummy duration


# --- Tests ---
def test_animated_webp(preview_thumb, qtbot, tmp_path):
    """
    Test that update_preview correctly loads an animated WebP preview.
    It should work similarly to animated GIFs.
    """
    preview_thumb.show()
    qtbot.waitForWindowShown(preview_thumb)
    webp_file = create_animated_webp(tmp_path)
    stats = preview_thumb.update_preview(webp_file, ".webp")
    # Verify that stats include width and height.
    assert "width" in stats and "height" in stats

    # Check that a QMovie has been created and attached to the preview_gif label.
    movie = preview_thumb.preview_gif.movie()
    assert movie is not None, "No QMovie was created for animated WebP."
    assert movie.isValid(), "The QMovie for animated WebP is not valid."
    # Animated WebP should have more than one frame.
    assert movie.frameCount() > 1, "Animated WebP should have more than one frame."

    # Verify that the animated preview widget is visible and others are hidden.
    assert preview_thumb.preview_gif.isVisible(), "Animated WebP preview is not visible."
    assert (
        not preview_thumb.preview_img.isVisible()
    ), "Static image preview should be hidden when using WebP."
    assert (
        not preview_thumb.preview_vid.isVisible()
    ), "Video preview should be hidden when using WebP."

    # After update, ensure the file can be deleted.
    webp_file.unlink()
    assert not webp_file.exists(), "Animated WebP file was not deleted."


def test_animated_preview(preview_thumb, qtbot, tmp_path):
    """
    Test that update_preview correctly loads an animated GIF (or WebP) preview.
    Verifies that the QLabel for animated previews shows a valid QMovie with multiple frames.
    Also, verifies that after update_preview, the file is no longer held open (and can be deleted).
    """
    preview_thumb.show()
    qtbot.waitForWindowShown(preview_thumb)
    anim_file = create_animated_gif(tmp_path)
    stats = preview_thumb.update_preview(anim_file, ".gif")
    # Verify that stats include width and height.
    assert "width" in stats and "height" in stats

    # Check that a QMovie has been created and attached to the preview_gif label.
    movie = preview_thumb.preview_gif.movie()
    assert movie is not None, "No QMovie was created."
    assert movie.isValid(), "The QMovie is not valid."
    # For an animated GIF, the frame count should be greater than 1.
    assert movie.frameCount() > 1, "Animated GIF should have more than one frame."

    # Verify that the animated preview widget is visible and others are hidden.
    assert preview_thumb.preview_gif.isVisible(), "Animated preview is not visible."
    assert not preview_thumb.preview_img.isVisible(), "Static image preview should be hidden."
    assert not preview_thumb.preview_vid.isVisible(), "Video preview should be hidden."

    # After update, the file should have been read completely so we can delete it.
    anim_file.unlink()
    assert not anim_file.exists(), "Animated GIF file was not deleted."


def test_static_preview(preview_thumb, qtbot, tmp_path):
    """
    Test that update_preview loads a static image preview for non-animated files.
    The preview_img button should be visible while animated and video previews remain hidden.
    """
    preview_thumb.show()
    qtbot.waitForWindowShown(preview_thumb)
    static_file = create_static_image(tmp_path)
    stats = preview_thumb.update_preview(static_file, ".jpg")
    # For static images, preview_img should be visible.
    assert preview_thumb.preview_img.isVisible(), "Static image preview should be visible."

    # Animated and video previews should be hidden.
    assert not preview_thumb.preview_gif.isVisible(), "Animated preview should be hidden."
    assert not preview_thumb.preview_vid.isVisible(), "Video preview should be hidden."

    # Check that stats contain image dimensions.
    assert "width" in stats and "height" in stats

    # Ensure the file can be deleted (since it should not be held open).
    static_file.unlink()
    assert not static_file.exists(), "Static image file was not deleted."


def test_delete_action(preview_thumb, qtbot, tmp_path, dummy_driver):
    """
    Test that triggering the delete action in the preview calls the driver's delete_files_callback.
    """
    static_file = create_static_image(tmp_path, filename="delete_test.jpg")
    preview_thumb.update_preview(static_file, ".jpg")
    # The update_preview method also connects the delete_action.
    # Simulate triggering the delete action.
    preview_thumb.delete_action.trigger()
    # Verify that the dummy driver's delete_files_callback was called.
    assert dummy_driver.deleted is True, "Driver's delete_files_callback was not called."
    # Also check that the file passed to the callback is the same as our static file.
    assert dummy_driver.deleted_file == static_file, "Deleted file path does not match."
