from app.main import get_human_age


def test_get_human_age_receive_zero_list_when_args_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_receive_zero_list_when_args_less_than_15_years() -> None:
    assert get_human_age(14, 5) == [0, 0]


def test_receive_1_human_age_when_args_equal_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_cat_receive_1_human_age_and_dog_0_when_args_equal_15_and_6_years() -> None:
    assert get_human_age(15, 6) == [1, 0]


def test_cat__and_dog_2_when_args_equal_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat__receive_3_and_dog_2_when_args_equal_28_years() -> None:
    assert get_human_age(28, 28) == [3, 2]
