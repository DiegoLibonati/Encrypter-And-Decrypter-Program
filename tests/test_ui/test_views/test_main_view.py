import tkinter as tk
from unittest.mock import MagicMock

from src.ui.components.action_buttons import ActionButtons
from src.ui.components.file_importer import FileImporter
from src.ui.styles import Styles
from src.ui.views.main_view import MainView


class TestMainView:
    def test_instantiation(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert view is not None

    def test_is_frame(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert isinstance(view, tk.Frame)

    def test_background_color(self, root: tk.Tk) -> None:
        styles: Styles = Styles()
        view: MainView = MainView(
            root=root,
            styles=styles,
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert view.cget("bg") == styles.WHITE_COLOR

    def test_result_label_starts_empty(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert view._label_operation_result.get() == ""

    def test_set_result_updates_label(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        view.set_result("Successfully encrypted.")
        assert view._label_operation_result.get() == "Successfully encrypted."

    def test_set_result_overwrites_previous(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        view.set_result("first result")
        view.set_result("second result")
        assert view._label_operation_result.get() == "second result"

    def test_set_import_label_delegates_to_file_importer(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        view.set_import_label("/path/to/file.txt")
        assert view._file_importer._label_import_file.get() == "/path/to/file.txt"

    def test_file_importer_is_correct_type(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert isinstance(view._file_importer, FileImporter)

    def test_action_buttons_is_correct_type(self, root: tk.Tk) -> None:
        view: MainView = MainView(
            root=root,
            styles=Styles(),
            on_import=MagicMock(),
            on_encrypt=MagicMock(),
            on_decrypt=MagicMock(),
        )
        assert isinstance(view._action_buttons, ActionButtons)
