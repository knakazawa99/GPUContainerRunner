## :bulb: Overview
研究室の計算機サーバーで Dockerコンテナ上での Pythonプログラムを実行しやすくする

## :white_check_mark: Setup

:rocket: install
> sudo python setup.py develop  
> sudo pip install -e .

:fire: uninstall
> sudo python setup.py develop -u  

## :hammer: Develop

:technologist: run cui
> pyton -m gpu_container_runner

:test_tube: run test
> python -m tests
