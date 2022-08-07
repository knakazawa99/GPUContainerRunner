import glob
import os
import readline
import textwrap
from typing import List

from gpu_container_runner.commands.docker import get_image_infos
from gpu_container_runner.commands.gpu import get_gpu_info
from gpu_container_runner.lib.completer import Completer
from gpu_container_runner.lib.logger import Logger
from gpu_container_runner.value_object.script_info import ScriptInfo


def input_user(start_time: str):
    readline.parse_and_bind("tab: complete")
    Logger.info("GO Deepstation!!\n")

    print(
        textwrap.dedent(
            """
        Input the volume directory path to mount with the docker container 
        Examples:
            ・ $PWD (current directory)
            ・ /home/kensuke/programs/project        
    """
        ).strip()
    )
    volume_path = input("\ntarget directory path: ")
    print()

    python_files = get_python_files(volume_path)
    completer = Completer(python_files)
    readline.set_completer(completer.complete)

    print(
        textwrap.dedent(
            """
        Input the python file path (relative path from volume path)
        If the absolute python file path is /home/kensuke/programs/project/run/main.py
        & the volume path is /home/kensuke/programs/project
        Input will be 'run/main.py'
    """
        ).strip()
    )
    file_path = input("\npython script path: ")
    while not validate_python_path(file_path):
        Logger.warning("Invalid input! Python extension (.py) not included or incorrect path")
        file_path = input("python script path: ")
        print()

    gpu_infos = get_gpu_info()
    gpu_usage = [f"- ID: {gpu_info.id} ({round(gpu_info.memory_usage * 100, 2)}%)" for gpu_info in gpu_infos]
    gpu_info_text = "\n".join(gpu_usage)
    print("\nSelect the GPU")
    print(textwrap.dedent(f"{gpu_info_text}".format(gpu_info_text=gpu_info_text)).strip())
    gpu_id = input("\nGPU ID: ")

    docker_image_infos = get_image_infos()
    docker_images = list(docker_image_infos.keys())
    completer = Completer(docker_images)
    readline.set_completer(completer.complete)

    print(
        textwrap.dedent(
            """
        Select the docker image
        available images: {}
    """.format(
                docker_images
            )
        ).strip()
    )
    image_name = input("\nimage name: ")
    while not validate_docker_image_name(image_name, docker_image_infos.keys()):
        Logger.warning("no such image")
        image_name = input("\nimage name: ")

    docker_image_infos = get_image_infos()
    docker_tags = docker_image_infos[image_name]
    completer = Completer(docker_tags)
    readline.set_completer(completer.complete)

    print(
        textwrap.dedent(
            """
        Select the docker image tag
        available tags: {}
    """.format(
                docker_tags
            )
        ).strip()
    )
    image_tag = input("\nimage tag: ")

    print(
        textwrap.dedent(
            """
        Specify the path to save the log file
        If you don't need the file, input 'n'
        Examples)
            ・ ./
    """
        ).strip()
    )
    log_path = input("\nlog file path: ")

    return ScriptInfo(
        volume_path=volume_path,
        python_path=file_path,
        gpu_id=gpu_id,
        image_name=image_name,
        image_tag=image_tag,
        log_path=log_path + start_time + ".log",
    )


def get_python_files(volume_path: str) -> List[str]:
    target_path = os.getcwd() if volume_path == "$PWD" else volume_path
    if target_path[-1] == os.sep:
        target_path = target_path[:-1]

    python_files = glob.glob(f"{target_path}/**/*.py", recursive=True)
    python_files = [python_file.replace(target_path + os.sep, "") for python_file in python_files]

    return python_files


def validate_python_path(file_path: str) -> bool:
    python_path = file_path.split(" ")[0]
    return python_path.endswith(".py")


def validate_docker_image_name(image_name: str, images: List[str]) -> bool:
    return image_name in images
