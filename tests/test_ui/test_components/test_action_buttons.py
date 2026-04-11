import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.action_buttons import ActionButtons
from src.ui.styles import Styles


class TestActionButtons:
    def test_instantiation(self, root: tk.Tk) -> None:
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert buttons is not None

    def test_is_frame(self, root: tk.Tk) -> None:
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert isinstance(buttons, tk.Frame)

    def test_background_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=styles,
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert buttons.cget("bg") == styles.WHITE_COLOR

    def test_on_encrypt_callback_stored(self, root: tk.Tk) -> None:
        on_encrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=on_encrypt,
            on_decrypt=MagicMock(),
        )
        assert buttons._on_encrypt is on_encrypt

    def test_on_decrypt_callback_stored(self, root: tk.Tk) -> None:
        on_decrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=MagicMock(),
            on_decrypt=on_decrypt,
        )
        assert buttons._on_decrypt is on_decrypt

    def test_on_encrypt_callback_called(self, root: tk.Tk) -> None:
        on_encrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=on_encrypt,
            on_decrypt=MagicMock(),
        )
        buttons._on_encrypt()
        on_encrypt.assert_called_once()

    def test_on_decrypt_callback_called(self, root: tk.Tk) -> None:
        on_decrypt: MagicMock = MagicMock()
        buttons: ActionButtons = ActionButtons(
            parent=root,
            styles=Styles(),
            on_encrypt=MagicMock(),
            on_decrypt=on_decrypt,
        )
        buttons._on_decrypt()
        on_decrypt.assert_called_once()
