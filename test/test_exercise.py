# DO NOT MODIFY THE CODE IN THIS FILE
import pytest
from testbook import testbook
import random
import os

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

# order: frequency, amplitude, phase_shift, sample_rate, n_seconds
# input_1 = [1, 1, 0, 44100, 1]
# output_1 = ([0.0,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9], [0.0,  0.5877852522924731,  0.9510565162951535,  0.9510565162951535,  0.5877852522924732,  1.2246467991473532e-16,  -0.5877852522924734,  -0.9510565162951535,  -0.9510565162951536,  -0.5877852522924734])

input_1 = [1, 1, 1, 1, 1]
output_1 = ([3, 4], [5, 6])

@pytest.mark.parametrize("test_input,expected", [(input_1, output_1)]) # , ([3.5, 7.13], 10.63), ([-13.23, 6], -7.23)])
def test_exercise_1(tb, test_input, expected):
    student_work = tb.ref("get_sine_data")
    assert student_work(frequency=test_input[0], amplitude=test_input[1], phase_shift=test_input[2], sample_rate=test_input[3], n_seconds=test_input[4]) == pytest.approx(expected, 0.01)
