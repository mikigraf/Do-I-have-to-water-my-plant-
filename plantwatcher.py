\# Skrypt napisany przez Mikolaja Wawrzyniaka @spejss
# Email do wysylania powiadomien musi byc adresem z koncowka @gmail.com!
# Argumenty w wierszu polecen:
# python plantwatcher.py <email do wysylania powiadomien> <haslo do tego emaila> <email na ktory te powiadomienia maja docierac>
# Przyklad: python plantwatcher.py jaroslaw@gmail.com kotekkotkajarka powiadommnie@gmail.com

import RPi.GPIO as GPIO
import smtplib, time, sys, datetime
from time import gmtime, strftime
version = "0.2"

# Dzien w roku, w ktorym zostalo wyslane ostatnie powiadomienie
lastNotifiedOn = 0

# Funkcja, ktora zostaje wywolana w odpowiedzi na wydarzenia
def callback(channel):
    if lastNotifiedOn is None:
	global lastNotifiedOn
	lastNotifiedOn = 0
    # Jesli nadchodzi sygnal i dzien, w ktorym zostalo wyslane ostatnie powiadomienie
    # nie jest dniem dzisiejszym, to wyslij powiadomienie 
    if GPIO.input(channel) and lastNotifiedOn is not datetime.datetime.now().timetuple().tm_yday :
        notify()
	lastNotifiedOn = datetime.datetime.now().timetuple().tm_yday
	print "Wilgoc nie zostala wykryta. Ostatnie powiadomienie zostalo wyslane w  %s dniu tego roku" %(lastNotifiedOn)
    else:
	print "Wilgoc zostala wykryta. Wszystko w porzadku! :)"

def notify():
    # informacje o nadawcy
    s_username = sys.argv[1]
    s_password = sys.argv[2]

    # informacje o odbiorcy
    R_EMAIL_ADDRESS = sys.argv[3]
    print(sys.argv[1])  
    print(sys.argv[2])
    print(sys.argv[3])
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(s_username, s_password)
    header = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ' To:' + R_EMAIL_ADDRESS + '\n' + 'From: ' + s_username + '\n' + 'Subject:[PlantWatcher] Potrzeba wody :(  \n'
    print header
    msg = header + '\n' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " Woda nie zostala wykryta :( Twoje kwiaty potrzebuja wody.  \n\n"
    smtpserver.sendmail(s_username, R_EMAIL_ADDRESS, msg)
    print 'Wyslane!'
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

