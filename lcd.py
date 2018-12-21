import sys
from datetime import timedelta
from RPLCD.gpio import CharLCD
import os, datetime, time
from datetime import timedelta

lcd = CharLCD(cols=16, rows=2, pin_rs=11, pin_e=12, pins_data=[13,15,16,18])

sec = 0

days_old = 99
hrs_old = 99
mins_old = 99

vacances_targetTime = datetime.datetime(2018, 12, 21, 16, 30)
noel_targetTime = datetime.datetime(2018, 12, 25, 0, 0)

def print_lcd(banner, when, fini1, fini2):
        timeNow = datetime.datetime.now() # the time now
        remainingTime = (when - timeNow)
        days = remainingTime.days
        secs = remainingTime.seconds
        hrs, secs = divmod(secs, 3600)
        mins, secs = divmod(secs, 60)

	if remainingTime.total_seconds() > 0:	
		lcd.cursor_pos = (0, 0)
		s = banner+"                     "
		lcd.write_string(s[:16])

        	lcd.cursor_pos = (1, 0)
		s = str(days)+"J "+str(hrs)+"h "+str(mins)+"m "+str(secs)+"s              "
        	lcd.write_string(s[:16])
	else:
		lcd.cursor_pos = (0, 0)
		s = fini1 + "                     "
		lcd.write_string(s[:16])

        	lcd.cursor_pos = (1, 0)
		s = fini2 + "                     "
		lcd.write_string(s[:16])
		

i = 1
while 1 :
	if i < 5:
		print_lcd("Vacances dans", vacances_targetTime, "C'est", "Les Vacances!")
	if i >= 5:
		print_lcd("Noel dans", noel_targetTime, "Le Pere Noel", "est passe...")

	if i >= 8:
		i = 0

	i = i + 1
        
	time.sleep(1)
