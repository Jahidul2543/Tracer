# Write your test functions in the class 'CountOddsAndEvensTests'

"""
Implemented count_odds_and_evens() function in tracer_app.CountOddAndEven.py to test
whether constructor can invoke the the function while using an instance created by the
 constructor provided in this  class
"""
# import tracer_app.CountOddAndEven


class CountOddsAndEvensTests(object):

    # DO NOT TOUCH
    def __init__(self, fn_to_test):
        self.count_odds_and_evens = fn_to_test

    def test_small_list(self):
        # tests that correct output is given when input is small list of integers
        test_input = [1, 2, 3, 4]
        expected = {'ODDS': 2, 'EVENS': 2}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
        else:
            print("No Exception")
        return expected == actual

    def test_large_list(self):
        # tests that correct output is given when input is big list of integers
        test_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        expected = {'ODDS': 8, 'EVENS': 8}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
        else:
            print("No Exception")
        return expected == actual

    def test_empty_list(self):
        # tests that correct output is given when input is empty list of integers
        test_input = []
        expected = {'ODDS': 0, 'EVENS': 0}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
        else:
            print("No Exception")

        return expected == actual

    def test_only_even_list(self):
        # tests that correct output is given when input is only even list of integers
        test_input = [2, 4, 6]
        expected = {'ODDS': 0, 'EVENS': 3}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
        else:
            print("No Exception")
        return expected == actual

    def test_only_odd_list(self):
        # tests that correct output is given when input is only odd list of integers
        test_input = [1, 3, 5]
        expected = {'ODDS': 3, 'EVENS': 0}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
        else:
            print("No Exception")
        return expected == actual

    def test_with_non_numeric_value_in_list(self):

        """
        tests that when non numeric value passed in the list instead of integer test fails
        and returns false
        """

        test_input = ['a', 2, 4, 6]
        expected = {'ODDS': 0, 'EVENS': 3}
        actual = None
        try:
            actual = self.count_odds_and_evens(test_input)
        except Exception as detail:
            print(detail)
            print("Please check test_input")

        return expected == actual


# Using below instance of this class can be used to text the function written in tracer_test.CountOddAndEven.py
# obj = CountOddsAndEvensTests(tracer_app.CountOddAndEven.count_odds_and_evens)
# now lets call all the test functions and see the result
# print('test_small_list: ' + obj.test_small_list().__str__())
# print("test_large_list: " + obj.test_large_list().__str__())
# print("test_empty_list: " + obj.test_empty_list().__str__())
# print("test_only_even_list: " + obj.test_only_even_list().__str__())
# print("test_only_odd_list: " + obj.test_only_odd_list().__str__())
# print("test_with_non_numeric_value_in_list: " + obj.test_with_non_numeric_value_in_list().__str__())
