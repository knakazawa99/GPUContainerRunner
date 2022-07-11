from setuptools import setup

setup(
    name = 'run_gpu',
    version = '1.0.2',
    install_requires = ['slackweb'],
    entry_points = {
        "console_scripts": ['run_gpu = gpu_container_runner.__main__:main'],
    }
)
