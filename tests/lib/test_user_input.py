import io
import time
from unittest import TestCase

from gpu_container_runner.lib.user_input import (
    get_python_files,
    input_user,
    validate_docker_image_name,
    validate_python_path
)
from gpu_container_runner.value_object.script_info import ScriptInfo


def mock_for_input_user(monkeypatch, mocker):
    mock_gpu_info = b"0, 8, 16\n1, 4, 16\n"
    mocker.patch("gpu_container_runner.commands.gpu.run_nvidia_smi", return_value=mock_gpu_info)

    mock_image_infos = (
        b"REPOSITORY TAG IMAGE ID CREATED  SIZE\n "
        b"test/image  1.0 a86ef3993d32  16 hours ago 10.6GB\n"
        b"test/image  2.0 a86bf3993d32  16 hours ago 10.6GB\n"
        b"test/image2 1.0 a86bf3993d32  16 hours ago 10.6GB\n"
    )
    mocker.patch("subprocess.check_output", return_value=mock_image_infos)


def test_input_user(monkeypatch, mocker):
    mock_for_input_user(monkeypatch, mocker)
    # 標準入力をモック
    monkeypatch.setattr("sys.stdin", io.StringIO("$PWD\ntest.py\n1\ntest/image\n1.0\n./\n"))
    start = time.strftime("%Y%m%d%H%M")
    result = input_user(start)
    expect = ScriptInfo(
        volume_path="$PWD",
        python_path="test.py",
        gpu_id="1",
        image_name="test/image",
        image_tag="1.0",
        log_path=f"./{start}.log",
    )
    assert result == expect


def test_input_user_python(monkeypatch, mocker):
    """Input Python File 2 times"""
    mock_for_input_user(monkeypatch, mocker)
    # 標準入力をモック
    monkeypatch.setattr("sys.stdin", io.StringIO("$PWD\ntest\ntest.py\n1\ntest\ntest/image\n1.0\n./\n"))
    start = time.strftime("%Y%m%d%H%M")
    result = input_user(start)
    expect = ScriptInfo(
        volume_path="$PWD",
        python_path="test.py",
        gpu_id="1",
        image_name="test/image",
        image_tag="1.0",
        log_path=f"./{start}.log",
    )
    assert result == expect


def test_input_user_docker(monkeypatch, mocker):
    """Input Docker Image Name 2 times"""
    mock_for_input_user(monkeypatch, mocker)
    monkeypatch.setattr("sys.stdin", io.StringIO("$PWD\ntest.py\n1\ntest\ntest/image\n1.0\n./\n"))
    start = time.strftime("%Y%m%d%H%M")
    result = input_user(start)
    expect = ScriptInfo(
        volume_path="$PWD",
        python_path="test.py",
        gpu_id="1",
        image_name="test/image",
        image_tag="1.0",
        log_path=f"./{start}.log",
    )
    assert result == expect


def test_get_python_files_pwd():
    python_files = get_python_files("$PWD")
    for python_file in python_files:
        assert python_file.endswith(".py")


def test_get_python_files():
    python_files = get_python_files("./")
    for python_file in python_files:
        assert python_file.endswith(".py")


def test_validate_docker_image_name():
    result = validate_docker_image_name("test", ["test", "docker"])
    assert result


def test_validate_docker_image_name_false():
    result = validate_docker_image_name("test", ["docker", "continuous"])
    assert not result


class TestUserInput(TestCase):
    def test_validate_python_path_no_option(self):
        target_path = "test.py"
        validation_result = validate_python_path(target_path)
        self.assertEqual(True, validation_result)

    def test_validate_python_path_option(self):
        target_path = "/mmdetection/tools/test.py -o ./"
        validation_result = validate_python_path(target_path)
        self.assertEqual(True, validation_result)
