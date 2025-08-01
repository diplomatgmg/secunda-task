-include .env

help:
	@awk 'BEGIN {FS = ":.*#"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?#/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^#@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

up: ## compose up
	@docker compose up -d

down: ## compose down
	@docker compose down

stop: ## compose stop
	@docker compose  stop

venv: # create/update venv
	@uv sync --frozen --all-packages --all-groups --all-extras

lint: # run linters and formatters
	@uv run ruff check .
	@uv run isort . --check-only
	@uv run ruff format --check .
	@uv run mypy .

lint-fix: # run linters and formatters with fix
	@uv run ruff check .
	@uv run isort .
	@uv run ruff format .
	@uv run mypy .

migrate: # apply migrations
	@uv run alembic upgrade head

mm: # create migration
	@if [ -z "$(m)" ]; then \
		echo 'Usage: make mm m="migration message"'; \
		exit 1; \
	fi;
	@uv run alembic revision --autogenerate -m "$(m)"

downgrade: # downgrade migrations
	@if [ -z "$(r)" ]; then \
		echo "Usage: make downgrade r=<revision>"; \
		exit 1; \
	fi;
	@uv run alembic downgrade $(r)
