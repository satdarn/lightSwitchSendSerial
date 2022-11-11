import datetime
import calendar
import time
import serial

# implement in Prod
#Serial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=10)

def send(data):
    #just incase of Arduino not being conected
    try:
        Serial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600, timeout=10)
        Serial.write(bytes(data, 'utf-8'))
    except:
        print(f"Serial Failed \n {data} not sent")
    time.sleep(0.05)

Schedual = {
"Monday": { 
    "on": ["5:00", "16:00"],
    "off": ["15:00", "9:00"],
},
"Tuesday": {
    "on": ["5:00", "16:00"],
    "off": ["15:00", "9:00"],
},
"Wednesday": {
    "on": ["5:00", "16:00"],
    "off": ["15:00", "9:00"],
},
"Thursday": {
    "on": ["5:00", "16:00"],
    "off": ["15:00", "9:00"],    
},
"Friday": {
    "on": ["5:00", "16:00"],
    "off": ["15:00", "9:00"],    
},
"Saturday": {
    "on": ["5:00"],
    "off": ["15:00"],    
},
"Sunday": {
    "on": ["5:00" ],
    "off": ["15:00"],    
}
}


current_time = datetime.datetime.now()
def findDayofWeek():
    date = f'{current_time.day-6} {current_time.month} {current_time.year}'
    dayOfWeek = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[dayOfWeek])

dayOfWeek = findDayofWeek()

alarmSchedual = Schedual[dayOfWeek]

def checkTimes():

    for onTime in alarmSchedual["on"]:
        [hour, min] = onTime.split(":")
        print(current_time.minute)
        if int(hour) == current_time.hour and int(min) == current_time.minute:
            send("2")
            break
    for offTime in alarmSchedual["off"]:
        [hour, min] = offTime.split(":")
        print(current_time.minute)
        if int(hour) == current_time.hour and int(min) == current_time.minute:
            send("1")
            break

def main():
    