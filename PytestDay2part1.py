#import pytest
#import _pytest

from Day2Part1 import intcode


def test_intcode():
    nums = [1, 0, 0, 0, 99]
    expected_output = [2, 0, 0, 0, 99]
    assert intcode(nums) == expected_output

    nums = [2, 3, 0, 3, 99]
    expected_output = [2, 3, 0, 6, 99]
    assert intcode(nums) == expected_output

    nums = [2, 4, 4, 5, 99, 0]
    expected_output = [2, 4, 4, 5, 99, 9801]
    assert intcode(nums) == expected_output

    nums = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    expected_output = [30, 1, 1, 4, 2, 5, 6, 0, 99]
    assert intcode(nums) == expected_output

def test_main_program():
    with open("Day2Part2_Aoc.txt") as file:
        program = file.read()
        program = [int(n) for n in program.split(",")]
        program[1] = 12
        program[2] = 2
        intcode(program)
        assert program[0] == 3850704
