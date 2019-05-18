# Schedule Telegram Bot
[logo]
## Description
> Attention! Logging is temporarily disabled in this version. Advanced users can manually enable this feature.

This bot is designed for parsing events (in this case - university schedule) from Google Calendar.
Also, every day at specified time, the bot reminds student of upcoming events (schedule for the current day),
current weather at current city (depends on the location of the university).

> To start you can use some other methods and mechanisms. Since I'm a beginner, I describe a method that I know

## Specifications
* Python 2.6 or greater
* Installed pip package management tool for Python
* Internet
* A Google account with Google Calendar enabled
## Used modules
* Telepot
```angular2
$ pip install telepot
```
* Google Calendar Api
```angular2
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
* PYOWM
```angular2
$ pip install pyowm
```
* httplib2
```angular2
pip install httplib2
```

All other modules should already be installed on your computer.
If you get the error "module not found", find module on the [PyPi](https://pypi.org) and install it.
## Usage

### Turn on the Google Calendar API

Visit [Python Quickstart](https://developers.google.com/google-apps/calendar/quickstart/python) and press **"ENABLE THE GOOGLE CALENDAR API"** button,
give a name to your project and agree to the terms of use.

Then come to **[Api Console](https://console.developers.google.com/?authuser=1&project=quickstart-1557704950837) 
-> Credentials -> Create credentials**

In the menu:
 
1.**"Where will you be calling the API from?"** choose **"Web server(e.g. node.js, Tomcat)"**

2.**"What data will you be accessing?"** choose **"Application data"**

3.**"Are you planning to use this API with App Engine or Compute Engine?"** choose **"No, I'm not using them"**

After that, press **"What credentials do I need?"** button.

Set the service account name and select a role: **App Engine -> App Engine Admin**

Press **"Continue"** button ang get your key as JSON file.

>After getting the file, it's better to move it to the directory with the bot files

### Getting OWM key

Visit [OpenWeatherMap](https://openweathermap.org/) and sign up. Then in **"API keys"** tab generate your API key.

### Getting Telegram Token

Open Telegram app and looking for a bot with the nickname **@botfather**, and start a dialogue with it.

Create a bot using the command **/newbot** and give it a name, and username.
>Attention! Username must end in "bot".

After the name is selected, **@botfather** will send the bot token.

### Replace values in the "config.py" file

1. In **lang** instead of text, specify the language in which you will receive weather alerts

2. In **location** instead of text, indicate the city where the university is located

3. In **sr_status** instead of text, specify status

   **sr_status** has two statuses: 
   * ED - the bot will notify you every day at the specified time. 
   If you specified this status, then you need to specify **sr_time** parameter

   * TEST - the bot will notify you every 10 sec, for test the performance
   
4. In **sr_time** instead of text, specify the time at which the bot should send a notification. 
Format "hh:mm", example: "07:00"


5. In **owm_token** instead of text, insert your token, which you generated on the [OpenWeatherMap](https://openweathermap.org/)

6. In **telegram_token** insert your token, which you got from **@botfather**

7. In **calendar_id**  insert your calendar identifier, which you can find in **Calendar options** on the [Google Calendar](https://calendar.google.com/calendar/)

8. In **client_secret_calendar** insert path on your JSON file with the key, which you got when turn on the Google Calendar API

9. In **recipient_id** insert user or group ID to which the bot will send messages. Also you can insert your ID.
How to get the ID, look on the Internet

10. In **calendar_link** insert a link to your Google Calendar that you use for parsing. 
It is advisable to use short links using the link shortener (bit.ly)


## Run

>To uninterrupted work of the  bot, you can place it on the server (Heroku and etc.) using instructions from the internet

1. Launch bot/Add to group

If in **recipient_id** you indicated group ID then find your bot and add it to the group to which it will send notifications.
But if you indicated your ID or another user, you (or recipient) must find the bot and run it from **/start** command

2. Run Virtual Environment

(how to install, follow the [link](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b))
```angular2
source env/bin/activate
```

3. Go to the directory where this repository was cloned
```angular2
cd /home/user/Repositories/ScheduleTelegramBot
```
4. Run the "bot.py" script

```angular2
python bot.py
```

5. Getting notifications

If in **sr_status** you specified the TEST-status, then bot will send notifications every 10 seconds. 
But if you specified the ED-status, then the bot will send you notifications at the time you specify
> Advanced users can change the test-time in the "bot.py" file



## About the project and the developer
This bot designed specially for Kyiv National University Culture and Arts,
Faculty of Information Policy and Cyber Security,
Department of Computer Since.

Designed by makcevi4 (Maksym Bohynskyi)

For question and suggestions: bohynskyimaksym@gmail.com