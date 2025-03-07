from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SaSession
from sqlalchemy.orm import sessionmaker
from src.core.library.alchemy.enums import FilterState, SortingModeEnum
from src.core.library.alchemy.library import Library, LibraryPrefs
from src.core.library.alchemy.models import Base, Entry, Folder


# Define a dummy prefs function that returns default values.
def dummy_prefs(key):
    # If the key is LibraryPrefs.EXTENSION_LIST, return an empty list or your default extensions.
    # Adjust as needed for other preference keys.
    if key == LibraryPrefs.EXTENSION_LIST:
        return []
    return None


# Define a session fixture that sets up an in-memory SQLite database.
@pytest.fixture(scope="function")
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    sess: SaSession = session()
    # Attach required attributes to the session:
    sess.engine = engine
    sess.prefs = dummy_prefs  # Attach the callable dummy_prefs
    yield sess
    sess.close()


# Fixture to add dummy entries to the database.
@pytest.fixture
def mock_entries(session):
    """Create dummy files in the database for testing."""
    # Create a dummy folder (required by Entry)
    dummy_folder = Folder(path=Path("dummy"), uuid="dummy")
    session.add(dummy_folder)
    session.commit()

    # Create entries using a file path, the dummy folder, and an empty list for fields.
    session.add_all(
        [
            Entry(path=Path("banana.txt"), folder=dummy_folder, fields=[]),
            Entry(path=Path("apple.txt"), folder=dummy_folder, fields=[]),
            Entry(path=Path("cherry.txt"), folder=dummy_folder, fields=[]),
        ]
    )
    session.commit()
    return session


def test_sort_by_filename_ascending(mock_entries):
    """Test sorting by filename in ascending order."""
    filter_state = FilterState(sorting_mode=SortingModeEnum.FILENAME, ascending=True)
    results = Library.search_library(mock_entries, filter_state)

    # Use entry.path.name to get the filename.
    filenames = [entry.path.name for entry in results]
    assert filenames == ["apple.txt", "banana.txt", "cherry.txt"]


def test_sort_by_filename_descending(mock_entries):
    """Test sorting by filename in descending order."""
    filter_state = FilterState(sorting_mode=SortingModeEnum.FILENAME, ascending=False)
    results = Library.search_library(mock_entries, filter_state)

    filenames = [entry.path.name for entry in results]
    assert filenames == ["cherry.txt", "banana.txt", "apple.txt"]
