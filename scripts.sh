#!/bin/bash

case $1 in

  # Local
  init_workspace)
  if [[ $2 == "local" ]]; then
    pip install -r requirements/dev_requirements.txt
    pip install -r requirements/requirements.txt
    pip install -e .
  elif [[ $2 == "dev" ]]; then
    pip install -t dependencies -r requirements/dev_requirements.txt
  fi
  pip install -t dependencies -r requirements/requirements.txt
  pip install -t dependencies .
  ;;

  load_env_vars)
    source .env
  ;;

  all_tests)
    python -m pytest --cov app --cov-report html --cov-report term --cov-config .coveragerc tests/ -vs
  ;;

  lint)
    python -m flake8
  ;;

  serve_coverage)
    cd htmlcov
    python -m http.server 8001
  ;;

  run_app_local)
    FLASK_APP=app/routes.py python -m flask run
  ;;

  # Local with containers
  docker_run_app)
    docker-compose up -d
  ;;

  docker_stop_app)
    docker-compose stop
  ;;

  setup_concourse)
    ./keys/generate
    brew cask install fly
  ;;

  # Concourse locally
  docker_run_concourse)
    docker-compose -f docker-compose.concourse.yml up -d
  ;;

  docker_stop_concourse)
    docker-compose -f docker-compose.concourse.yml stop
  ;;

  # Concourse commands
  concourse_login)
    fly --target hello_world login --team-name main --concourse-url http://localhost:8080
  ;;

  concourse_set_pipeline)
    if [[ $2 ]]; then
      fly validate-pipeline --config pipelines/$2.yml
      fly -t hello_world set-pipeline --pipeline $2 --config pipelines/$2.yml -l pipelines/credentials.yml
    else
      echo 'missing pipeline name'
    fi
  ;;

  # GCP
  gcp_login)
    gcloud auth activate-service-account $GCP_SA \
      --key-file=$GCP_SA_PATH --project=$GCP_PROJECT_ID
  ;;

  gcb_build)
    gcloud builds submit --tag gcr.io/$GCP_PROJECT_ID/$GCP_IMAGE_NAME app/
  ;;

  gcr_deploy)
    gcloud run deploy $GCP_SERVICE_NAME \
      --region=$GCP_REGION \
      --image=gcr.io/$GCP_PROJECT_ID/$GCP_IMAGE_NAME \
      --service-account=$GCP_SA \
      --platform=$GCR_PLATFORM \
      --no-allow-unauthenticated
  ;;

  gcr_destroy)
    gcloud beta run services delete $GCP_SERVICE_NAME --platform=$GCR_PLATFORM \
      --region=$GCP_REGION
  ;;

  *)
    echo -n "unknown cmd :("
  ;;
esac
