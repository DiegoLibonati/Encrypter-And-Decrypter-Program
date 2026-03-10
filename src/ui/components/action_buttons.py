from tkinter import Button, Frame, Misc

from src.ui.styles import Styles


class ActionButtons(Frame):
    def __init__(self, parent: Misc, styles: Styles, on_encrypt: callable, on_decrypt: callable) -> None:
        super().__init__(parent, bg=styles.WHITE_COLOR)
        self._styles = styles
        self._on_encrypt = on_encrypt
        self._on_decrypt = on_decrypt

        Button(
            self,
            width=20,
            height=1,
            font=self._styles.FONT_TIMES_15,
            text="ENCRYPT",
            relief=self._styles.RELIEF_RAISED,
            bg=self._styles.RED_COLOR,
            fg=self._styles.WHITE_COLOR,
            borderwidth=1,
            command=self._on_encrypt,
        ).grid(row=0, column=0, padx=(0, 20))

        Button(
            self,
            width=20,
            height=1,
            font=self._styles.FONT_TIMES_15,
            text="DECRYPT",
            relief=self._styles.RELIEF_RAISED,
            bg=self._styles.GREEN_COLOR,
            fg=self._styles.WHITE_COLOR,
            borderwidth=1,
            command=self._on_decrypt,
        ).grid(row=0, column=1)
