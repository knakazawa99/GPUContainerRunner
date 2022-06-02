from typing import List
from unittest import TestCase

from gpu_container_runner.commands.gpu import generate_gpu_info
from gpu_container_runner.value_object.gpu_info import GPUInfo


class TestGpu(TestCase):
    def test_generate_gpu_info(self):
        test_lines = [
            '0, 2, 10',
            '1, 2, 20'
        ]
        gpu_infos: List[GPUInfo] = generate_gpu_info(test_lines)
        for gpu_info, test_line in zip(gpu_infos, test_lines):
            test = test_line.split(', ')
            self.assertEqual(gpu_info.id, test[0])
            self.assertEqual(gpu_info.memory_usage, float(test[1]) / float(test[2]))
