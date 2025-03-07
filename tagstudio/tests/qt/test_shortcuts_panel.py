from typing import Optional
from PySide6.QtCore import QSettings
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QMenu
from src.qt.modals.shortcuts_panel import ShortcutSettingsPanel 
import pytest

# Dummy driver class to simulate the driver object
class DummyDriver:
    settings: Optional[QSettings]
    add_tag_to_selected_action: Optional[QAction]
    menu: Optional[QMenu]

    def __init__(self) -> None:
        self.settings = None
        self.add_tag_to_selected_action = None
        self.menu = None

@pytest.fixture
def dummy_driver(tmp_path):
    # Create a temporary QSettings file
    settings_file = tmp_path / "test_settings.ini"
    settings = QSettings(str(settings_file), QSettings.Format.IniFormat)
    settings.setValue("shortcuts/add_tag", "T")
    
    driver = DummyDriver()
    driver.settings = settings

    # Create dummy QMenu and store it so that it isnt garbage collected
    menu = QMenu()
    driver.menu = menu
    driver.add_tag_to_selected_action = QAction("Add Tag", menu)
    
    return driver

def test_save_shortcuts(dummy_driver, qtbot):
    # create instance of the panel using dummy driver
    panel = ShortcutSettingsPanel(dummy_driver)
    qtbot.addWidget(panel)
    
    # Simulate a user changing the shortcut in shortcut panel
    new_shortcut_str = "Ctrl+Shift+X"
    panel.add_tag_shortcut_edit.setKeySequence(new_shortcut_str)
    
    # update settings and the QAction
    panel.save_shortcuts()
    
    # Verify QSettings value is updated
    assert dummy_driver.settings.value("shortcuts/add_tag") == new_shortcut_str
    
    # Verify QAction shortcut updated.
    assert dummy_driver.add_tag_to_selected_action.shortcut() == QKeySequence(new_shortcut_str)
