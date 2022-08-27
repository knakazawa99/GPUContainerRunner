.PHONY: linter
linter:
	poetry run flake8 gpu_container_runner tests --max-line-length 120 --ignore=W291

.PHONY: format
format:
	poetry run isort -rc -sl .
	poetry run autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables .
	poetry run black --line-length 120 .
	poetry run isort -rc -m 3 .

.PHONY: setup
setup:
	pre-commit install
	poetry install
	git config --local commit.template .github/.commit_template

.PHONY: test
test:
	poetry run pytest -v -p no:warning --cov=gpu_container_runner

.PHONY: test-ci
test-ci:
	poetry run pytest -v --cov=gpu_container_runner --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt
