from src.utils.utils import get_text

def test_get_text(test_path_txt: str, test_txt: str) -> None:
    text_from_file = get_text(path=test_path_txt)

    assert text_from_file
    assert type(text_from_file) == str
    assert text_from_file == test_txt