k8s up:
	helm install backend-dev ./.chart

validate helm:
	helm template ./.chart