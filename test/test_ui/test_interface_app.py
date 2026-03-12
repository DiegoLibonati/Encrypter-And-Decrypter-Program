from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_SUCCESS_DECRYPTED, MESSAGE_SUCCESS_ENCRYPTED
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


@pytest.fixture
def interface_app(mock_root: MagicMock, mock_styles: MagicMock) -> InterfaceApp:
    with patch("src.ui.interface_app.MainView") as mock_main_view_class:
        mock_main_view: MagicMock = MagicMock()
        mock_main_view.grid = MagicMock()
        mock_main_view_class.return_value = mock_main_view
        instance: InterfaceApp = InterfaceApp.__new__(InterfaceApp)
        instance._styles = mock_styles
        instance._root = mock_root
        instance._config = MagicMock()
        instance._main_view = mock_main_view
        instance._path = ""
        return instance


class TestInterfaceAppInit:
    def test_stores_styles(self, interface_app: InterfaceApp, mock_styles: MagicMock) -> None:
        assert interface_app._styles == mock_styles

    def test_stores_root(self, interface_app: InterfaceApp, mock_root: MagicMock) -> None:
        assert interface_app._root == mock_root

    def test_path_initial_value_is_empty(self, interface_app: InterfaceApp) -> None:
        assert interface_app._path == ""

    def test_title_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.title.assert_called_once_with("Encrypter And Decrypter")

    def test_geometry_is_set(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.geometry.assert_called_once_with("800x300+0+0")

    def test_is_not_resizable(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        mock_root.resizable.assert_called_once_with(False, False)

    def test_default_styles_is_styles_instance(self, mock_root: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            app: InterfaceApp = InterfaceApp(root=mock_root, config=MagicMock())

        assert isinstance(app._styles, Styles)

    def test_main_view_receives_callbacks(self, mock_root: MagicMock, mock_styles: MagicMock) -> None:
        with patch("src.ui.interface_app.MainView") as mock_main_view_class:
            mock_main_view_class.return_value.grid = MagicMock()
            InterfaceApp(root=mock_root, config=MagicMock(), styles=mock_styles)

        _, kwargs = mock_main_view_class.call_args
        assert callable(kwargs.get("on_import"))
        assert callable(kwargs.get("on_encrypt"))
        assert callable(kwargs.get("on_decrypt"))


class TestInterfaceAppSelectFile:
    def test_path_is_updated(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value="/path/to/file.txt"):
            interface_app._select_file()

        assert interface_app._path == "/path/to/file.txt"

    def test_set_import_label_called_with_path(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value="/path/to/file.txt"):
            interface_app._select_file()

        interface_app._main_view.set_import_label.assert_called_once_with("/path/to/file.txt")

    def test_path_updated_to_empty_when_dialog_cancelled(self, interface_app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value=""):
            interface_app._select_file()

        assert interface_app._path == ""


class TestInterfaceAppEncryptFile:
    def test_set_result_called_with_success_message(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.encrypt_file.return_value = True
            interface_app._encrypt_file()

        interface_app._main_view.set_result.assert_called_once_with(MESSAGE_SUCCESS_ENCRYPTED)

    def test_set_result_not_called_when_encrypt_returns_false(self, interface_app: InterfaceApp) -> None:
        interface_app._path = ""

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.encrypt_file.return_value = False
            interface_app._encrypt_file()

        interface_app._main_view.set_result.assert_not_called()

    def test_encrypt_file_called_with_path(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_instance: MagicMock = mock_file_service_class.return_value
            mock_instance.encrypt_file.return_value = True
            interface_app._encrypt_file()

        mock_instance.encrypt_file.assert_called_once_with(interface_app._path)

    def test_fresh_file_service_is_instantiated(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.encrypt_file.return_value = True
            interface_app._encrypt_file()

        mock_file_service_class.assert_called_once_with()


class TestInterfaceAppDecryptFile:
    def test_set_result_called_with_success_message(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.decrypt_file.return_value = True
            interface_app._decrypt_file()

        interface_app._main_view.set_result.assert_called_once_with(MESSAGE_SUCCESS_DECRYPTED)

    def test_set_result_not_called_when_decrypt_returns_false(self, interface_app: InterfaceApp) -> None:
        interface_app._path = ""

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.decrypt_file.return_value = False
            interface_app._decrypt_file()

        interface_app._main_view.set_result.assert_not_called()

    def test_decrypt_file_called_with_path(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_instance: MagicMock = mock_file_service_class.return_value
            mock_instance.decrypt_file.return_value = True
            interface_app._decrypt_file()

        mock_instance.decrypt_file.assert_called_once_with(interface_app._path)

    def test_fresh_file_service_is_instantiated(self, interface_app: InterfaceApp) -> None:
        interface_app._path = "notes.txt"

        with patch("src.ui.interface_app.FileService") as mock_file_service_class:
            mock_file_service_class.return_value.decrypt_file.return_value = True
            interface_app._decrypt_file()

        mock_file_service_class.assert_called_once_with()
