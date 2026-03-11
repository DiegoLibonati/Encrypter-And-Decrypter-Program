import os
from unittest.mock import MagicMock, mock_open, patch

import pytest

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

    def test_base_path_is_stored(self, file_service_with_base_path: FileService) -> None:
        assert file_service_with_base_path.base_path == "/base/path"


class TestFileServiceResolvePath:
    def test_returns_filename_when_no_base_path(self, file_service: FileService) -> None:
        result: str = file_service._resolve_path("file.txt")
        assert result == "file.txt"

    def test_returns_joined_path_when_base_path_set(self, file_service_with_base_path: FileService) -> None:
        result: str = file_service_with_base_path._resolve_path("file.txt")
        assert result == os.path.join("/base/path", "file.txt")


class TestFileServiceGetText:
    def test_raises_value_error_when_filename_is_empty(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="path in order to find a file"):
            file_service.get_text("")

    def test_raises_value_error_when_not_txt_extension(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="txt file"):
            file_service.get_text("document.pdf")

    def test_returns_file_content(self, file_service: FileService) -> None:
        with patch("builtins.open", mock_open(read_data="hello content")):
            result: str = file_service.get_text("file.txt")
        assert result == "hello content"

    def test_opens_file_in_read_mode(self, file_service: FileService) -> None:
        with patch("builtins.open", mock_open(read_data="content")) as mock_file:
            file_service.get_text("file.txt")
        mock_file.assert_called_once_with("file.txt", "r")

    def test_uses_base_path_when_set(self, file_service_with_base_path: FileService) -> None:
        expected_path: str = os.path.join("/base/path", "file.txt")
        with patch("builtins.open", mock_open(read_data="content")) as mock_file:
            file_service_with_base_path.get_text("file.txt")
        mock_file.assert_called_once_with(expected_path, "r")


class TestFileServiceEncryptFile:
    def test_raises_value_error_when_filename_is_empty(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="path in order to find a file"):
            file_service.encrypt_file("")

    def test_raises_value_error_when_not_txt_extension(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="txt file"):
            file_service.encrypt_file("document.pdf")

    def test_writes_encrypted_content(self, file_service: FileService) -> None:
        original: str = "abc"
        expected_encrypted: str = "bcd"
        with (
            patch.object(file_service, "get_text", return_value=original),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.encrypt_file("file.txt")

        handle: MagicMock = mock_file()
        handle.write.assert_called_once_with(expected_encrypted)

    def test_each_char_is_shifted_by_one(self, file_service: FileService) -> None:
        original: str = "Hello"
        with (
            patch.object(file_service, "get_text", return_value=original),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.encrypt_file("file.txt")

        handle: MagicMock = mock_file()
        written: str = handle.write.call_args[0][0]
        assert written == "Ifmmp"

    def test_opens_file_in_write_mode(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "get_text", return_value="text"),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.encrypt_file("file.txt")

        mock_file.assert_called_once_with("file.txt", "w")


class TestFileServiceDecryptFile:
    def test_raises_value_error_when_filename_is_empty(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="path in order to find a file"):
            file_service.decrypt_file("")

    def test_raises_value_error_when_not_txt_extension(self, file_service: FileService) -> None:
        with pytest.raises(ValueError, match="txt file"):
            file_service.decrypt_file("document.pdf")

    def test_writes_decrypted_content(self, file_service: FileService) -> None:
        encrypted: str = "bcd"
        expected_decrypted: str = "abc"
        with (
            patch.object(file_service, "get_text", return_value=encrypted),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.decrypt_file("file.txt")

        handle: MagicMock = mock_file()
        handle.write.assert_called_once_with(expected_decrypted)

    def test_each_char_is_shifted_back_by_one(self, file_service: FileService) -> None:
        encrypted: str = "Ifmmp"
        with (
            patch.object(file_service, "get_text", return_value=encrypted),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.decrypt_file("file.txt")

        handle: MagicMock = mock_file()
        written: str = handle.write.call_args[0][0]
        assert written == "Hello"

    def test_opens_file_in_write_mode(self, file_service: FileService) -> None:
        with (
            patch.object(file_service, "get_text", return_value="text"),
            patch("builtins.open", mock_open()) as mock_file,
        ):
            file_service.decrypt_file("file.txt")

        mock_file.assert_called_once_with("file.txt", "w")

    def test_encrypt_then_decrypt_restores_original(self, file_service: FileService) -> None:
        original: str = "Hello World"
        encrypted: str = "".join(chr(ord(c) + 1) for c in original)
        decrypted: str = "".join(chr(ord(c) - 1) for c in encrypted)
        assert decrypted == original
