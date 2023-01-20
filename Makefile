gen:
	rm -r app/src/openapi
	rm -r app/src/models
	openapi-generator generate -i docs/api/* -g python-aiohttp -o app -c docs/openapi_config.yaml --skip-overwrite

run-server:
	docker-compose build
	docker-compose up -d

stop-server:
	docker-compose down

