import callr
import os
from datetime import datetime


username = os.environ.get('LOGIN_CALLR')
password = os.environ.get('PWD_CALLR')

api = callr.Api(username, password)

def convert_utc_datetime(time, date):
    """ Convert local datetime on utc datetime """
    parser_time = time.split(':')
    parser_date = date.split('-')

    time_now = datetime.utcnow()

    execute_at = time_now.replace(
        year=int(parser_date[0]),
        month=int(parser_date[1]),
        day=int(parser_date[2]),
        hour=int(parser_time[0]) - 2,
        minute=int(parser_time[1]),
        second=0,
        microsecond=0
    )

    return execute_at