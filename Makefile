
.PHONY: format
format:
	poetry run isort -rc -sl .
	poetry run autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables .
	poetry run black .
	poetry run isort -rc -m 3 .

.PHONY: setup
setup:
	poetry install
	git config --local commit.template .github/.commit_template

.PGONY: test
test:
	poetry run pytest -v -p no:warning --cov=gpu_container_runner