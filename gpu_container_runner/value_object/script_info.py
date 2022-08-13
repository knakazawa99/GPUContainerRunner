from pydantic import BaseModel, Field


class ScriptInfo(BaseModel):
    class Config:
        allow_mutation = False

    volume_path: str = Field(..., title="Target Mount Path", examples="$PWD" "/var/app")

    python_path: str = Field(..., title="Target Python Path", examples="src/main.py")

    gpu_id: str = Field(
        ...,
        title="Using GPU ID or GPU IDs",
        description="Link to gpu_container_runner.value_object.gpu_info.GPUInfo.id",
        examples="0" "0,1",
    )

    image_name: str = Field(
        ...,
        title="Using Docker Image",
    )

    image_tag: str = Field(..., title="Using Docker Tag")

    log_path: str = Field(..., title="Log Path")
