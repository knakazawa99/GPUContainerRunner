import uuid

from gpu_container_runner.commands.docker import run_docker_command
from gpu_container_runner.lib.notify import notify_to_slack
from gpu_container_runner.lib.user_input import input_user


def main():
    job_id = uuid.uuid4()
    script_info = input_user(job_id)
    run_docker_command(script_info, job_id)

    notification_message = f"Job has registered。job_id: {job_id}" f"If you wanna stop job, run `$ docker kill {job_id}`"
    notify_to_slack(notification_message)


if __name__ == "__main__":
    main()
