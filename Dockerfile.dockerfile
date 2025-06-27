# See https://docs.docker.com/engine/reference/builder/ to learn how to customize your container

# This stage is used when running from VS in fast mode (Default for Debug configuration)  
FROM python:3.11-slim as base
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

# This stage is used to build the service project
FROM python:3.11-slim as build
WORKDIR /src

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# This stage is used in production or when running from VS in regular mode
FROM base as final
WORKDIR /app

# Copy installed packages from build stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
COPY --from=build /src .

ENTRYPOINT ["python", "main.py"]