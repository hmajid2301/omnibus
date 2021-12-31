.DEFAULT_GOAL := help


.PHONY: help
help: ## Generates a help README
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install-hooks: ## Install pre commit hooks
	@poetry run pre-commit install

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