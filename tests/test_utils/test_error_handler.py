import types
from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_calls_open_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="invalid input")
        exc_type: type[ValidationDialogError] = ValidationDialogError
        exc_tb: MagicMock = MagicMock(spec=types.TracebackType)

        with patch.object(exc, "open") as mock_open:
            error_handler(exc_type, exc, exc_tb)
            mock_open.assert_called_once()

    def test_creates_internal_dialog_for_unknown_exception(self) -> None:
        exc: ValueError = ValueError("something broke")
        exc_type: type[ValueError] = ValueError
        exc_tb: MagicMock = MagicMock(spec=types.TracebackType)

        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(exc_type, exc, exc_tb)
            mock_internal.assert_called_once_with(message="something broke")
            mock_instance.open.assert_called_once()

    def test_internal_dialog_receives_exception_message(self) -> None:
        exc: RuntimeError = RuntimeError("connection timeout")
        exc_type: type[RuntimeError] = RuntimeError
        exc_tb: MagicMock = MagicMock(spec=types.TracebackType)

        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(exc_type, exc, exc_tb)
            mock_internal.assert_called_once_with(message="connection timeout")

    def test_base_dialog_subclass_open_is_called(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="field required")
        exc_type: type[ValidationDialogError] = ValidationDialogError
        exc_tb: MagicMock = MagicMock(spec=types.TracebackType)

        with patch.object(exc, "open") as mock_open:
            error_handler(exc_type, exc, exc_tb)
            mock_open.assert_called_once()
