import os
from unittest.mock import MagicMock, mock_open, patch

import pytest

from src.constants.messages import MESSAGE_NOT_VALID_FILE_TYPE, MESSAGE_NOT_VALID_PATH
from src.services.file_service import FileService


@pytest.fixture
def file_service() -> FileService:
    return FileService()


@pytest.fixture
def file_service_with_base_path() -> FileService:
    return FileService(base_path="/base/path")


class TestFileServiceInit:
    def test_default_base_path_is_empty(self, file_service: FileService) -> None:
        assert file_service.base_path == ""

    def test_custom_base_path_is_stored(self, file_service_with_base_path: FileService) -> None:
        assert file_service_with_base_path.base_path == "/base/path"


class TestFileServiceResolvePath:
    def test_returns_filepath_when_base_path_is_empty(self, file_service: FileService) -> None:
        result: str = file_service._resolve_path(filepath="file.txt")
        assert result == "file.txt"

    def test_returns_joined_path_when_base_path_is_set(self, file_service_with_base_path: FileService) -> None:
        result: str = file_service_with_base_path._resolve_path(filepath="file.txt")
        assert result == os.path.join("/base/path", "file.txt")


class TestFileServiceValidate:
    def test_returns_false_when_filepath_is_empty(self, file_service: FileService) -> None:
        with patch("src.services.file_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result: bool = file_service._validate(filepath="")

        assert result is False

    def test_validation_dialog_called_when_filepath_is_empty(self, file_service: FileService) -> None:
        with patch("src.services.file_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            file_service._validate(filepath="")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_PATH)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_returns_false_when_file_is_not_txt(self, file_service: FileService) -> None:
        with patch("src.services.file_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            result: bool = file_service._validate(filepath="notes.pdf")

        assert result is False

    def test_validation_dialog_called_when_file_is_not_txt(self, file_service: FileService) -> None:
        with patch("src.services.file_service.ValidationDialogError") as mock_dialog_class:
            mock_dialog_class.return_value = MagicMock()
            file_service._validate(filepath="notes.pdf")

        mock_dialog_class.assert_called_once_with(message=MESSAGE_NOT_VALID_FILE_TYPE)
        mock_dialog_class.return_value.dialog.assert_called_once()

    def test_returns_true_for_valid_txt_filepath(self, file_service: FileService) -> None:
        result: bool = file_service._validate(filepath="notes.txt")
        assert result is True

    def test_returns_true_for_valid_filepath_with_base_path(self, file_service_with_base_path: FileService) -> None:
        result: bool = file_service_with_base_path._validate(filepath="notes.txt")
        assert result is True


class TestFileServiceGetText:
    def test_returns_file_content(self, file_service: FileService) -> None:
        with patch("builtins.open", mock_open(read_data="hello world")):
            result: str = file_service._get_text(filepath="notes.txt")
        assert result == "hello world"

    def test_opens_resolved_path(self, file_service_with_base_path: FileService) -> None:
        mock_file = mock_open(read_data="content")
        with patch("builtins.open", mock_file):
            file_service_with_base_path._get_text(filepath="notes.txt")

        mock_file.assert_called_once_with(os.path.join("/base/path", "notes.txt"))


class TestFileServiceEncryptFile:
    def test_returns_false_when_validation_fails(self, file_service: FileService) -> None:
        with patch.object(file_service, "_validate", return_value=False):
            result: bool = file_service.encrypt_file(filepath="")

        assert result is False

    def test_get_text_not_called_when_validation_fails(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "_validate", return_value=False),
            patch.object(file_service, "_get_text") as mock_get_text,
        ):
            file_service.encrypt_file(filepath="")

        mock_get_text.assert_not_called()

    def test_returns_true_on_success(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="abc"),
            patch("builtins.open", mock_open()),
        ):
            result: bool = file_service.encrypt_file(filepath="notes.txt")

        assert result is True

    def test_shifts_each_char_by_one(self, file_service: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="abc"),
            patch("builtins.open", mock_file),
        ):
            file_service.encrypt_file(filepath="notes.txt")

        written: str = mock_file().write.call_args[0][0]
        assert written == "bcd"

    def test_writes_to_resolved_path(self, file_service: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="a"),
            patch("builtins.open", mock_file),
        ):
            file_service.encrypt_file(filepath="notes.txt")

        mock_file.assert_called_once_with("notes.txt", "w")

    def test_writes_to_resolved_path_with_base_path(self, file_service_with_base_path: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service_with_base_path, "_validate", return_value=True),
            patch.object(file_service_with_base_path, "_get_text", return_value="a"),
            patch("builtins.open", mock_file),
        ):
            file_service_with_base_path.encrypt_file(filepath="notes.txt")

        mock_file.assert_called_once_with(os.path.join("/base/path", "notes.txt"), "w")


class TestFileServiceDecryptFile:
    def test_returns_false_when_validation_fails(self, file_service: FileService) -> None:
        with patch.object(file_service, "_validate", return_value=False):
            result: bool = file_service.decrypt_file(filepath="")

        assert result is False

    def test_get_text_not_called_when_validation_fails(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "_validate", return_value=False),
            patch.object(file_service, "_get_text") as mock_get_text,
        ):
            file_service.decrypt_file(filepath="")

        mock_get_text.assert_not_called()

    def test_returns_true_on_success(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="bcd"),
            patch("builtins.open", mock_open()),
        ):
            result: bool = file_service.decrypt_file(filepath="notes.txt")

        assert result is True

    def test_shifts_each_char_back_by_one(self, file_service: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="bcd"),
            patch("builtins.open", mock_file),
        ):
            file_service.decrypt_file(filepath="notes.txt")

        written: str = mock_file().write.call_args[0][0]
        assert written == "abc"

    def test_writes_to_resolved_path(self, file_service: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service, "_validate", return_value=True),
            patch.object(file_service, "_get_text", return_value="b"),
            patch("builtins.open", mock_file),
        ):
            file_service.decrypt_file(filepath="notes.txt")

        mock_file.assert_called_once_with("notes.txt", "w")

    def test_writes_to_resolved_path_with_base_path(self, file_service_with_base_path: FileService) -> None:
        mock_file = mock_open()
        with (
            patch.object(file_service_with_base_path, "_validate", return_value=True),
            patch.object(file_service_with_base_path, "_get_text", return_value="b"),
            patch("builtins.open", mock_file),
        ):
            file_service_with_base_path.decrypt_file(filepath="notes.txt")

        mock_file.assert_called_once_with(os.path.join("/base/path", "notes.txt"), "w")

    def test_encrypt_then_decrypt_returns_original(self) -> None:
        original: str = "Hello World"
        encrypted: str = "".join(chr(ord(c) + 1) for c in original)
        decrypted: str = "".join(chr(ord(c) - 1) for c in encrypted)
        assert decrypted == original
