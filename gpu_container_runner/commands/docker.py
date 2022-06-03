import subprocess
from typing import Dict, List

from gpu_container_runner.value_object.script_info import ScriptInfo


def run_docker_command(script_info: ScriptInfo) -> List[str]:
    
    cmd = generate_command(script_info)
    output = subprocess.check_output(cmd, shell=True)
    
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    
    return lines


def get_image_infos() -> Dict[str, List[str]]:
    cmd = 'docker images'
    output = subprocess.check_output(cmd, shell=True)

    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    lines.pop(0)

    docker_image_info = dict()
    for line in lines:
        text = " ".join(line.split()).split(' ')
        image_name, image_tag = text[0], text[1]
        if image_name in docker_image_info.keys():
            docker_image_info[image_name].append(image_tag)
        else:
            docker_image_info[image_name] = [image_tag]

    return docker_image_info


def generate_command(script_info: ScriptInfo) -> str:
    volumes =  f'{script_info.volume_path}/:/usr/src/myapp'
    working_dir = '/usr/src/myapp'
    image = script_info.image_name
    image_tag = script_info.image_tag
    target_script = script_info.python_path
    gpu_id = script_info.gpu_id

    return f'docker run -it --rm --gpus {gpu_id} -v {volumes} -w {working_dir} {image}:{image_tag} python {target_script}'
