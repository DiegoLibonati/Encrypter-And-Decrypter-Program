from tkinter import Frame, Label, StringVar, Tk

from src.ui.components.action_buttons import ActionButtons
from src.ui.components.file_importer import FileImporter
from src.ui.styles import Styles


class MainView(Frame):
    def __init__(
        self,
        root: Tk,
        styles: Styles,
        on_import: callable,
        on_encrypt: callable,
        on_decrypt: callable,
    ) -> None:
        super().__init__(root, bg=styles.WHITE_COLOR)
        self._styles = styles
        self._on_import = on_import
        self._on_encrypt = on_encrypt
        self._on_decrypt = on_decrypt

        self._label_operation_result = StringVar()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self.columnconfigure(0, weight=1)

        self._file_importer = FileImporter(
            parent=self,
            styles=self._styles,
            on_import=self._on_import,
        )
        self._file_importer.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))

        self._action_buttons = ActionButtons(
            parent=self,
            styles=self._styles,
            on_encrypt=self._on_encrypt,
            on_decrypt=self._on_decrypt,
        )
        self._action_buttons.grid(row=1, column=0, pady=(50, 0))

        Label(
            self,
            font=self._styles.FONT_TIMES_12,
            textvariable=self._label_operation_result,
            bg=self._styles.WHITE_COLOR,
            fg=self._styles.BLACK_COLOR,
        ).grid(row=2, column=0, pady=(30, 0))

    def set_import_label(self, path: str) -> None:
        self._file_importer.set_path(path)

    def set_result(self, text: str) -> None:
        self._label_operation_result.set(text)
