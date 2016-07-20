import grovepi
import smtplib, time, sys
from time import gmtime, strftime

notified = false;

# Connect the Grove Moisture Sensor to analog port A0
# SIG,NC,VCC,GND
sensorA0 = 0

def notify(plantsWithDryEarth):
    # senders information
    s_username = sys.argv[1]
    s_password = sys.argv[2]
    # recipents information
    R_EMAIL_ADDRESS = sys.argv[3]
    print(sys.argv[1])  
    print(sys.argv[2])
    print(sys.argv[3])
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(s_username, s_password)
    header = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' To:' + R_EMAIL_ADDRESS + '\n' + 'From: ' + s_username + '\n' + 'Subject:[PlantWatcher] Water needed! \n'
    print header
    plants = ''.join(plantsWithDryEarth)
    print plants
    msg = header + '\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' Folgende Blumen brauchen Wasser: \n\n' + plants
    smtpserver.sendmail(s_username, R_EMAIL_ADDRESS, msg)
    print 'done!'
    smtpserver.close()

while True:
    valueA0 = 150
    plantsWithDryEarth = [];
    try:
        valueA0 = grovepi.analogRead(sensorA0)
        if valueA0 < 300 and notified = false:
            plantsWithDryEarth.append(sensorA0)
            notified = true;
            notify(plantsWithDryEarth)
        else if value > 300 and notified = true:
            notified = false;
        time.sleep(5)
    except KeyboardInterrupt:
            break
    except IOError:
            print "IOException :("
