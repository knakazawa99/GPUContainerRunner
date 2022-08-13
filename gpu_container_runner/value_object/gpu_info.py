from pydantic import BaseModel, Field, confloat


class GPUInfo(BaseModel):
    class Config:
        allow_mutation = False

    id: str = Field(..., title="GPU ID or GPU IDs", examples="- 0" "- 0,1")
    memory_usage: confloat(ge=0.0, le=1.0) = Field(
        ...,
        title="Memory Usage ",
        description="Percent of time over the past sample period during which one or "
        "more kernels was executing on the GPU.",
    )
