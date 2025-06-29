from data.homework_test_case import HomeworkTestCase
from data.homework_test_suite import HomeworkTestSuite

test_suite = HomeworkTestSuite([
    HomeworkTestCase(
        description="Straight path to goal",
        args=["1", "1"],
        expected_output="""\
########
#......#
#.####.#
#.#g#..#
#.#.##.#
#.#....#
#.######
#......#
########"""
    ),
    HomeworkTestCase(
        description="Start near goal with wall in between",
        args=["3", "3"],
        expected_output="""\
########
#      #
# #### #
#.#g#  #
#.#.## #
#.#    #
#.###### 
#......#
########"""
    ),
    HomeworkTestCase(
        description="Start in dead-end, must backtrack",
        args=["1", "5"],
        expected_output="""\
########
#....x.#
#.####x#
#.#g#xx#
#.#.##x#
#.#....#
#.######
#......#
########"""
    ),
    HomeworkTestCase(
        description="Goal unreachable due to walls",
        args=["1", "1"],
        expected_output="Goal not reachable"
    )
])

