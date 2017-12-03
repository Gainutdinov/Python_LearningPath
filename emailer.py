import requests
import smtplib


api_key = input("What's is your API key for openweather?")

def get_emails():
    emails = {}
    try:
        email_file = open('emails2.txt','r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)
    return emails

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    return schedule

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')

        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)
    
    return schedule

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Kazan&units=metric&APPID=41f472b4e810a5def86b69214c2f99b2'
     
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max)) + 'Celciuses'
    forecast += ' and a low of ' + str(int(temp_min))  + 'Celciuses'

    return(forecast)


def send_emails(emails, schedule, forecast):
    # Connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com','587')

    # Start TLS encryption
    server.starttls()

    # Login
    password = input("What's is your password?")
    server.login('gaynetdin@gmail.com', password)
    from_email = 'gaynetdin@gmail.com'
    server.sendmail(from_email,from_email, 'Test Message')

    # Send to entire email list
    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Kazan!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to see you there!'
        server.sendmail(from_email,to_email, message)
    server.quit()


def main():
    emails = get_emails()

    schedule = get_schedule()

    forecast = get_weather_forecast()

    send_emails(emails, schedule, forecast)

main()










    
