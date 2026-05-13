from bad_code import poorly_formatted


def test_poorly_formatted():
    # This test will fail intentionally
    assert poorly_formatted(5, 3) == 5  # Wrong! Should be 5
