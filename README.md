# Quick start

For start server use:
```
docker-compose up -d
```

If you want to stop server use:

```
docker compose down
```

For rebuild docker images:

```
docker-compose build
```

# Develop

## Instaling dependencies

1) [Install openapi-generator](https://github.com/OpenAPITools/openapi-generator#1---installation)

## Generate new API method

1) you should modify `docs/api` files
2) run `make gen` for generate template for your new method

