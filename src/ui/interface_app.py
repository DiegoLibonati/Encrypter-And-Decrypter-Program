# coding: utf8
from tkinter import Button, Label, StringVar, Tk

from src.services.file_service import FileService
from src.utils.styles import (
    ANCHOR_CENTER,
    BLACK_COLOR,
    FONT_TIMES_12,
    FONT_TIMES_15,
    GREEN_COLOR,
    RED_COLOR,
    RELIEF_RAISED,
    WHITE_COLOR,
)


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = WHITE_COLOR) -> None:
        self._root = root
        self._root.title("Encrypter And Decrypter")
        self._root.geometry("800x300+0+0")
        self._root.resizable(False, False)
        self._root.config(bg=bg)

        self._path = ""

        self._file_service = FileService()

        self._create_widgets()

    def _create_widgets(self) -> None:
        self._label_import_file = StringVar()
        self._label_operation_result = StringVar()

        Button(
            width=20,
            height=1,
            text="Import File",
            relief=RELIEF_RAISED,
            bg=WHITE_COLOR,
            borderwidth=1,
            command=self._select_file,
        ).place(x=10, y=10)
        Label(
            font=FONT_TIMES_12,
            textvariable=self._label_import_file,
            bg=WHITE_COLOR,
            fg=BLACK_COLOR,
        ).place(x=200, y=10)

        Button(
            width=20,
            height=1,
            font=FONT_TIMES_15,
            text="ENCRYPT",
            relief=RELIEF_RAISED,
            bg=RED_COLOR,
            fg=WHITE_COLOR,
            borderwidth=1,
            command=self._encrypt_file,
        ).place(x=150, y=125)
        Button(
            width=20,
            height=1,
            font=FONT_TIMES_15,
            text="DECRYPT",
            relief=RELIEF_RAISED,
            bg=GREEN_COLOR,
            fg=WHITE_COLOR,
            borderwidth=1,
            command=self._decrypt_file,
        ).place(x=400, y=125)
        Label(
            font=FONT_TIMES_12,
            textvariable=self._label_operation_result,
            bg=WHITE_COLOR,
            fg=BLACK_COLOR,
        ).place(x=400, y=250, anchor=ANCHOR_CENTER)

    def _select_file(self) -> None:
        from tkinter import filedialog

        self._path = filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(("Text files", "*.txt*"), ("All files", "*.*")),
        )
        self._label_import_file.set(self._path)

    def _encrypt_file(self) -> None:
        try:
            self._file_service.encrypt_file(self._path)
            self._label_operation_result.set("Successfully encrypted.")
        except ValueError as e:
            self._label_operation_result.set(str(e))

    def _decrypt_file(self) -> None:
        try:
            self._file_service.decrypt_file(self._path)
            self._label_operation_result.set("Successfully decrypted.")
        except ValueError as e:
            self._label_operation_result.set(str(e))
