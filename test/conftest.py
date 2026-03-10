from tkinter import StringVar
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles


@pytest.fixture
def mock_root() -> MagicMock:
    root: MagicMock = MagicMock()
    root.title = MagicMock()
    root.geometry = MagicMock()
    root.resizable = MagicMock()
    root.config = MagicMock()
    root.columnconfigure = MagicMock()
    root.rowconfigure = MagicMock()
    return root


@pytest.fixture
def mock_styles() -> MagicMock:
    styles: MagicMock = MagicMock()
    styles.WHITE_COLOR = "#FFFFFF"
    styles.BLACK_COLOR = "#000000"
    styles.RED_COLOR = "#FF0000"
    styles.GREEN_COLOR = "#00FF00"
    styles.FONT_TIMES_12 = "Times 12"
    styles.FONT_TIMES_15 = "Times 15"
    styles.RELIEF_RAISED = "raised"
    return styles


@pytest.fixture
def real_styles() -> Styles:
    return Styles()


@pytest.fixture
def mock_on_import() -> MagicMock:
    return MagicMock()


@pytest.fixture
def mock_on_encrypt() -> MagicMock:
    return MagicMock()


@pytest.fixture
def mock_on_decrypt() -> MagicMock:
    return MagicMock()


@pytest.fixture
def variable() -> MagicMock:
    return MagicMock(spec=StringVar)
