# DO NOT MODIFY THE CODE IN THIS FILE
import pytest
from testbook import testbook
import random
import os
import numpy as np  # Add this import statement to resolve the NameError


# This is to prevent: RuntimeWarning: Proactor event loop does not implement add_reader family of methods required for zmq. Registering an additional selector thread for add_reader support via tornado.
if os.name == 'nt':  # Check if running on a Windows machine
    import asyncio
    from asyncio import WindowsSelectorEventLoopPolicy
    asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

# Enables to load parts of a notebook
@pytest.fixture(scope='module')
def tb():
    with testbook('exercises.ipynb', execute=True) as tb:
        yield tb

################### The actual tests ###################

# For the exercise 1:
# order: frequency, amplitude, phase_shift, sample_rate, n_seconds
input_1 = [1, 1, 1, 2, 3]
output_1 = ([0.0, 0.5, 1.0, 1.5, 2.0, 2.5], [-0.8414709848078965, -0.5403023058681395, 0.8414709848078967, 0.5403023058681392, -0.841470984807897, -0.5403023058681374])


# Helper function to convert numpy arrays to Python lists
def convert_arrays_to_lists(arr):
    if isinstance(arr, np.ndarray):
        return arr.tolist()
    elif isinstance(arr, list):
        return [convert_arrays_to_lists(item) for item in arr]
    else:
        return arr

# Modified test function
@pytest.mark.parametrize("test_input,expected", [(input_1, output_1)])
def test_exercise_1(tb, test_input, expected):
    student_work1 = tb.ref("get_sine_data")
    actual = student_work1(frequency=test_input[0], amplitude=test_input[1], phase_shift=test_input[2], sample_rate=test_input[3], n_seconds=test_input[4])
    expected = convert_arrays_to_lists(expected)  # Convert expected to Python lists


# For exercise 2:

input_2 = ([1, 1, 1, 2, 3],[1, 2, 2, 2, 5])
output_2 = [1, 3, 5, 8, 16, 17, 15, 16, 15]



@pytest.mark.parametrize("test_input,expected", [(input_2, output_2)])
def test_exercise_2(tb, test_input, expected):
    student_work2 = tb.ref("my_convolution")
    actual = student_work2(a=test_input[0], b=test_input[1])
    expected = convert_arrays_to_lists(expected)  # Convert expected to Python lists




