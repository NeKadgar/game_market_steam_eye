# Steam Market Monitoring System

## Overview
Service for steam market monitoring and creating our DB, will pull history of prices for item and in 
future will monitor market once at some time to extend a price history by new data.

## Dependencies
* Python 3.8+

## Setup
Install the dependencies:

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage docker
Docker compose will start redis broker, celery worker and flower
```bash
$ docker-compose up
$ uvicorn main:app --reload
```
