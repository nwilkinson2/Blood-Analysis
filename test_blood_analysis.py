import pytest


@pytest.mark.parametrize("HDL_result, expected",
                         [(70, "Good"),
                          (45, "Borderline"),
                          (18, "Bad")])
def test_HDL_analysis(HDL_result, expected):
    from blood_analysis import HDL_analysis
    answer = HDL_analysis(HDL_result)
    assert answer == expected


def test_LDL_analysis():
    from blood_analysis import LDL_analysis
    answer = LDL_analysis(129)
    expected = "Normal"
    assert answer == expected


def test_line_generation():
    from blood_analysis import line_generation
    answer = line_generation((1, 1), (3, 3), 2)
    expected = 2
    assert answer == expected


def test_line_equation():
    from blood_analysis import line_equation
    m, b = line_equation((1, 1), (4, 4))
    assert m == 1
    assert b == 0


def test_line_check():
    from blood_analysis import line_check
    answer = line_check((1, 1), (5, 5), (10, 10))
    expected = True
    assert answer == expected


def test_line_check_falsecase():
    from blood_analysis import line_check
    answer = line_check((1, 1), (5, 5), (10, 9))
    expected = False
    assert answer == expected
