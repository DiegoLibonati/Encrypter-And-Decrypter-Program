import os

from src.constants.messages import MESSAGE_NOT_VALID_FILE_TYPE, MESSAGE_NOT_VALID_PATH
from src.utils.dialogs import ValidationDialogError


class FileService:
    def __init__(self, base_path: str = ""):
        self.base_path = base_path

    def encrypt_file(self, filepath: str) -> bool:
        if not self._validate(filepath=filepath):
            return False

        path = self._resolve_path(filepath=filepath)
        text = self._get_text(filepath=filepath)
        encrypted_text = "".join(chr(ord(c) + 1) for c in text)
        with open(path, "w") as f:
            f.write(encrypted_text)

        return True

    def decrypt_file(self, filepath: str) -> bool:
        if not self._validate(filepath=filepath):
            return False

        path = self._resolve_path(filepath=filepath)
        text = self._get_text(filepath=filepath)
        decrypted_text = "".join(chr(ord(c) - 1) for c in text)
        with open(path, "w") as f:
            f.write(decrypted_text)

        return True

    def _validate(self, filepath: str) -> bool:
        if not filepath:
            ValidationDialogError(message=MESSAGE_NOT_VALID_PATH).dialog()
            return False
        if not filepath.endswith(".txt"):
            ValidationDialogError(message=MESSAGE_NOT_VALID_FILE_TYPE).dialog()
            return False
        return True

    def _resolve_path(self, filepath: str) -> str:
        if self.base_path:
            return os.path.join(self.base_path, filepath)
        return filepath

    def _get_text(self, filepath: str) -> str:
        path = self._resolve_path(filepath=filepath)
        with open(path) as f:
            return f.read()
