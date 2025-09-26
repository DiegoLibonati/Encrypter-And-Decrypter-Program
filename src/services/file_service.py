class FileService:
    def __init__(self, base_path: str = ""):
        self.base_path = base_path

    def get_text(self, filename: str) -> str:
        path = self._resolve_path(filename)
        if not filename:
            raise ValueError("You must enter a path in order to find a file.")
        if not filename.endswith(".txt"):
            raise ValueError("You must insert a txt file.")
        with open(path, "r") as f:
            return f.read()

    def encrypt_file(self, filename: str) -> None:
        if not filename:
            raise ValueError(
                "You must enter a path in order to find a file to encrypt."
            )
        if not filename.endswith(".txt"):
            raise ValueError("You must insert a txt file to encrypt.")

        path = self._resolve_path(filename)
        text = self.get_text(filename)
        encrypted_text = "".join(chr(ord(c) + 1) for c in text)
        with open(path, "w") as f:
            f.write(encrypted_text)

    def decrypt_file(self, filename: str) -> None:
        if not filename:
            raise ValueError(
                "You must enter a path in order to find a file to decrypt."
            )
        if not filename.endswith(".txt"):
            raise ValueError("You must insert a txt file to decrypt.")

        path = self._resolve_path(filename)
        text = self.get_text(filename)
        decrypted_text = "".join(chr(ord(c) - 1) for c in text)
        with open(path, "w") as f:
            f.write(decrypted_text)

    def _resolve_path(self, filename: str) -> str:
        import os

        if self.base_path:
            return os.path.join(self.base_path, filename)
        return filename
