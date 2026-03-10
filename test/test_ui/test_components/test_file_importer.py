from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.file_importer import FileImporter


@pytest.fixture
def file_importer(mock_styles: MagicMock, mock_on_import: MagicMock) -> FileImporter:
    with (
        patch("src.ui.components.file_importer.Frame.__init__", return_value=None),
        patch("src.ui.components.file_importer.Button"),
        patch("src.ui.components.file_importer.Label"),
        patch("src.ui.components.file_importer.StringVar"),
        patch.object(FileImporter, "columnconfigure"),
    ):
        instance: FileImporter = FileImporter.__new__(FileImporter)
        instance._styles = mock_styles
        instance._on_import = mock_on_import
        instance._label_import_file = MagicMock(spec=StringVar)
        return instance


class TestFileImporterInit:
    def test_stores_styles(self, file_importer: FileImporter, mock_styles: MagicMock) -> None:
        assert file_importer._styles == mock_styles

    def test_stores_on_import(self, file_importer: FileImporter, mock_on_import: MagicMock) -> None:
        assert file_importer._on_import == mock_on_import

    def test_button_command_is_on_import(self, mock_styles: MagicMock, mock_on_import: MagicMock) -> None:
        with (
            patch("src.ui.components.file_importer.Frame.__init__", return_value=None),
            patch("src.ui.components.file_importer.Button") as mock_button,
            patch("src.ui.components.file_importer.Label") as mock_label,
            patch("src.ui.components.file_importer.StringVar"),
            patch.object(FileImporter, "columnconfigure"),
        ):
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: FileImporter = FileImporter.__new__(FileImporter)
            instance._styles = mock_styles
            FileImporter.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_import=mock_on_import,
            )

        _, kwargs = mock_button.call_args
        assert kwargs.get("command") == mock_on_import

    def test_button_text_is_import_file(self, mock_styles: MagicMock, mock_on_import: MagicMock) -> None:
        with (
            patch("src.ui.components.file_importer.Frame.__init__", return_value=None),
            patch("src.ui.components.file_importer.Button") as mock_button,
            patch("src.ui.components.file_importer.Label") as mock_label,
            patch("src.ui.components.file_importer.StringVar"),
            patch.object(FileImporter, "columnconfigure"),
        ):
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: FileImporter = FileImporter.__new__(FileImporter)
            instance._styles = mock_styles
            FileImporter.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_import=mock_on_import,
            )

        _, kwargs = mock_button.call_args
        assert kwargs.get("text") == "Import File"

    def test_columnconfigure_called_twice(self, mock_styles: MagicMock, mock_on_import: MagicMock) -> None:
        with (
            patch("src.ui.components.file_importer.Frame.__init__", return_value=None),
            patch("src.ui.components.file_importer.Button") as mock_button,
            patch("src.ui.components.file_importer.Label") as mock_label,
            patch("src.ui.components.file_importer.StringVar"),
            patch.object(FileImporter, "columnconfigure") as mock_columnconfigure,
        ):
            mock_button.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: FileImporter = FileImporter.__new__(FileImporter)
            instance._styles = mock_styles
            FileImporter.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_import=mock_on_import,
            )

        assert mock_columnconfigure.call_count == 2


class TestFileImporterSetPath:
    def test_sets_label_to_given_path(self, file_importer: FileImporter) -> None:
        file_importer.set_path("/some/path/file.txt")
        file_importer._label_import_file.set.assert_called_once_with("/some/path/file.txt")

    def test_sets_empty_string(self, file_importer: FileImporter) -> None:
        file_importer.set_path("")
        file_importer._label_import_file.set.assert_called_once_with("")
