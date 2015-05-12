# django-aws-simple-duplicate-image-checker

Simple django app that allows for uploading of image to s3 (via vanilla django admin app) and checks for duplicates using pHash in a celery task. Postgres RDS used for backing database.

More details to come (on setup/deployment)

## Requirements
### Expected software/packages in environment
* Python 2.7.6 ( build-essential python-dev python-setuptools virtualenv )
* Postgres ( postgresql libpq-dev )
* PIL libraries ( libjpeg8-dev libfreetype6-dev zlib1g-dev imagemagick graphicsmagick python-imaging )
* pHash related libaries ( libphash0 libphash0-dev )
* Python library requirements specified in requirements.txt, install via pip:
```sh
  $ source bin/activate
  $ pip install -r requirements.txt
```

### Expected environment variables
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


