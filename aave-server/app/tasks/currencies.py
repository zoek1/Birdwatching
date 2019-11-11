#This example uses Python 2.7 and the python-request library.
from invoke import task
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

from aave import RESERVES


@task
def ids(c, key, url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/map', ):
    parameters = {
      'symbol': ','.join([reserve['symbol'] for reserve in RESERVES.values()])
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': key
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      for c in data['data']:
          print('{}: {}'.format(c['id'], c['symbol']))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)