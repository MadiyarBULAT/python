# Test results:
# test_analyse_twice ... ok
# test_result_has_required_keys ... ok
# test_result_is_not_empty ... ok
# test_total_students ... ok
#
# Ran 4 tests
# OK

import unittest
from analytics.analyser import GpaAnalyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"GPA": "3.8"},
            {"GPA": "2.5"},
            {"GPA": "3.9"},
            {"GPA": "1.8"},
            {"GPA": "3.5"},
        ]

    def test_result_is_not_empty(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()

        self.assertIn("average_gpa", analyser.result)
        self.assertIn("max_gpa", analyser.result)
        self.assertIn("min_gpa", analyser.result)
        self.assertIn("high_performers", analyser.result)

    def test_analyse_twice(self):
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()

        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == "__main__":
    unittest.main()
