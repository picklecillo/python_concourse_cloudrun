# Base Stage
FROM python:3.6 as base

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install .

# Lint & test stage
FROM base AS test

RUN pip install -r dev_requirements.txt
RUN flake8

RUN echo 'run tests here!'

# Build stage
FROM python:3.6-alpine

WORKDIR /app
COPY --from=base /app /app
COPY --from=base /usr/local/lib/python3.6/site-packages/ /usr/local/lib/python3.6/site-packages/

RUN echo 'build stage!'

# Ports
EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app/routes.py"]
