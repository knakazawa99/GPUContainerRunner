from operator import mod
from pprint import pprint
import time

from gpu_container_runner.commands.docker import run_docker_command
from gpu_container_runner.lib.user_input import input_user
from gpu_container_runner.lib.notify import notify_to_slack


def main():
    script_info = input_user()
    start = time.strftime('%Y%m%d%H%M')
    result = run_docker_command(script_info)
    end = time.strftime('%Y%m%d%H%M')
    
    if script_info.log_path != 'n':
        log_file_path = script_info.log_path + f'{start}-{end}.log'
        with open(log_file_path, mode='x') as f:
            f.write('\n'.join(result))
    notify_to_slack('終了しました。')


if __name__ == '__main__':
    main()