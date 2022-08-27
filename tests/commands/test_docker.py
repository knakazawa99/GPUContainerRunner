import uuid
from unittest import TestCase

from gpu_container_runner.commands.docker import (
    generate_command,
    get_image_infos,
    run_docker_command,
)
from gpu_container_runner.value_object.script_info import ScriptInfo


def test_run_docker_command(mocker):
    cmd_mock_value = "docker images"
    subprocess_mock_value = b"test clear \n " b"test done\n"
    mocker.patch("gpu_container_runner.commands.docker.generate_command", return_value=cmd_mock_value)
    mocker.patch("subprocess.check_output", return_value=subprocess_mock_value)
    job_id = uuid.uuid4()
    result = run_docker_command(
        ScriptInfo(
            gpu_id="1", python_path="hoge.py", volume_path="./", image_name="test", image_tag="1.0", log_path="./"
        ),
        job_id,
    )
    expect_value = ["test clear", "test done"]
    assert result == expect_value


def test_get_image_infos(mocker):
    mock_value = (
        b"REPOSITORY TAG IMAGE ID CREATED  SIZE\n "
        b"test/image  1.0 a86ef3993d32  16 hours ago 10.6GB\n"
        b"test/image  2.0 a86bf3993d32  16 hours ago 10.6GB\n"
        b"test/image2 1.0 a86bf3993d32  16 hours ago 10.6GB\n"
    )

    mocker.patch("subprocess.check_output", return_value=mock_value)
    image_infos = get_image_infos()
    expect_image_infos = {"test/image": ["1.0", "2.0"], "test/image2": ["1.0"]}
    for image_info_key, image_info_tags in image_infos.items():
        assert image_infos[image_info_key] == expect_image_infos[image_info_key]


class TestDocker(TestCase):
    def test_generate_command(self):
        script_info = ScriptInfo(
            volume_path="volume_path",
            python_path="python_path/test.py",
            gpu_id="1",
            image_name="python",
            image_tag="3",
            log_path="./2022.log",
        )
        job_id = uuid.uuid4()
        command = generate_command(script_info, job_id)
        self.assertEqual(
            command,
            f"nohup docker run -i --rm --gpus 1 -v volume_path/:/var/app -w /var/app --name {job_id}"
            "python:3 python python_path/test.py > ./2022.log &",
        )
