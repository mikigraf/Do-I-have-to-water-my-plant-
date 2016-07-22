# This script requires 3 command line arguments
# 1st argument: senders email address
# 2nd argument: password to the senders email address
# 3rd argument: recipents email address
import RPi.GPIO as GPIO
import smtplib, time, sys, datetime
from time import gmtime, strftime
version = "0.2"

# check if the notification has been already sent, in case of an triggering event
notified = False

# day of the year, during which the last notification was sent on
lastNotifiedOn = 0

def callback(channel):
    if lastNotifiedOn is None:
	global lastNotifiedOn
	lastNotifiedOn = 0
     
    if GPIO.input(channel) and lastNotifiedOn is not datetime.datetime.now().timetuple().tm_yday :
        notify()
	lastNotifiedOn = datetime.datetime.now().timetuple().tm_yday
	print "Feuchtigkeit ist nicht erkennbar und eine Benachrichtigung wurde am %s Tag des Jahres verschickt" %(lastNotifiedOn)
    else:
	print "Feuchtigkeit ist erkennbar."

def notify():
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
    msg = header + '\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' Deine Blumen muessen unbedingt Wasser bekommen, sonst wird nix Bruddi \n\n'
    smtpserver.sendmail(s_username, R_EMAIL_ADDRESS, msg)
    print 'done!'
    smtpserver.close()
    notified = True

print "PlantWatcher" + version
GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel,GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(0.1)

