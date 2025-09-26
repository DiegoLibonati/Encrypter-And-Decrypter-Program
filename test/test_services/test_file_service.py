from pathlib import Path

import pytest

from src.services.file_service import FileService


@pytest.fixture
def file_service() -> FileService:
    return FileService()


def test_get_text_reads_file(tmp_path: Path, file_service: FileService) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello")

    result = file_service.get_text(str(file_path))

    assert result == "hello"


def test_encrypt_file_and_decrypt_file(
    tmp_path: Path, file_service: FileService
) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text("abc")

    file_service.encrypt_file(str(file_path))
    encrypted_content = file_path.read_text()

    assert encrypted_content != "abc"
    assert all(ord(c) == ord(o) + 1 for c, o in zip(encrypted_content, "abc"))

    file_service.decrypt_file(str(file_path))
    decrypted_content = file_path.read_text()

    assert decrypted_content == "abc"


def test_encrypt_file_invalid_path(file_service: FileService) -> None:
    with pytest.raises(ValueError) as exc_info:
        file_service.encrypt_file("")

    assert (
        str(exc_info.value)
        == "You must enter a path in order to find a file to encrypt."
    )


def test_encrypt_file_invalid_txt(tmp_path: Path, file_service: FileService) -> None:
    file_path = tmp_path / "test.bin"
    file_path.write_bytes(b"\x00\x01")

    with pytest.raises(ValueError) as exc_info:
        file_service.encrypt_file(str(file_path))

    assert str(exc_info.value) == "You must insert a txt file to encrypt."


def test_decrypt_file_invalid_path(file_service: FileService) -> None:
    with pytest.raises(ValueError) as exc_info:
        file_service.decrypt_file("")

    assert (
        str(exc_info.value)
        == "You must enter a path in order to find a file to decrypt."
    )


def test_decrypt_file_invalid_txt(tmp_path: Path, file_service: FileService) -> None:
    file_path = tmp_path / "test.bin"
    file_path.write_bytes(b"\x00\x01")

    with pytest.raises(ValueError) as exc_info:
        file_service.decrypt_file(str(file_path))

    assert str(exc_info.value) == "You must insert a txt file to decrypt."
