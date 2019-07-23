# -*- coding: utf-8 -*-
import pytest

from solution.solutions import solution_1124, solution_1125


@pytest.mark.parametrize("hours, expected",
                         [
                             pytest.param([9, 9, 6, 0, 6, 6, 9], 3),
                             pytest.param([1, 2, 3, 9, 8, 9, 10, 1, 2, 3], 5),
                             pytest.param([1], 0),
                             pytest.param([9], 1),
                             pytest.param([], 0)
                         ])
def test_solution_1124(hours, expected):
    result = solution_1124(hours)
    assert result == expected


@pytest.mark.parametrize("req_skills, people, expected",
                         [
                             pytest.param(
                                 ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
                                 [["algorithms", "math", "java"],
                                  ["algorithms", "math", "reactjs"],
                                  ["java", "csharp", "aws"],
                                  ["reactjs", "csharp"],
                                  ["csharp", "math"],
                                  ["aws", "java"]],
                                 [1, 2])
                         ])
def test_solution_1125(req_skills, people, expected):
    result = solution_1125(req_skills, people)
    assert result == expected
