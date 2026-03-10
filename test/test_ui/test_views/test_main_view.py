from tkinter import StringVar
from unittest.mock import MagicMock, patch

import pytest

from src.ui.views.main_view import MainView


@pytest.fixture
def main_view(
    mock_root: MagicMock,
    mock_styles: MagicMock,
    mock_on_import: MagicMock,
    mock_on_encrypt: MagicMock,
    mock_on_decrypt: MagicMock,
) -> MainView:
    with (
        patch("src.ui.views.main_view.Frame.__init__", return_value=None),
        patch("src.ui.views.main_view.FileImporter"),
        patch("src.ui.views.main_view.ActionButtons"),
        patch("src.ui.views.main_view.Label"),
        patch("src.ui.views.main_view.StringVar"),
        patch.object(MainView, "columnconfigure"),
    ):
        instance: MainView = MainView.__new__(MainView)
        instance._styles = mock_styles
        instance._on_import = mock_on_import
        instance._on_encrypt = mock_on_encrypt
        instance._on_decrypt = mock_on_decrypt
        instance._label_operation_result = MagicMock(spec=StringVar)
        instance._file_importer = MagicMock()
        instance._action_buttons = MagicMock()
        return instance


class TestMainViewInit:
    def test_stores_styles(self, main_view: MainView, mock_styles: MagicMock) -> None:
        assert main_view._styles == mock_styles

    def test_stores_on_import(self, main_view: MainView, mock_on_import: MagicMock) -> None:
        assert main_view._on_import == mock_on_import

    def test_stores_on_encrypt(self, main_view: MainView, mock_on_encrypt: MagicMock) -> None:
        assert main_view._on_encrypt == mock_on_encrypt

    def test_stores_on_decrypt(self, main_view: MainView, mock_on_decrypt: MagicMock) -> None:
        assert main_view._on_decrypt == mock_on_decrypt

    def test_file_importer_receives_on_import(
        self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_import: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock
    ) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.FileImporter") as mock_file_importer,
            patch("src.ui.views.main_view.ActionButtons") as mock_action_buttons,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_file_importer.return_value.grid = MagicMock()
            mock_action_buttons.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                on_import=mock_on_import,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        _, kwargs = mock_file_importer.call_args
        assert kwargs.get("on_import") == mock_on_import

    def test_action_buttons_receives_on_encrypt(
        self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_import: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock
    ) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.FileImporter") as mock_file_importer,
            patch("src.ui.views.main_view.ActionButtons") as mock_action_buttons,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_file_importer.return_value.grid = MagicMock()
            mock_action_buttons.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                on_import=mock_on_import,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        _, kwargs = mock_action_buttons.call_args
        assert kwargs.get("on_encrypt") == mock_on_encrypt

    def test_action_buttons_receives_on_decrypt(
        self, mock_root: MagicMock, mock_styles: MagicMock, mock_on_import: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock
    ) -> None:
        with (
            patch("src.ui.views.main_view.Frame.__init__", return_value=None),
            patch("src.ui.views.main_view.FileImporter") as mock_file_importer,
            patch("src.ui.views.main_view.ActionButtons") as mock_action_buttons,
            patch("src.ui.views.main_view.Label") as mock_label,
            patch("src.ui.views.main_view.StringVar"),
            patch.object(MainView, "columnconfigure"),
        ):
            mock_file_importer.return_value.grid = MagicMock()
            mock_action_buttons.return_value.grid = MagicMock()
            mock_label.return_value.grid = MagicMock()
            instance: MainView = MainView.__new__(MainView)
            instance._styles = mock_styles
            MainView.__init__(
                instance,
                root=mock_root,
                styles=mock_styles,
                on_import=mock_on_import,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        _, kwargs = mock_action_buttons.call_args
        assert kwargs.get("on_decrypt") == mock_on_decrypt


class TestMainViewSetImportLabel:
    def test_delegates_to_file_importer(self, main_view: MainView) -> None:
        main_view.set_import_label("/path/to/file.txt")
        main_view._file_importer.set_path.assert_called_once_with("/path/to/file.txt")

    def test_delegates_empty_string(self, main_view: MainView) -> None:
        main_view.set_import_label("")
        main_view._file_importer.set_path.assert_called_once_with("")


class TestMainViewSetResult:
    def test_sets_result_text(self, main_view: MainView) -> None:
        main_view.set_result("Successfully encrypted.")
        main_view._label_operation_result.set.assert_called_once_with("Successfully encrypted.")

    def test_sets_empty_string(self, main_view: MainView) -> None:
        main_view.set_result("")
        main_view._label_operation_result.set.assert_called_once_with("")
