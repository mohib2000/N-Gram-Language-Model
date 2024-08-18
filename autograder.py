"""
DO NOT CHANGE THE CODE BELOW
"""
import numpy as np
import copy

def create_tests_functions(func, *args):
    def new_test(self):
        func_output = func(*copy.deepcopy(args[0])) if isinstance(args[0], tuple) else func(copy.deepcopy(args[0]))
        print()
        if isinstance(args[1], np.ndarray):  # check for numpy arrays
            self.assertIsInstance(func_output, np.ndarray, f"Expected {args[1]} got {func_output}.")
            self.assertEqual(args[1].shape, func_output.shape, f"Expected {args[1]} got {func_output}.")
            equal = np.isclose(args[1], func_output)
            self.assertTrue(equal.all(), f"Expected {args[1]} got {func_output}.")
        elif isinstance(args[1], dict):  # check for dicts
            func_output = dict(func_output)
            if isinstance(next(iter(func_output.values())), dict):
                func_output = {k: {k2: v2 for k2, v2 in v.items()} for k, v in func_output.items()}
            self.assertDictEqual(args[1], func_output, f"Expected {args[1]} got {func_output}.")
        else:
            self.assertEqual(args[1], func_output, f"Expected {args[1]} got {func_output}.")
    return new_test

def create_tests(test_class, func, input_lst, name=None):
    name = name if name is not None else func.__name__
    for i, args in enumerate(input_lst):
        setattr(test_class, f"test_{name}_{i + 1}", create_tests_functions(func, *args))

