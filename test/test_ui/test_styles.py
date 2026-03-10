from tkinter import BOTH, BOTTOM, CENTER, END, HORIZONTAL, NONE, RAISED, RIGHT, X, Y

from src.ui.styles import Styles


class TestStyles:
    def test_white_color(self) -> None:
        assert Styles.WHITE_COLOR == "#FFFFFF"

    def test_black_color(self) -> None:
        assert Styles.BLACK_COLOR == "#000000"

    def test_red_color(self) -> None:
        assert Styles.RED_COLOR == "#FF0000"

    def test_green_color(self) -> None:
        assert Styles.GREEN_COLOR == "#00FF00"

    def test_font_times_base(self) -> None:
        assert Styles.FONT_TIMES == "Times"

    def test_font_times_10(self) -> None:
        assert Styles.FONT_TIMES_10 == "Times 10"

    def test_font_times_12(self) -> None:
        assert Styles.FONT_TIMES_12 == "Times 12"

    def test_font_times_13(self) -> None:
        assert Styles.FONT_TIMES_13 == "Times 13"

    def test_font_times_14(self) -> None:
        assert Styles.FONT_TIMES_14 == "Times 14"

    def test_font_times_15(self) -> None:
        assert Styles.FONT_TIMES_15 == "Times 15"

    def test_font_times_20(self) -> None:
        assert Styles.FONT_TIMES_20 == "Times 20"

    def test_wrap_none(self) -> None:
        assert Styles.WRAP_NONE == NONE

    def test_fill_both(self) -> None:
        assert Styles.FILL_BOTH == BOTH

    def test_fill_y(self) -> None:
        assert Styles.FILL_Y == Y

    def test_fill_x(self) -> None:
        assert Styles.FILL_X == X

    def test_side_right(self) -> None:
        assert Styles.SIDE_RIGHT == RIGHT

    def test_side_bottom(self) -> None:
        assert Styles.SIDE_BOTTOM == BOTTOM

    def test_orient_horizontal(self) -> None:
        assert Styles.ORIENT_HORIZONTAL == HORIZONTAL

    def test_position_end(self) -> None:
        assert Styles.POSITION_END == END

    def test_anchor_center(self) -> None:
        assert Styles.ANCHOR_CENTER == CENTER

    def test_relief_raised(self) -> None:
        assert Styles.RELIEF_RAISED == RAISED

    def test_instantiation(self) -> None:
        styles: Styles = Styles()
        assert styles.WHITE_COLOR == "#FFFFFF"
