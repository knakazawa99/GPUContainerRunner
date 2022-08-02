import subprocess
from typing import List, Union

from gpu_container_runner.lib.logger import Logger
from gpu_container_runner.value_object.gpu_info import GPUInfo

GPU_QUERY = (
    "index",
    "memory.used",
    "memory.total",
)


def get_gpu_info() -> List[GPUInfo]:
    output = run_nvidia_smi()

    if not output:
        return [GPUInfo(id="-1", memory_usage="0")]

    lines = output.decode().split("\n")
    lines = [line.strip() for line in lines if line.strip() != ""]

    return generate_gpu_info(lines)


def run_nvidia_smi() -> Union[str, bool]:
    query_gpu = ",".join(GPU_QUERY)
    command = f"nvidia-smi --query-gpu={query_gpu} --format=csv,noheader,nounits"
    try:
        output = subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        Logger.warning(e)
        return False
    return output


def generate_gpu_info(lines: List[str]) -> List[GPUInfo]:

    gpu_infos: List[GPUInfo] = []
    for line in lines:
        gpu_info = {k: v for k, v in zip(GPU_QUERY, line.split(", "))}
        gpu_infos.append(
            GPUInfo(
                id=gpu_info["index"],
                memory_usage=float(gpu_info["memory.used"]) / float(gpu_info["memory.total"]),
            )
        )

    return gpu_infos
