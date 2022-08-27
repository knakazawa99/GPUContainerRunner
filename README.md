[![CI](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml/badge.svg)](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/KensukeNakazawa/27de0c03b88fd9d4bc03c3c28f628ebc/raw/pytest-coverage-comment.json)](https://github.com/KensukeNakazawa/GPUContainerRunner/actions/workflows/ci.yaml)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PythonVersion](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)

## :bulb: Overview
研究室の計算機サーバーで Dockerコンテナ上での GPUを用いた Pythonプログラムを実行しやすくするためのCUIツール

<div>
  <video autoplay src="https://user-images.githubusercontent.com/62752589/187019201-67c98144-bff6-4ce9-961c-2a0397bea3f7.mp4" muted="false">
  </video>
</div>

## :label: Requirements
- [x] [Python](https://www.python.org/)
- [x] [Poetry](https://github.com/python-poetry/poetry)
- [x] [Docker](https://www.docker.com/)
- [x] [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

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
