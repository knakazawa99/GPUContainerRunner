import time

from gpu_container_runner.commands.docker import run_docker_command
from gpu_container_runner.lib.notify import notify_to_slack
from gpu_container_runner.lib.user_input import input_user


def main():
    start = time.strftime("%Y%m%d%H%M")
    script_info = input_user(start)
    run_docker_command(script_info)

    notify_to_slack("Jobを登録しました。")


if __name__ == "__main__":
    main()
