import dataclasses
from unittest import TestCase

from gpu_container_runner.value_object.gpu_info import GPUInfo


class TestGPUInfo(TestCase):
    def test_generate_instance(self):
        gpu_info = GPUInfo(
            id='1',
            memory_usage=50.0
        )
        assert isinstance(gpu_info, GPUInfo)

    def test_insert_failed(self):
        gpu_info = GPUInfo(
            id='1',
            memory_usage=50.0
        )
        with self.assertRaises(dataclasses.FrozenInstanceError):
            gpu_info.id = '2'
