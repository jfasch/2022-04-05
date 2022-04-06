import sys

name = input('Gib bitte deinen Namen ein, lieber Freund: ')
sex = input('Gib noch dein Geschlecht ein (m/f): ')
sex = sex.lower()

if sex == 'm':
    anrede = 'Mr.'
elif sex == 'f':
    anrede = 'Mrs.'
else:
    print('Das ist jetzt aber kein gueltiges Geschlecht (ich sagte m/f)')
    sys.exit(1)

hour_of_day = input('Uhrzeit auch noch (0-23): ')

hour_of_day = int(hour_of_day)

if 0 <= hour_of_day <= 9:
    phrase = "Good Morning"
elif 10 <= hour_of_day <= 17:
    phrase = "Good Day"
elif 18 <= hour_of_day <= 23:
    phrase = "Good Evening"
else:
    print('Uhrzeit ist schlecht (0-23 sagte ich!!)')
    sys.exit(2)

greeting = phrase + ', ' + anrede + ' ' + name
print(greeting)
