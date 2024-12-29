def get_text(path: str) -> str:
    text = open(path, "r")
    text_read = text.read()
    text.close()

    return text_read
