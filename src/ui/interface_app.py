from tkinter import Tk, filedialog

from src.configs.default_config import DefaultConfig
from src.services.file_service import FileService
from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class InterfaceApp:
    def __init__(self, root: Tk, config: DefaultConfig, styles: Styles = Styles()) -> None:
        self._styles = styles
        self._config = config
        self._root = root
        self._root.title("Encrypter And Decrypter")
        self._root.geometry("800x300+0+0")
        self._root.resizable(False, False)
        self._root.config(bg=self._styles.WHITE_COLOR)

        self._path = ""

        self._main_view = MainView(
            root=self._root,
            styles=self._styles,
            on_import=self._select_file,
            on_encrypt=self._encrypt_file,
            on_decrypt=self._decrypt_file,
        )
        self._main_view.grid(row=0, column=0, sticky="nsew")
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)

    def _select_file(self) -> None:
        self._path = filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(("Text files", "*.txt*"), ("All files", "*.*")),
        )
        self._main_view.set_import_label(self._path)

    def _encrypt_file(self) -> None:
        try:
            FileService().encrypt_file(self._path)
            self._main_view.set_result("Successfully encrypted.")
        except ValueError as e:
            self._main_view.set_result(str(e))

    def _decrypt_file(self) -> None:
        try:
            FileService().decrypt_file(self._path)
            self._main_view.set_result("Successfully decrypted.")
        except ValueError as e:
            self._main_view.set_result(str(e))
