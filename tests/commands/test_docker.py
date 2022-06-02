from typing import List
from unittest import TestCase

from gpu_container_runner.commands.docker import generate_command
from gpu_container_runner.value_object.script_info import ScriptInfo


class TestDocker(TestCase):
    def test_generate_command(self):
        script_info = ScriptInfo(
            volume_path='volume_path',
            python_path='python_path/test.py',
            gpu_id='1',
            image_name='python',
            image_tag='3',
            log_path='./'
        )
        command = generate_command(script_info)
        self.assertEqual(
            command,
            'docker run -it --rm -v volume_path/:/usr/src/myapp -w /usr/src/myapp python:3 python python_path/test.py'
        )
