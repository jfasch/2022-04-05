import sys

name = input('Gib bitte deinen Namen ein, lieber Freund: ')

while True:
    sex = input('Gib noch dein Geschlecht ein (m/f): ')
    sex = sex.lower()
    
    if sex == 'm':
        anrede = 'Mr.'
        break
    elif sex == 'f':
        anrede = 'Mrs.'
        break
    else:
        print('Das ist jetzt aber kein gueltiges Geschlecht (ich sagte m/f)')

while True:    
    hour_of_day = input('Uhrzeit auch noch (0-23): ')
    
    hour_of_day = int(hour_of_day)
    
    if 0 <= hour_of_day <= 9:
        phrase = "Good Morning"
        break
    elif 10 <= hour_of_day <= 17:
        phrase = "Good Day"
        break
    elif 18 <= hour_of_day <= 23:
        phrase = "Good Evening"
        break
    else:
        print('Uhrzeit ist schlecht (0-23 sagte ich!!)')

greeting = phrase + ', ' + anrede + ' ' + name
print(greeting)
