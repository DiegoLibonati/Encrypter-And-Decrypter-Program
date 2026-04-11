import os
from pathlib import Path

import pytest

from src.services.file_service import FileService
from src.utils.dialogs import ValidationDialogError


class TestFileService:
    def test_init_default_base_path(self) -> None:
        service: FileService = FileService()
        assert service.base_path == ""

    def test_init_custom_base_path(self) -> None:
        service: FileService = FileService(base_path="/some/path")
        assert service.base_path == "/some/path"

    def test_validate_empty_filepath_raises(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service._validate(filepath="")

    def test_validate_non_txt_filepath_raises(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service._validate(filepath="file.pdf")

    def test_validate_txt_filepath_returns_true(self) -> None:
        service: FileService = FileService()
        result: bool = service._validate(filepath="file.txt")
        assert result is True

    def test_resolve_path_without_base_path(self) -> None:
        service: FileService = FileService()
        result: str = service._resolve_path(filepath="file.txt")
        assert result == "file.txt"

    def test_resolve_path_with_base_path(self) -> None:
        service: FileService = FileService(base_path="/base")
        result: str = service._resolve_path(filepath="file.txt")
        assert result == os.path.join("/base", "file.txt")

    def test_get_text_reads_file(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("hello")
        service: FileService = FileService()
        result: str = service._get_text(filepath=str(file))
        assert result == "hello"

    def test_encrypt_file_returns_true(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("abc")
        service: FileService = FileService()
        result: bool = service.encrypt_file(filepath=str(file))
        assert result is True

    def test_encrypt_file_transforms_content(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("abc")
        service: FileService = FileService()
        service.encrypt_file(filepath=str(file))
        assert file.read_text() == "bcd"

    def test_decrypt_file_returns_true(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("bcd")
        service: FileService = FileService()
        result: bool = service.decrypt_file(filepath=str(file))
        assert result is True

    def test_decrypt_file_transforms_content(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("bcd")
        service: FileService = FileService()
        service.decrypt_file(filepath=str(file))
        assert file.read_text() == "abc"

    def test_encrypt_then_decrypt_restores_content(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        original: str = "Hello World!"
        file.write_text(original)
        service: FileService = FileService()
        service.encrypt_file(filepath=str(file))
        service.decrypt_file(filepath=str(file))
        assert file.read_text() == original

    def test_encrypt_file_raises_on_empty_path(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service.encrypt_file(filepath="")

    def test_encrypt_file_raises_on_non_txt(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service.encrypt_file(filepath="file.pdf")

    def test_decrypt_file_raises_on_empty_path(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service.decrypt_file(filepath="")

    def test_decrypt_file_raises_on_non_txt(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError):
            service.decrypt_file(filepath="file.pdf")

    def test_encrypt_with_base_path(self, tmp_path: Path) -> None:
        file: Path = tmp_path / "test.txt"
        file.write_text("abc")
        service: FileService = FileService(base_path=str(tmp_path))
        result: bool = service.encrypt_file(filepath="test.txt")
        assert result is True
        assert file.read_text() == "bcd"

    def test_validate_error_message_on_empty_path(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError) as exc_info:
            service._validate(filepath="")
        assert "path" in exc_info.value.message.lower()

    def test_validate_error_message_on_non_txt(self) -> None:
        service: FileService = FileService()
        with pytest.raises(ValidationDialogError) as exc_info:
            service._validate(filepath="file.csv")
        assert "txt" in exc_info.value.message.lower()
