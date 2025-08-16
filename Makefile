build:
	docker build -t wojtek9502/satellites_passes_mcp .

build_no_cache:
	docker build --no-cache -t wojtek9502/satellites_passes_mcp .

push:
	docker push wojtek9502/satellites_passes_mcp
