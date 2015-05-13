# django-aws-simple-duplicate-image-checker

Simple django app that allows for uploading of image to s3 (via vanilla django admin app) and checks for duplicates using pHash in a celery task. Postgres RDS used for backing database.

More details to come (on setup/deployment/demo)

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

## Demo / Screenshots
### Django Admin Panels

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin1.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin2.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin3.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin4.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin5.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/aws-s3-storage.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/admin4.png)

### Local console

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/console1.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/console2.png)

### AWS console

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/aws-s3.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/aws-rds.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/aws-sqs.png)

![Screenshot](https://github.com/kevd1337/django-aws-simple-duplicate-image-checker/blob/master/demo-screenshots/aws-ec2.png)
