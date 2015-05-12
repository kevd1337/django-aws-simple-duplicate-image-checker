# django-aws-simple-duplicate-image-checker

Simple django app that allows for uploading of image to s3 (via vanilla django admin app) and checks for duplicates using pHash in a celery task. Postgres RDS used for backing database.

## Setup
###Expected environment variables:
* APP_DEBUG -> true or false, switches on django environment variables
* RDS_DB_NAME
* RDS_USERNAME
* RDS_PASSWORD
* RDS_HOSTNAME
* RDS_PORT
* AWS_ACCESS_KEY_ID -> requires a AWS IAM user with access to SQS and S3
* AWS_SECRET_ACCESS_KEY
* BOTO_S3_BUCKET
* BOTO_BUCKET_LOCATION
* BROKER_TRANSPORT_OPTIONS_REGION

More details to come (on setup/deployment)
