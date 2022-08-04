from typing import List
from unittest import TestCase

from gpu_container_runner.commands.gpu import generate_gpu_info, get_gpu_info
from gpu_container_runner.value_object.gpu_info import GPUInfo


def test_get_gpu_info(mocker):
    mock_value = b"0, 8, 16\n1, 4, 16\n"
    mocker.patch("subprocess.check_output", return_value=mock_value)
    gpu_infos = get_gpu_info()
    print(gpu_infos, flush=True)
    expect_gpu_infos = [GPUInfo(id="0", memory_usage=0.5), GPUInfo(id="1", memory_usage=0.25)]
    for expect_gpu_info, gpu_info in zip(expect_gpu_infos, gpu_infos):
        assert isinstance(gpu_info, GPUInfo)
        assert gpu_info.id == expect_gpu_info.id
        assert gpu_info.memory_usage == expect_gpu_info.memory_usage


def test_get_gpu_info_no_nvidia_smi():
    gpu_infos = get_gpu_info()
    for gpu_info in gpu_infos:
        assert isinstance(gpu_info, GPUInfo)


class TestGpu(TestCase):
    def test_generate_gpu_info(self):
        test_lines = ["0, 2, 10", "1, 2, 20"]
        gpu_infos: List[GPUInfo] = generate_gpu_info(test_lines)
        for gpu_info, test_line in zip(gpu_infos, test_lines):
            test = test_line.split(", ")
            self.assertEqual(gpu_info.id, test[0])
            self.assertEqual(gpu_info.memory_usage, float(test[1]) / float(test[2]))
