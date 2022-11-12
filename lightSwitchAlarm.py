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

def getSchedualFromJson():
    #read the func name dibshit, its self expanitory
    with open() as jsonFile:
        pass
    return 


current_time = datetime.datetime.now()
def findDayofWeek():
    # see prevous comment
    date = f'{current_time.day-6} {current_time.month} {current_time.year}'
    dayOfWeek = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[dayOfWeek])

def checkTimes(alarmSchedual):
    #check the times in schedual against the current time 
    #send 1 to serial for off, send 2 to serial for on
    for onTime in alarmSchedual["on"]:
        [hour, min] = onTime.split(":") 
        if int(hour) == current_time.hour and int(min) == current_time.minute:
            send("2")
            return True
            break
    for offTime in alarmSchedual["off"]:
        [hour, min] = offTime.split(":")
        if int(hour) == current_time.hour and int(min) == current_time.minute:
            send("1")
            return True
            break
    

def main():
    while True:
        
        checkTimes(Schedual[findDayofWeek()])
        time.sleep(60)
main()