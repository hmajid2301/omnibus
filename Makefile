.DEFAULT_GOAL := help


.PHONY: help
help: ## Generates a help README
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## Start the application "stack" using Docker
	@docker-compose up --build

.PHONY: start-deps
start-deps: ## Start all the Docker containers that this app depends on directly
	@docker-compose pull
	@docker-compose up --build -d database database-gui

.PHONY: unit_tests_docker
unit_tests_docker: ## Run unit tests in Docker container
	@docker-compose run app make unit_tests

.PHONY: integration_tests_docker
integration_tests_docker: ## Run integration tests in Docker container
	@docker-compose run app make integration_tests

.PHONY: coverage_docker
coverage_docker: ## Run coverage tests in Docker container
	@docker-compose run app make coverage

.PHONY: unit_tests
unit_tests: ## Run all the unit tests
	@poetry run pytest -v tests/unit

.PHONY: integration_tests
integration_tests: ## Run all the integration tests
	@poetry run pytest -v tests/integration

.PHONY: coverage
coverage: ## Run the integration tests with code coverage report generated
	@poetry run pytest -v --junitxml=report.xml --cov=app/ tests/integration
	@poetry run coverage xml

.PHONY: install-hooks
install-hooks: ## Install pre commit hooks
	@poetry pre-commit install

.PHONY: lint
lint: ## Run the lint steps (pre-commit hook)
	@poetry run pre-commit run --all-files

.PHONY: clean
clean: ### Clean all temporary files
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' | xargs rm -rf
	@find . -type d -name '*.ropeproject' | xargs rm -rf
	@rm -rf build/
	@rm -rf dist/
	@rm -f src/*.egg
	@rm -f src/*.eggs
	@rm -rf src/*.egg-info/
	@rm -f MANIFEST
	@rm -rf docs/build/
	@rm -rf htmlcov/
	@rm -f .coverage
	@rm -f .coverage.*
	@rm -rf .cache/
	@rm -f coverage.xml
	@rm -f *.cover
	@rm -rf .pytest_cache/