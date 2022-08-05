[![CI](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml/badge.svg)](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/KensukeNakazawa/27de0c03b88fd9d4bc03c3c28f628ebc/raw/pytest-coverage-comment.json)](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PythonVersion](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)


## :bulb: Overview
研究室の計算機サーバーで Dockerコンテナ上での Pythonプログラムを実行しやすくする

## :white_check_mark: Setup

:rocket: `install`
> poetry build  
> sudo pip install -e .

:fire: `uninstall`
> sudo python setup.py develop -u  

## :hammer: Develop

> make setup

:technologist: `run cui`
> poetry run python gpu_container_runner 

:test_tube: `run test`
> make test
