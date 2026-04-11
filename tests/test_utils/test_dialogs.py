from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class TestBaseDialog:
    def test_default_dialog_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom error")
        assert dialog.message == "custom error"

    def test_none_message_keeps_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_to_dict_returns_correct_structure(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test msg"

    def test_to_dict_has_all_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_open_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test error")
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once_with("Error", "test error")

    def test_open_warning_calls_showwarning(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING
            message = "warn msg"

        dialog: WarningDialog = WarningDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once_with("Warning", "warn msg")

    def test_open_info_calls_showinfo(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO
            message = "info msg"

        dialog: InfoDialog = InfoDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()
            mock_handler.assert_called_once_with("Information", "info msg")

    def test_open_invalid_type_calls_showerror_with_not_found(self) -> None:
        class BadDialog(BaseDialog):
            dialog_type = "INVALID"

        dialog: BadDialog = BadDialog()
        with patch("src.utils.dialogs.messagebox.showerror") as mock_error:
            dialog.open()
            mock_error.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)

    def test_title_falls_back_to_error_on_unknown_type(self) -> None:
        class BadDialog(BaseDialog):
            dialog_type = "UNKNOWN"

        dialog: BadDialog = BadDialog()
        assert dialog.title == "Error"

    def test_error_constant(self) -> None:
        assert BaseDialog.ERROR == "Error"

    def test_warning_constant(self) -> None:
        assert BaseDialog.WARNING == "Warning"

    def test_info_constant(self) -> None:
        assert BaseDialog.INFO == "Info"


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, Exception)

    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert isinstance(error, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        error: BaseDialogError = BaseDialogError()
        assert error.message == MESSAGE_ERROR_APP

    def test_can_be_raised(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()

    def test_is_base_dialog_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert isinstance(error, BaseDialogError)

    def test_custom_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="bad input")
        assert error.message == "bad input"

    def test_dialog_type_is_error(self) -> None:
        error: ValidationDialogError = ValidationDialogError()
        assert error.dialog_type == BaseDialog.ERROR


class TestAuthenticationDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(AuthenticationDialogError):
            raise AuthenticationDialogError()

    def test_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()
        assert error.message == "Authentication error"

    def test_custom_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError(message="invalid token")
        assert error.message == "invalid token"


class TestNotFoundDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(NotFoundDialogError):
            raise NotFoundDialogError()

    def test_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()
        assert error.message == "Resource not found"


class TestConflictDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(ConflictDialogError):
            raise ConflictDialogError()

    def test_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()
        assert error.message == "Conflict error"


class TestBusinessDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(BusinessDialogError):
            raise BusinessDialogError()

    def test_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()
        assert error.message == "Business rule violated"


class TestInternalDialogError:
    def test_is_exception(self) -> None:
        with pytest.raises(InternalDialogError):
            raise InternalDialogError()

    def test_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()
        assert error.message == "Internal error"

    def test_custom_message(self) -> None:
        error: InternalDialogError = InternalDialogError(message="db connection failed")
        assert error.message == "db connection failed"


class TestBaseDialogNotification:
    def test_is_not_exception(self) -> None:
        notification: BaseDialogNotification = BaseDialogNotification()
        assert not isinstance(notification, Exception)

    def test_is_base_dialog(self) -> None:
        notification: BaseDialogNotification = BaseDialogNotification()
        assert isinstance(notification, BaseDialog)


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.message == "This feature is deprecated"

    def test_title_is_warning(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert warning.title == "Warning"

    def test_is_not_exception(self) -> None:
        warning: DeprecatedDialogWarning = DeprecatedDialogWarning()
        assert not isinstance(warning, Exception)


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.message == "Operation completed successfully"

    def test_title_is_information(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert info.title == "Information"

    def test_is_not_exception(self) -> None:
        info: SuccessDialogInformation = SuccessDialogInformation()
        assert not isinstance(info, Exception)
