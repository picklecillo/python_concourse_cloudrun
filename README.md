# HELLO WORLD

## Local setup

### `pyenv` + `virtualenv`

```bash
brew update
brew install pyenv pyenv-virtualenv

pyenv install 3.6
pyenv global 3.6
python -V
```

#### Profile

```bash
...
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi

if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

#Virtualenv
VIRTUALENVWRAPPER_PYTHON=$HOME/.pyenv/versions/3.6/bin/python

#export PIP_REQUIRE_VIRTUALENV=true
#gpip(){
#  PIP_REQUIRE_VIRTUALENV="" pip "$@"
#}

export WORKON_HOME=$HOME/.virtualenvs
pyenv virtualenvwrapper_lazy
...
```

### Env vars

```bash
./scripts.sh load_env_vars
```

### Serve locally

```bash
./scripts.sh init_workspace local
./scripts.sh run_local
```

## Tests

```bash
./scripts.sh all_tests
```

## Deploy to cloud run

1. Setup gcp project
2. Enable apis:
    * `cloudbuild.googleapis.com`
    * `run.googleapis.com`

3. Create a service account with roles
    * Cloud Run Admin
    * Storage Admin
    * Cloud Build Service Account

4. Get key
5. Setup env vars
6. Run build
7. Run `gcr_deploy`
```bash
> ./scripts.sh gcr_deploy
Allow unauthenticated invocations to [hello-world] (y/N)?

Deploying container to Cloud Run service [hello-world] in project [python-concourse-1313] region [us-central1]
✓ Deploying new service... Done.
  ✓ Creating Revision... Deploying Revision...
  ✓ Routing traffic...
Done.
Service [hello-world] revision [hello-world-00001-wud] has been deployed and is serving 100 percent of traffic at <service_url>
```
8. `export GCP_SERVICE_URL=<service_url>`


### Test your service locally

```bash
curl -SH "Content-Type: application/json" --request GET  \
    http://localhost:80/hello
```

```bash
curl -SH "Content-Type: application/json" --request POST  \
    --data '{"description":"ticket description","title":"ticket title"}' \
    http://localhost:80/create
```

### Test your service on Cloud Run

```bash
curl -SH "Content-Type: application/json" --request GET  \
    -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    $GCP_SERVICE_URL/hello
```
Test `$GCP_SERVICE_URL/hello?word=you` for a different response.


```bash
curl -SH "Content-Type: application/json" --request POST  \
    -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    --data '{"description":"ticket description","title":"ticket title"}' \
    $GCP_SERVICE_URL/create
```

## Concourse

### Sample pipeline
```bash
./scripts.sh concourse_set_pipeline hello_world
# Unpause from UI
```

