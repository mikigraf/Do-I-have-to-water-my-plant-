import RPi.GPIO as GPIO
import smtplib, time, sys
from time import gmtime, strftime

version = "0.1"

def callback(channel):
    if GPIO.input(channel):
        notify()
    else:
	print "Feutchigkeit erkennbar :)))!"

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

print "PlantWatcher" + version
GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel,GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel, callback)

counter = 0;

while True:
    counter += 1
    print counter
    time.sleep(5)

