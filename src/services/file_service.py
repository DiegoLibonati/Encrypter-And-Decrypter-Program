def get_text(path: str) -> str:
    if not path:
        raise ValueError("You must enter a path in order to find a file.")

    if not path.endswith(".txt"):
        raise ValueError("You must insert a txt file.")

    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise ValueError("Error reading file.") from e


def encrypt_file(path: str) -> None:
    if not path:
        raise ValueError("You must enter a path in order to find a file to encrypt.")
    if not path.endswith(".txt"):
        raise ValueError("You must insert a txt file to encrypt.")

    text = get_text(path)
    encrypted_text = "".join(chr(ord(letter) + 1) for letter in text)

    with open(path, "w") as f:
        f.write(encrypted_text)


def decrypt_file(path: str) -> None:
    if not path:
        raise ValueError("You must enter a path in order to find a file to decrypt.")
    if not path.endswith(".txt"):
        raise ValueError("You must insert a txt file to decrypt.")

    text = get_text(path)
    decrypted_text = "".join(chr(ord(letter) - 1) for letter in text)

    with open(path, "w") as f:
        f.write(decrypted_text)
