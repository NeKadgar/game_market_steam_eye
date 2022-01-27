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

## API Examples:
 * http://steamcommunity.com/market/pricehistory/?country=PT&currency=3&appid=730&market_hash_name=Falchion%20Case
 * https://steamcommunity.com/market/itemordershistogram?country=PK&language=english&currency=1&item_nameid=176096390&two_factor=0&norender=1
 * https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name=StatTrak%E2%84%A2%20M4A1-S%20|%20Hyper%20Beast%20(Minimal%20Wear)