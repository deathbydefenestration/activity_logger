.PHONY: test

test: .venv3/bin/pytest
	.venv3/bin/pytest tests -v --capture=no --cov src --cov-fail-under 100  --cov-report term-missing

.venv3/bin/pip:
	python3 -m venv --prompt=run_logger .venv3

.venv3/bin/pytest: .venv3/bin/pip
	.venv3/bin/pip install pytest-cov
