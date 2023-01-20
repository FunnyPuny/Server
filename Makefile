gen:
	rm -f app/openapi.yaml
	rm -rf app/src/web/models
	openapi-generator generate -i docs/api/* -g python-fastapi -o app -c docs/openapi_config.yaml --skip-overwrite

run-server:
	docker-compose build
	docker-compose up -d

stop-server:
	docker-compose down

