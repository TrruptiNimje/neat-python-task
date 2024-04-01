import unittest
from reportinput.report_params import gen_params


class test_report_params(unittest.TestCase):
    def test_valid_inputs_with_common_elements(self):
        result = gen_params("Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox", "Frog  apple    fox cat fish fish")
        self.assertEqual(result, ['apple', 'fish', 'fox', 'frog'])

    def test_valid_inputs_with_no_common_elements(self):
        result = gen_params("Dog,cat,fish", "apple,banana,orange")
        self.assertEqual(result, [])

    def test_partial_matches_not_included(self):
        result = gen_params("Dog,apple,  Monkey,frog", "pineapple, Frog")
        expected = ['frog']
        self.assertEqual(result, expected)

    def test_empty_strings_as_inputs(self):
        with self.assertRaises(ValueError) as context:
            gen_params("", "")
        self.assertEqual(str(context.exception), "Input strings cannot be empty or None.")

    def test_null_inputs(self):
        with self.assertRaises(ValueError) as context:
            gen_params(None, None)
        self.assertEqual(str(context.exception), "Input strings cannot be empty or None.")

    def test_inputs_with_different_delimiters(self):
        result = gen_params( "Frog  apple    fox cat fish fish", "Dog,caTfish,Frog,FIsh,apple  ,    Monkey,appLe,fox")
        self.assertEqual(result, ['apple', 'fish', 'fox', 'frog'])

    def test_exception_handling_empty_input(self):
        with self.assertRaises(ValueError) as context:
            gen_params("", "Frog  apple    fox cat fish fish")
        self.assertEqual(str(context.exception), "Input strings cannot be empty or None.")

    def test_exception_handling_null_input(self):
        with self.assertRaises(ValueError) as context:
            gen_params(None, "Frog  apple    fox cat fish fish")
        self.assertEqual(str(context.exception), "Input strings cannot be empty or None.")

    def test_non_string_inputs(self):
        with self.assertRaises(TypeError) as context:
            gen_params(123, 345)
        self.assertEqual(str(context.exception), "Inputs must be strings.")

    def test_digits_as_strings(self):
        result = gen_params("123, 456, 789", "456 789 101112")
        self.assertEqual(result, ['456', '789'])

    def test_special_characters_as_inputs(self):
        result = gen_params("!@#,$%^&*()", "#$%^&*(),@!^ !@#")
        self.assertEqual(result, ['!@#'])



