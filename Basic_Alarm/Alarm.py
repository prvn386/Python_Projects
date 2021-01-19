from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the alarm time to be set in this format HH:MM:SS(AM/PM)\n")
alarm_hour = alarm_time[0:2]
alarm_min  = alarm_time[3:5]
alarm_sec  = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper() # this tells whether am or pm
while True:

    now = datetime.now()
    current_hour   = now.strftime('%I')
    current_minute = now.strftime('%M')
    current_second = now.strftime('%S')
    current_period = now.strftime('%p')
    if current_period == alarm_period:
        if current_hour == alarm_hour:
            if current_minute == alarm_min:
                if current_second == alarm_sec:
                    print('Wake Up')
                    playsound('alarm.mp3')
