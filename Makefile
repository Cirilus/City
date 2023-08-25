up kubernetes prod:
	helm install backend-prod ./.chart

up kubernetes dev:
	helm install backend-dev ./.chart

validate helm:
	helm template ./.chart