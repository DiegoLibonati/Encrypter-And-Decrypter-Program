import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.file_importer import FileImporter
from src.ui.styles import Styles


class TestFileImporter:
    def test_instantiation(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        assert importer is not None

    def test_is_frame(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        assert isinstance(importer, tk.Frame)

    def test_background_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        importer: FileImporter = FileImporter(
            parent=root,
            styles=styles,
            on_import=MagicMock(),
        )
        assert importer.cget("bg") == styles.WHITE_COLOR

    def test_label_starts_empty(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        assert importer._label_import_file.get() == ""

    def test_set_path_updates_label(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        importer.set_path("/some/file.txt")
        assert importer._label_import_file.get() == "/some/file.txt"

    def test_set_path_overwrites_previous_value(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        importer.set_path("/first/path.txt")
        importer.set_path("/second/path.txt")
        assert importer._label_import_file.get() == "/second/path.txt"

    def test_set_path_with_empty_string(self, root: tk.Tk) -> None:
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=MagicMock(),
        )
        importer.set_path("/some/file.txt")
        importer.set_path("")
        assert importer._label_import_file.get() == ""

    def test_on_import_callback_stored(self, root: tk.Tk) -> None:
        on_import: MagicMock = MagicMock()
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=on_import,
        )
        assert importer._on_import is on_import

    def test_on_import_callback_called(self, root: tk.Tk) -> None:
        on_import: MagicMock = MagicMock()
        importer: FileImporter = FileImporter(
            parent=root,
            styles=Styles(),
            on_import=on_import,
        )
        importer._on_import()
        on_import.assert_called_once()
