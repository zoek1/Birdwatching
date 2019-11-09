from os import environ

from influxdb import InfluxDBClient


def get_influx_instance(host="127.0.0.1", user='telegraf', password='secret', db='aave'):
    influx_host = environ.get("INFLUX_HOST", host)
    influx_user = environ.get("INFLUX_USER", user)
    influx_password = environ.get("INFLUX_PASSWORD", password)
    influx_db = environ.get("INFLUX_DB", db)

    return InfluxDBClient(influx_host, 8086, influx_user, influx_password, influx_db)