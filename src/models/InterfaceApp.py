# coding: utf8
from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import filedialog

from src.utils.utils import get_text
from src.utils.constants import WHITE_COLOR
from src.utils.constants import BLACK_COLOR
from src.utils.constants import RED_COLOR
from src.utils.constants import GREEN_COLOR
from src.utils.constants import RELIEF_RAISED
from src.utils.constants import ANCHOR_CENTER
from src.utils.constants import FONT_TIMES_12
from src.utils.constants import FONT_TIMES_15


class InterfaceApp:
    def __init__(self, root: Tk, bg: str = WHITE_COLOR) -> None:
        # APP Config
        self._root = root
        self._root.title("Encrypter And Decrypter")
        self._root.geometry("800x300+0+0")
        self._root.resizable(False, False)
        self._root.config(bg=bg)

        self._path = ""

        # Create widges
        self._create_widgets()


    def _create_widgets(self) -> None:
        self._label_import_file = StringVar()
        self._label_operation_result = StringVar()

        Button(width=20, height=1, text="Import File", relief=RELIEF_RAISED, bg=WHITE_COLOR, borderwidth=1, command=lambda:self._select_file()).place(x=10, y=10)
        Label(font=FONT_TIMES_12, textvariable=self._label_import_file, bg=WHITE_COLOR, fg=BLACK_COLOR).place(x=200, y=10)

        Button(width=20, height=1, font=FONT_TIMES_15, text="ENCRYPT", relief=RELIEF_RAISED, bg=RED_COLOR, fg=WHITE_COLOR, borderwidth=1, command=lambda:self._encrypt_file()).place(x=150, y=125)
        Button(width=20, height=1, font=FONT_TIMES_15, text="DECRYPT", relief=RELIEF_RAISED, bg=GREEN_COLOR,fg=WHITE_COLOR, borderwidth=1, command=lambda:self._decrypt_file()).place(x=400, y=125)
        Label(font=FONT_TIMES_12, textvariable=self._label_operation_result, bg=WHITE_COLOR, fg=BLACK_COLOR).place(x=400, y=250, anchor=ANCHOR_CENTER)


    def _select_file(self) -> None:
        self._path = filedialog.askopenfilename(
            initialdir = "/",
            title = "Select a File",
            filetypes = (
                ("Text files", "*.txt*"),
                ("All files", "*.*")
            )
        )

        self._label_import_file.set(self._path)


    def _encrypt_file(self) -> None:
        if not self._path:
            raise ValueError("You must enter a path in order to find a file to encrypt.")

        try:
            encrypted_text = ""
            text = get_text(path=self._path)

            for letter in text: 
                new_letter = ord(letter) + 1
                new_letter = chr(new_letter)
                encrypted_text += new_letter

            file_to_encrypt = open(self._path, "w")
            file_to_encrypt.write(encrypted_text)
            file_to_encrypt.close()

            self._label_operation_result.set("Successfully encrypted.")
        except:
            self._label_operation_result.set("You must insert a txt file to encrypt.")


    def _decrypt_file(self) -> None:
        if not self._path:
            raise ValueError("You must enter a path in order to find a file to decrypt.")

        try:
            decrypted_text = ""
            text = get_text(path=self._path)

            for letter in text: 
                new_letter = ord(letter) - 1
                new_letter = chr(new_letter)
                decrypted_text += new_letter

            file_to_decrypt = open(self._path, "w")
            file_to_decrypt.write(decrypted_text)
            file_to_decrypt.close()

            self._label_operation_result.set("Successfully decrypted.")
        except:
            self._label_operation_result.set("You must insert a txt file to decrypt.")