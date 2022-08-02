from dataclasses import dataclass


@dataclass(frozen=True)
class ScriptInfo:
    python_path: str

    volume_path: str

    gpu_id: str

    image_name: str

    image_tag: str

    log_path: str
