from functions_3a import is_ascending, word_concat


def test_is_ascending():
    assert is_ascending(1, 2, 3)


def test_is_ascending_eq():
    assert not is_ascending(1, 1, 1)


def test_not_ascending():
    assert not is_ascending(20, 10, 1)


def test_mixed():
    assert not is_ascending(10, 20, 10)


def test_concat_first_shorter():
    assert word_concat("alma", "korte") == "almakorte"


def test_concat_first_longer():
    assert word_concat("korte", "alma") == "almakorte"


def test_concat_first_longer():
    assert word_concat("korte", "meggy") == "kortemeggy"