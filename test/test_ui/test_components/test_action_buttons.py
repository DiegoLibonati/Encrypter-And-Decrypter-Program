from unittest.mock import MagicMock, patch

import pytest

from src.ui.components.action_buttons import ActionButtons


@pytest.fixture
def action_buttons(mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> ActionButtons:
    with (
        patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
        patch("src.ui.components.action_buttons.Button"),
    ):
        instance: ActionButtons = ActionButtons.__new__(ActionButtons)
        instance._styles = mock_styles
        instance._on_encrypt = mock_on_encrypt
        instance._on_decrypt = mock_on_decrypt
        return instance


class TestActionButtonsInit:
    def test_stores_styles(self, action_buttons: ActionButtons, mock_styles: MagicMock) -> None:
        assert action_buttons._styles == mock_styles

    def test_stores_on_encrypt(self, action_buttons: ActionButtons, mock_on_encrypt: MagicMock) -> None:
        assert action_buttons._on_encrypt == mock_on_encrypt

    def test_stores_on_decrypt(self, action_buttons: ActionButtons, mock_on_decrypt: MagicMock) -> None:
        assert action_buttons._on_decrypt == mock_on_decrypt

    def test_encrypt_button_command_is_on_encrypt(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        first_call_kwargs: dict = mock_button.call_args_list[0].kwargs
        assert first_call_kwargs.get("command") == mock_on_encrypt

    def test_decrypt_button_command_is_on_decrypt(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        second_call_kwargs: dict = mock_button.call_args_list[1].kwargs
        assert second_call_kwargs.get("command") == mock_on_decrypt

    def test_encrypt_button_text_is_encrypt(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        first_call_kwargs: dict = mock_button.call_args_list[0].kwargs
        assert first_call_kwargs.get("text") == "ENCRYPT"

    def test_decrypt_button_text_is_decrypt(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        second_call_kwargs: dict = mock_button.call_args_list[1].kwargs
        assert second_call_kwargs.get("text") == "DECRYPT"

    def test_encrypt_button_bg_is_red(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        first_call_kwargs: dict = mock_button.call_args_list[0].kwargs
        assert first_call_kwargs.get("bg") == mock_styles.RED_COLOR

    def test_decrypt_button_bg_is_green(self, mock_styles: MagicMock, mock_on_encrypt: MagicMock, mock_on_decrypt: MagicMock) -> None:
        with (
            patch("src.ui.components.action_buttons.Frame.__init__", return_value=None),
            patch("src.ui.components.action_buttons.Button") as mock_button,
        ):
            mock_button.return_value.grid = MagicMock()
            instance: ActionButtons = ActionButtons.__new__(ActionButtons)
            instance._styles = mock_styles
            ActionButtons.__init__(
                instance,
                parent=MagicMock(),
                styles=mock_styles,
                on_encrypt=mock_on_encrypt,
                on_decrypt=mock_on_decrypt,
            )

        second_call_kwargs: dict = mock_button.call_args_list[1].kwargs
        assert second_call_kwargs.get("bg") == mock_styles.GREEN_COLOR
