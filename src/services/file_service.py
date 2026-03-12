import os

from src.constants.messages import MESSAGE_NOT_VALID_FILE_TYPE, MESSAGE_NOT_VALID_PATH
from src.utils.dialogs import ValidationDialogError


class FileService:
    def __init__(self, base_path: str = ""):
        self.base_path = base_path

    def get_text(self, filename: str) -> str:
        path = self._resolve_path(filename)
        if not filename:
            ValidationDialogError(message=MESSAGE_NOT_VALID_PATH).dialog()
            return
        if not filename.endswith(".txt"):
            ValidationDialogError(message=MESSAGE_NOT_VALID_FILE_TYPE).dialog()
            return

        with open(path) as f:
            return f.read()

    def encrypt_file(self, filename: str) -> bool:
        if not filename:
            ValidationDialogError(message=MESSAGE_NOT_VALID_PATH).dialog()
            return False

        if not filename.endswith(".txt"):
            ValidationDialogError(message=MESSAGE_NOT_VALID_FILE_TYPE).dialog()
            return False

        path = self._resolve_path(filename)
        text = self.get_text(filename)
        encrypted_text = "".join(chr(ord(c) + 1) for c in text)
        with open(path, "w") as f:
            f.write(encrypted_text)

        return True

    def decrypt_file(self, filename: str) -> bool:
        if not filename:
            ValidationDialogError(message=MESSAGE_NOT_VALID_PATH).dialog()
            return False
        if not filename.endswith(".txt"):
            ValidationDialogError(message=MESSAGE_NOT_VALID_FILE_TYPE).dialog()
            return False

        path = self._resolve_path(filename)
        text = self.get_text(filename)
        decrypted_text = "".join(chr(ord(c) - 1) for c in text)
        with open(path, "w") as f:
            f.write(decrypted_text)

        return True

    def _resolve_path(self, filename: str) -> str:
        if self.base_path:
            return os.path.join(self.base_path, filename)
        return filename
