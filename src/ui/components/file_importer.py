from tkinter import Button, Frame, Label, Misc, StringVar

from src.ui.styles import Styles


class FileImporter(Frame):
    def __init__(self, parent: Misc, styles: Styles, on_import: callable) -> None:
        super().__init__(parent, bg=styles.WHITE_COLOR)
        self._styles = styles
        self._on_import = on_import

        self._label_import_file = StringVar()

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)

        Button(
            self,
            width=20,
            height=1,
            text="Import File",
            relief=self._styles.RELIEF_RAISED,
            bg=self._styles.WHITE_COLOR,
            borderwidth=1,
            command=self._on_import,
        ).grid(row=0, column=0, sticky="w")

        Label(
            self,
            font=self._styles.FONT_TIMES_12,
            textvariable=self._label_import_file,
            bg=self._styles.WHITE_COLOR,
            fg=self._styles.BLACK_COLOR,
        ).grid(row=0, column=1, sticky="w", padx=(10, 0))

    def set_path(self, path: str) -> None:
        self._label_import_file.set(path)
