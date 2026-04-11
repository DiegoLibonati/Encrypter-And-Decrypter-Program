import tkinter as tk
from unittest.mock import patch

from src.configs.default_config import DefaultConfig
from src.constants.messages import MESSAGE_SUCCESS_DECRYPTED, MESSAGE_SUCCESS_ENCRYPTED
from src.services.file_service import FileService
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles


class TestInterfaceApp:
    def test_instantiation(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app is not None

    def test_initial_path_is_empty(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._path == ""

    def test_config_is_stored(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert app._config is config

    def test_styles_default_is_styles_instance(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        assert isinstance(app._styles, Styles)

    def test_select_file_updates_path(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value="/path/to/file.txt"):
            app._select_file()
        assert app._path == "/path/to/file.txt"

    def test_select_file_updates_import_label(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value="/path/to/file.txt"):
            app._select_file()
        assert app._main_view._file_importer._label_import_file.get() == "/path/to/file.txt"

    def test_select_file_empty_result_clears_path(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch("src.ui.interface_app.filedialog.askopenfilename", return_value=""):
            app._select_file()
        assert app._path == ""

    def test_encrypt_file_sets_success_result(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch.object(FileService, "encrypt_file", return_value=True):
            app._encrypt_file()
        assert app._main_view._label_operation_result.get() == MESSAGE_SUCCESS_ENCRYPTED

    def test_encrypt_file_does_not_set_result_on_failure(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.set_result("")
        with patch.object(FileService, "encrypt_file", return_value=False):
            app._encrypt_file()
        assert app._main_view._label_operation_result.get() == ""

    def test_decrypt_file_sets_success_result(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        with patch.object(FileService, "decrypt_file", return_value=True):
            app._decrypt_file()
        assert app._main_view._label_operation_result.get() == MESSAGE_SUCCESS_DECRYPTED

    def test_decrypt_file_does_not_set_result_on_failure(self, root: tk.Tk) -> None:
        config: DefaultConfig = DefaultConfig()
        app: InterfaceApp = InterfaceApp(root=root, config=config)
        app._main_view.set_result("")
        with patch.object(FileService, "decrypt_file", return_value=False):
            app._decrypt_file()
        assert app._main_view._label_operation_result.get() == ""
