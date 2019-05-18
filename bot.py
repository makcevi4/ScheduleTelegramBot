# -*- coding: utf-8 -*-

"""
This bot is designed for parsing events( in this case - university schedule) from Google Calendar.
Also, every day at 7 am, the bot reminds student of upcoming events (schedule for the current day),
current weather at current city (depends on the location of the university).
***
Designed specially for Kyiv National University Culture and Arts,
Faculty of Information Policy and Cyber Security,
Department of Computer Since.
Designed by Maksym Bohynskyi, student of KNUCaA, CS
***
Language: UA
University location: Kyiv, Ukraine
***
For complaints and suggestions: bohynskyimaksym@gmail.com
"""
import config, scripts
import telepot, schedule, time

import emojies as e


# --- Basic actions --- #


def job():
    bot = telepot.Bot(config.telegram_token)

    def main():
        # calendar initialization
        service = scripts.basic_initialization(config.client_secret_calendar)

        # time initialization
        now, today, now_1day, weekday = scripts.datetime_initialization()

        # weather initialization
        current_weather_info = scripts.weather_info(config.owm_token)

        # - Events
        # events initialization
        events = scripts.events_initialization(config.calendar_id, service, now, now_1day)

        # default message
        message = "Good morning, students!\n\n" + \
                  e.calendar + "Today: " + today + " (" + weekday + ")\n" + \
                  e.weather + "Weather in " + config.location.capitalize() +": " + current_weather_info + "\n" + \
                  e.bell + "Events for today:\n\n"


        # forming a message for the bot
        if not events:
            message += "\nNOTHING PLANNED FOR TODAY" + e.idk
            bot.sendMessage(config.recipient_id, message)
        else:

            num = 0
            for event in events:
                num += 1

                # - Initializations: title, start time, end time, description, event links
                event_title, event_start, event_end, event_link, event_description = scripts.event_items_initialization(event)


                message += scripts.message_additional_parameters(num, event_title,
                                                                 event_start, event_end,
                                                                 event_description)

                # - Logs collection and display
                # logs = scripts.packing_to_dict(today, event_title, event_start, event_end, event['htmlLink'], description=None)
                # print(num, "=" * 25,
                #       "\n" , logs , "\n" +
                #       "=" * 25, "\n\n")

            message += e.more + "More: " + config.calendar_link
            bot.sendMessage(config.recipient_id, message)


    if __name__ == '__main__':
        main()

print('Processing ...')


# Reminder

if config.sr_status == 'ED':
    schedule.every().day.at(config.sr_time).do(job)  # at the specified time of the day
if config.sr_status == 'TEST':
    schedule.every(0.1).minutes.do(job) # every 10 sec

while True:
     schedule.run_pending()
     time.sleep(1)


