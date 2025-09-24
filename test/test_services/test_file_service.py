from pathlib import Path

import pytest

from src.services.file_service import decrypt_file, encrypt_file, get_text


def test_get_text_reads_file(tmp_path: Path) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello")

    result = get_text(str(file_path))

    assert result == "hello"


def test_encrypt_file_and_decrypt_file(tmp_path: Path) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text("abc")

    # Encriptar
    encrypt_file(str(file_path))
    encrypted_content = file_path.read_text()

    assert encrypted_content != "abc"
    assert all(ord(c) == ord(o) + 1 for c, o in zip(encrypted_content, "abc"))

    # Desencriptar
    decrypt_file(str(file_path))
    decrypted_content = file_path.read_text()

    assert decrypted_content == "abc"


def test_encrypt_file_invalid_path() -> None:
    with pytest.raises(ValueError) as exc_info:
        encrypt_file("")

    assert (
        str(exc_info.value)
        == "You must enter a path in order to find a file to encrypt."
    )


def test_encrypt_file_invalid_txt(tmp_path: Path) -> None:
    file_path = tmp_path / "test.bin"
    file_path.write_bytes(b"\x00\x01")

    with pytest.raises(ValueError) as exc_info:
        encrypt_file(str(file_path))

    assert str(exc_info.value) == "You must insert a txt file to encrypt."


def test_decrypt_file_invalid_path() -> None:
    with pytest.raises(ValueError) as exc_info:
        decrypt_file("")

    assert (
        str(exc_info.value)
        == "You must enter a path in order to find a file to decrypt."
    )


def test_decrypt_file_invalid_txt(tmp_path: Path) -> None:
    file_path = tmp_path / "test.bin"
    file_path.write_bytes(b"\x00\x01")

    with pytest.raises(ValueError) as exc_info:
        decrypt_file(str(file_path))

    assert str(exc_info.value) == "You must insert a txt file to decrypt."
