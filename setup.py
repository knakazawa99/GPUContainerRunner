from setuptools import setup

setup(
    name = 'run_gpu',
    version = '0.0.1',
    install_requires = ['slackweb'],
    entry_points = {
        "console_scripts": ['run_gpu = gpu_container_runner.__main__:main'],
    }
)
