from dataclasses import dataclass
import textwrap
from typing import List

from gpu_container_runner.commands.gpu import get_gpu_info
from gpu_container_runner.commands.docker import get_image_infos
from gpu_container_runner.value_object.script_info import ScriptInfo


def input_user(start_time: str):
    print('GO Deepstation!!')

    print(textwrap.dedent('''
        Input your volume directory path for docker container 
        ex)
            ・ $PWD
            ・ /home/kensuke/programs/project        
    ''').strip())
    volume_path = input('\ntarget directory: ')

    print(textwrap.dedent('''
        Input your python file path relative path from volume_path
        If your python file exsit in /home/kensuke/programs/project/run/main.py
        Input `run/main.py`
        \n
    ''').strip())
    file_path = input('\npython script path: ')
    while not validate_python_path(file_path):
        print('not include python extension (.py)')
        file_path = input('python script path: ')

    gpu_infos = get_gpu_info()
    gpu_usage = [ f'- ID: {gpu_info.id} ({round(gpu_info.memory_usage * 100, 2)}%)' for gpu_info in gpu_infos]
    gpu_info_text = "\n".join(gpu_usage)
    print('Select use gpu id')
    print(textwrap.dedent(f'{gpu_info_text}'.format(gpu_info_text=gpu_info_text)).strip())
    gpu_id = input('\ngpu id: ')
    
    docker_image_infos = get_image_infos()
    print(textwrap.dedent('''
        Input docker image name
        exsit images: {}
    '''.format(docker_image_infos.keys())).strip())
    image_name = input('\nimage name: ')
    while not validate_docker_image_name(image_name, docker_image_infos.keys()):
        print('not exist image')
        image_name = input('\nimage name: ')

    print(textwrap.dedent('''
        Input docker image tag
        exsit images: {}
    '''.format(docker_image_infos[image_name])).strip())
    image_tag = input('\nimage tag: ')

    print(textwrap.dedent('''
        Input Log path
        If you don't need the file, input `n`
        ex)
            ・ ./
    '''.format(gpu_info_text=gpu_info_text)).strip())
    log_path = input('\nimage tag: ')

    return ScriptInfo(
        volume_path=volume_path,
        python_path=file_path,
        gpu_id=gpu_id,
        image_name=image_name,
        image_tag=image_tag,
        log_path=log_path + start_time + '.log'
    )


def validate_python_path(file_path: str) -> bool:
    return file_path.endswith('.py')


def validate_docker_image_name(image_name: str, images: List[str]) -> bool:
    return image_name in images