import logging

import pytest

from src.models.InterfaceApp import InterfaceApp
from src.utils.constants import WHITE_COLOR


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
    with pytest.raises(ValueError) as exc_info:
        interface_app._encrypt_file()

    assert str(exc_info.value) == "You must enter a path in order to find a file to encrypt."


def test_encrypt_file_invalid_txt(interface_app: InterfaceApp, test_invalid_path: str) -> None:
    interface_app._path = test_invalid_path
    interface_app._encrypt_file()

    assert interface_app._label_operation_result.get() == "You must insert a txt file to encrypt."


def test_encrypt_file(interface_app: InterfaceApp, test_path_txt: str) -> None:
    interface_app._path = test_path_txt
    interface_app._encrypt_file()

    assert interface_app._label_operation_result.get() == "Successfully encrypted."


def test_decrypt_file_invalid_path(interface_app: InterfaceApp) -> None:
    with pytest.raises(ValueError) as exc_info:
        interface_app._decrypt_file()

    assert str(exc_info.value) == "You must enter a path in order to find a file to decrypt."


def test_decrypt_file_invalid_txt(interface_app: InterfaceApp, test_invalid_path: str) -> None:
    interface_app._path = test_invalid_path
    interface_app._decrypt_file()

    assert interface_app._label_operation_result.get() == "You must insert a txt file to decrypt."


def test_decrypt_file(interface_app: InterfaceApp, test_path_txt: str) -> None:
    interface_app._path = test_path_txt
    interface_app._decrypt_file()

    assert interface_app._label_operation_result.get() == "Successfully decrypted."