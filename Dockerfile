FROM python:3.11

WORKDIR /app

COPY --chown=1000:1000 requirements.txt .

RUN pip install \
      --no-cache \
      --root-user-action=ignore \
      --requirement requirements.txt

COPY --chown=1000:1000 . .

# Expose port if needed (MCP uses stdio, so not required)

# Run the MCP server
CMD ["python", "-m", "satellites_search_server"]