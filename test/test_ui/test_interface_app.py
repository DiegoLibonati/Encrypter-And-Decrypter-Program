import logging

import pytest

from src.ui.interface_app import InterfaceApp
from src.utils.styles import WHITE_COLOR

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_initial_config_tk_app(interface_app: InterfaceApp) -> None:
    root = interface_app._root
    root.update()

    title = root.title()
    geometry = root.geometry().split("+")[0]
    resizable = root.resizable()
    config_bg = root.cget("bg")

    assert title == "Encrypter And Decrypter"
    assert geometry == "800x300"
    assert resizable == (False, False)
    assert config_bg == WHITE_COLOR


def test_encrypt_file_invalid_path(interface_app: InterfaceApp) -> None:
    interface_app._path = ""
    interface_app._encrypt_file()

    assert (
        interface_app._label_operation_result.get()
        == "You must enter a path in order to find a file to encrypt."
    )


def test_decrypt_file_invalid_path(interface_app: InterfaceApp) -> None:
    interface_app._path = ""
    interface_app._decrypt_file()

    assert (
        interface_app._label_operation_result.get()
        == "You must enter a path in order to find a file to decrypt."
    )


def test_encrypt_file_success(
    monkeypatch: pytest.MonkeyPatch, interface_app: InterfaceApp
) -> None:
    interface_app._path = "fake.txt"

    def mock_encrypt(path: str) -> None:
        assert path == "fake.txt"

    monkeypatch.setattr(interface_app._file_service, "encrypt_file", mock_encrypt)

    interface_app._encrypt_file()
    assert interface_app._label_operation_result.get() == "Successfully encrypted."


def test_encrypt_file_invalid_txt(
    monkeypatch: pytest.MonkeyPatch, interface_app: InterfaceApp
) -> None:
    interface_app._path = "fake.txt"

    def mock_encrypt(path: str) -> None:
        raise ValueError("You must insert a txt file to encrypt.")

    monkeypatch.setattr(interface_app._file_service, "encrypt_file", mock_encrypt)

    interface_app._encrypt_file()
    assert (
        interface_app._label_operation_result.get()
        == "You must insert a txt file to encrypt."
    )


def test_decrypt_file_success(
    monkeypatch: pytest.MonkeyPatch, interface_app: InterfaceApp
) -> None:
    interface_app._path = "fake.txt"

    def mock_decrypt(path: str) -> None:
        assert path == "fake.txt"

    monkeypatch.setattr(interface_app._file_service, "decrypt_file", mock_decrypt)

    interface_app._decrypt_file()
    assert interface_app._label_operation_result.get() == "Successfully decrypted."


def test_decrypt_file_invalid_txt(
    monkeypatch: pytest.MonkeyPatch, interface_app: InterfaceApp
) -> None:
    interface_app._path = "fake.txt"

    def mock_decrypt(path: str) -> None:
        raise ValueError("You must insert a txt file to decrypt.")

    monkeypatch.setattr(interface_app._file_service, "decrypt_file", mock_decrypt)

    interface_app._decrypt_file()
    assert (
        interface_app._label_operation_result.get()
        == "You must insert a txt file to decrypt."
    )
