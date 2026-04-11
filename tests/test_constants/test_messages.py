from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FILE_TYPE,
    MESSAGE_NOT_VALID_PATH,
    MESSAGE_SUCCESS_DECRYPTED,
    MESSAGE_SUCCESS_ENCRYPTED,
)


class TestMessages:
    def test_message_success_encrypted(self) -> None:
        assert MESSAGE_SUCCESS_ENCRYPTED == "Successfully encrypted."

    def test_message_success_decrypted(self) -> None:
        assert MESSAGE_SUCCESS_DECRYPTED == "Successfully decrypted."

    def test_message_error_app(self) -> None:
        assert MESSAGE_ERROR_APP == "Internal error. Contact a developer."

    def test_message_not_valid_path(self) -> None:
        assert MESSAGE_NOT_VALID_PATH == "You must enter a path in order to find a file."

    def test_message_not_valid_file_type(self) -> None:
        assert MESSAGE_NOT_VALID_FILE_TYPE == "You must insert a txt file."

    def test_message_not_found_dialog_type(self) -> None:
        assert MESSAGE_NOT_FOUND_DIALOG_TYPE == "The type of dialog to display is not found."

    def test_all_messages_are_non_empty_strings(self) -> None:
        messages: list[str] = [
            MESSAGE_SUCCESS_ENCRYPTED,
            MESSAGE_SUCCESS_DECRYPTED,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_PATH,
            MESSAGE_NOT_VALID_FILE_TYPE,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        for msg in messages:
            assert isinstance(msg, str)
            assert len(msg) > 0
