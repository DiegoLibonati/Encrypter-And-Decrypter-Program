import os
import shutil
from test.constants import DIR_TXTS, INVALID_TXT_PATH, PATH_TXT, TEXT_TXT
from tkinter import Tk

from pytest import fixture

from src.ui.interface_app import InterfaceApp


@fixture
def interface_app() -> InterfaceApp:
    root = Tk()
    return InterfaceApp(root=root)


@fixture
def test_path_txt() -> str:
    return PATH_TXT


@fixture
def test_invalid_path() -> str:
    return INVALID_TXT_PATH


@fixture
def test_txt() -> str:
    return TEXT_TXT


def pytest_sessionstart():
    """Se ejecuta antes de que comiencen los tests."""
    path_txt = PATH_TXT
    dir_txt = DIR_TXTS
    text = TEXT_TXT

    if not os.path.exists(dir_txt):
        os.makedirs(dir_txt)

    with open(path_txt, "w") as file:
        file.write(text)
        file.close()


def pytest_sessionfinish():
    """Se ejecuta después de que todos los tests hayan terminado."""
    dir = DIR_TXTS

    shutil.rmtree(path=dir)
