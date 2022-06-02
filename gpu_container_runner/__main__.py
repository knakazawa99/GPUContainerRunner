from pprint import pprint

from gpu_container_runner.commands.docker import run_docker_command
from gpu_container_runner.user_input import input_user


def main():
    script_info = input_user()
    result = run_docker_command(script_info)
    print(result)


if __name__ == '__main__':
    main()