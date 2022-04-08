def mache_gruss(n, s, h):
    if s == 'f':
        anrede = 'Mrs.'
    else:
        anrede = 'Mr.'

    if 0 <= h <= 9:
        tageszeit = 'Guten Morgen'
    elif 10 <= h <= 17:
        tageszeit = 'Guten Tag'
    else:
        tageszeit = 'Guten Abend'

    text = tageszeit + ', ' + anrede + ' ' + n
    return text










name = 'Joerg'
sex = 'f'
hour_of_day = 23

grusstext = mache_gruss(name, sex, hour_of_day)
print(grusstext)



print(mache_gruss('Koxi', 'm', 12))
print(mache_gruss('Hansi', 'f', 23))
