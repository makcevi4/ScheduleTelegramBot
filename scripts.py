from __future__ import print_function
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from pyowm.exceptions import api_response_error

import httplib2, pyowm, time
import config
import emojies as e


# --- INITIALIZATIONS -- #


def basic_initialization(client_secret_calendar):
    """Basic initialization, means like a calendar initialization"""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(client_secret_calendar,
                                                                   'https://www.googleapis.com/auth/calendar.readonly')
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    return service

def events_initialization(calendar_id, service, t_min, t_max, results=10):
    """Event initialization"""
    eventsResult = service.events().list(
        calendarId=calendar_id, timeMin=t_min, timeMax=t_max, maxResults=results,
        singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    return events

def datetime_initialization():
    """Initialization of current date, time, number of day of the week and recognize it in usual format """
    now = datetime.utcnow().isoformat() + 'Z'
    today = datetime.strftime(datetime.now(), "%d.%m.%Y")
    weekday = formatted_weekday(datetime.today().weekday())

    now_1day = round(time.time())+86400 # плюс сутки
    now_1day = datetime.fromtimestamp(now_1day).isoformat() + 'Z'
    return now, today, now_1day, weekday

def event_items_initialization(event):
    """Event objects initialization.
    Objects: title, start time, end time, link, description"""
    # title
    title = event['summary']

    # start
    start = event['start'].get('dateTime', event['start'].get('date'))
    start = datetime_conversion(start)

    # end
    end = event['end'].get('dateTime')
    end = datetime_conversion(end)

    # link
    # link = event['htmlLink']
    link = config.calendar_link

    # description
    def description(event):
        try:
            description = event['description']
        except KeyError:
            description = "missing"
        return description
    description = description(event)
    return title, start, end, link, description


# --- ADDITIONAL --- #


def datetime_conversion(datetime):
    """Conversion of event start time and event end time to usual format"""
    return datetime[11:16]

def message_additional_parameters(num, title, start, end, description):
    """Formed message via additional parameters, which are obtained during the program"""
    emoji_number = e.num_to_emoji(num)
    message = emoji_number +". " + title + "\n"
    message += e.clock + "Duration: from " + str(start) + " to " + str(end) + "\n"
    message += e.description + "Description: " + description + "\n\n"
    return message

def formatted_weekday(weekday_int):
    """ Сonvert the number of the day of the week to the usual format"""
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for wd in range(0, 7):
        if wd == weekday_int:
            return weekdays[wd]


# --- WEATHER --- #


def getting_weather_data(owm_token, place):
    """Getting weather information from weather service."""
    owm = pyowm.OWM(owm_token,  language=config.lang)
    try:
        weather = owm.weather_at_place(place)
        stats = weather.get_weather()
    except api_response_error.NotFoundError:
        return None
    else:
        return stats

def getting_detailed_status(stats):
    """Getting detailed status from got weather data"""
    return stats.get_detailed_status()

def getting_temperature(stats):
    """Getting temperature from got weather data"""
    return stats.get_temperature('celsius')

def weather_info(owm_token):
    """Finally definition, unifying all weather functions."""
    weather_data = getting_weather_data(owm_token, config.location)
    detailed_status = getting_detailed_status(weather_data)
    temperature = getting_temperature(weather_data)
    return detailed_status.capitalize() + ", " + str(round(temperature['temp'])) + "°C"


# --- LOGS --- #


def packing_to_dict(time, title, start, end, link, description):
    """Collects the data to dictionary for logging.
    !!!
    Unfortunately, this function doesn't work as it should, temporarily
    !!!"""
    dict_log = {
        'time':time,
        'events':{
            'title':title,
            'start':start,
            'end':end,
            'description':[description],
        'link':link
        }
    }
    return dict_log