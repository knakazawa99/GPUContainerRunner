from typing import List
import subprocess

from gpu_container_runner.value_object.script_info import ScriptInfo


def run_docker_command(script_info: ScriptInfo) -> List[str]:
    
    cmd = generate_command(script_info)
    output = subprocess.check_output(cmd, shell=True)
    
    lines = output.decode().split('\n')
    lines = [ line.strip() for line in lines if line.strip() != '' ]
    
    return lines


def generate_command(script_info: ScriptInfo) -> str:
    volumes =  f'{script_info.volume_path}/:/usr/src/myapp'
    working_dir = '/usr/src/myapp'
    image = script_info.image_name
    image_tag = script_info.image_tag
    target_script = script_info.python_path

    return f'docker run -it --rm -v {volumes} -w {working_dir} {image}:{image_tag} python {target_script}'
