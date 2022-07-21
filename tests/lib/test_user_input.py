from typing import List
from unittest import TestCase

from gpu_container_runner.lib.user_input import validate_python_path

class TestUserInput(TestCase):
    def test_validate_python_path_no_option(self):
        target_path = 'test.py'
        validation_result = validate_python_path(target_path)
        self.assertEqual(True, validation_result)

    def test_validate_python_path_option(self):
        target_path = '/mmdetection/tools/test.py -o ./'
        validation_result = validate_python_path(target_path)
        self.assertEqual(True, validation_result)
