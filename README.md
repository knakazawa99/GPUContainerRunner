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
