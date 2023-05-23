from Day2PAart2 import intcode, calculate_output

def test_intcode():
    # Test case 1
    nums = [1, 0, 0, 0, 99]
    expected_output = [2, 0, 0, 0, 99]
    assert intcode(nums) == expected_output

    # Test case 2
    nums = [2, 3, 0, 3, 99]
    expected_output = [2, 3, 0, 6, 99]
    assert intcode(nums) == expected_output

    # Test case 3
    nums = [2, 4, 4, 5, 99, 0]
    expected_output = [2, 4, 4, 5, 99, 9801]
    assert intcode(nums) == expected_output

    # Test case 4
    nums = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected_output = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert intcode(nums) == expected_output


def test_calculate_output():
    # Test case 1
    program = [1, 0, 0, 0, 99]
    y = 2
    expected_output = 10000
    assert calculate_output(program, y) == expected_output

    # Test case 2
    program = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    y = 30
    expected_output = 1202
    assert calculate_output(program, y) == expected_output


'''import pytest
from ABC1 import intcode
def test_intcode():
    program = [1,0,0,0,99]
    result = intcode(program)
    assert result == [2,0,0,0,99]

    program = [2,3,0,3,99]
    result = intcode(program)
    assert result == [2,3,0,6,99]

    program = [2,4,4,5,99,0]
    result = intcode(program)
    assert result == [2,4,4,5,99,9801]

    program = [1,1,1,4,99,5,6,0,99]
    result = intcode(program)
    assert result == [30,1,1,4,2,5,6,0,99]
    '''