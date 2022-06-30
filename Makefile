SHELL := /bin/bash
.DEFAULT_GOAL := help
.PHONY: help
VENV=env
PYTHON=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip
include .env
export $(shell sed 's/=.*//' .env)


help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' \
	| column -t  -s ':' \

clean: ## : Clean up the __pycache__ folder    
	@bash -l -c 'rm -rf __pycache__ && rm -rf craiglist/__pycache__/ && rm -rf listings/__pycache__'
	@bash -l -c 'rm -rf $(VENV)'

venv: ## : Create virtual environnement
	@bash -c -l 'python -m venv $(VENV)'

setup: ## : Install dependencies
	@bash -c -l '[[ "$(VIRTUAL_ENV)" == *"$(VENV)"* ]] && pip install -r requirements.txt || echo "Please create virtual environnement"'

build: ## : Restart containers
	@bash -l -c 'docker compose build'

up: ## : Start containers
	@bash -l -c 'docker compose up -d'

down: ## : Shutdown containers
	@bash -l -c 'docker compose down'

restart: ## : Restart containers
	@bash -l -c 'docker compose restart'

app_db: ## : Login inside database container
	@bash -l -c 'docker compose exec craiglist_db sh'

app_web: ## :  Login inside web container
	@bash -l -c 'docker compose exec craiglist_web sh'

runserver: ## : Run django server
	@bash -l -c 'docker compose stop craiglist_web && python manage.py runserver'

migration: ## : Make migrations
	@bash -l -c 'python manage.py makemigrations'

migrate: ## : Apply migrations
	@bash -l -c 'python manage.py migrate'

superuser: ## : Create super user
	@bash -l -c 'python manage.py createsuperuser'

test: ## : Run test
	@bash -l -c 'python manage.py test'
	
lint: ## : Lint 
	@bash -l -c 'flake8'

ci: ## : Run CI locally with act
	@bash -l -c 'act --secret-file .env'

ssh: ## : Connect to droplet ssh
	@bash -l -c 'doctl compute ssh django-craiglist'

droplet-status: ## : Get droplet status
	@bash -l -c 'doctl compute droplet get django-craiglist --output json | jq '.[0].status''

db-status: ## : Get database status
	@bash -l -c "curl -H 'Content-Type: application/json' -H 'Authorization: Bearer '$(DIGITAL_OCEAN_ACCESS_TOKEN)'' "https://api.digitalocean.com/v2/databases?name=django-docker-db" | jq '.databases[0].status'"

account: ## : Get account digital ocean
	@bash -l -c 'doctl account get'