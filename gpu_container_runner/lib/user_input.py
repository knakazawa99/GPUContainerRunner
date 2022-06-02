from dataclasses import dataclass
import textwrap

from gpu_container_runner.commands.gpu import get_gpu_info
from gpu_container_runner.value_object.script_info import ScriptInfo


def input_user():
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
    gpu_usage = [ f'{gpu_info.id}({gpu_info.memory_usage}%)' for gpu_info in gpu_infos]
    gpu_info_text = '|'.join(gpu_usage)
    print(textwrap.dedent('''
        Select use gpu id
        {gpu_info_text}

    '''.format(gpu_info_text=gpu_info_text)).strip())
    gpu_id = input('\ngpu id: ')
    

    print(textwrap.dedent('''
        Input docker image name

    '''.format(gpu_info_text=gpu_info_text)).strip())
    image_name = input('\nimage name: ')

    print(textwrap.dedent('''
        Input docker image tag

    '''.format(gpu_info_text=gpu_info_text)).strip())
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
        log_path=log_path
    )

def validate_python_path(file_path: str) -> bool:
    return file_path.endswith('.py')