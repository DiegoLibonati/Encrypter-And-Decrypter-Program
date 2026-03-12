from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FILE_TYPE,
    MESSAGE_NOT_VALID_PATH,
    MESSAGE_SUCCESS_DECRYPTED,
    MESSAGE_SUCCESS_ENCRYPTED,
)


class TestMessages:
    def test_success_encrypted_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_ENCRYPTED, str)

    def test_success_encrypted_is_not_empty(self) -> None:
        assert len(MESSAGE_SUCCESS_ENCRYPTED) > 0

    def test_success_decrypted_is_string(self) -> None:
        assert isinstance(MESSAGE_SUCCESS_DECRYPTED, str)

    def test_success_decrypted_is_not_empty(self) -> None:
        assert len(MESSAGE_SUCCESS_DECRYPTED) > 0

    def test_error_app_is_string(self) -> None:
        assert isinstance(MESSAGE_ERROR_APP, str)

    def test_error_app_is_not_empty(self) -> None:
        assert len(MESSAGE_ERROR_APP) > 0

    def test_not_valid_path_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_PATH, str)

    def test_not_valid_path_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_PATH) > 0

    def test_not_valid_file_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_VALID_FILE_TYPE, str)

    def test_not_valid_file_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_VALID_FILE_TYPE) > 0

    def test_not_found_dialog_type_is_string(self) -> None:
        assert isinstance(MESSAGE_NOT_FOUND_DIALOG_TYPE, str)

    def test_not_found_dialog_type_is_not_empty(self) -> None:
        assert len(MESSAGE_NOT_FOUND_DIALOG_TYPE) > 0

    def test_all_messages_are_unique(self) -> None:
        all_messages: list[str] = [
            MESSAGE_SUCCESS_ENCRYPTED,
            MESSAGE_SUCCESS_DECRYPTED,
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_PATH,
            MESSAGE_NOT_VALID_FILE_TYPE,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ]
        assert len(all_messages) == len(set(all_messages))
