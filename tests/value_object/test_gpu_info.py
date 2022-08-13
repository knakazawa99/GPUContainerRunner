from unittest import TestCase

from gpu_container_runner.value_object.gpu_info import GPUInfo


class TestGPUInfo(TestCase):
    def test_generate_instance(self):
        gpu_info = GPUInfo(id="1", memory_usage=0.5)
        assert isinstance(gpu_info, GPUInfo)

    def test_insert_failed(self):
        gpu_info = GPUInfo(id="1", memory_usage=0.5)
        with self.assertRaises(TypeError):
            gpu_info.id = "2"
