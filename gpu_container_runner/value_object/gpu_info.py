from dataclasses import dataclass


@dataclass(frozen=True)
class GPUInfo:
    id: str
    # Percent of time over the past sample period during which one or more kernels was executing on the GPU.
    memory_usage: float
