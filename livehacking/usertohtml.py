def user_to_html(u):
    fn = u['firstname']
    ln = u['lastname']
    nr = u['svnr']

    html = '<ul>\n  <li>' + fn + '</li>\n  <li>' + ln + '</li>\n  <li>' + nr + '</li>\n</ul>'

    return html

grazer_melderegister = [
    {
        'firstname': 'Joerg',
        'lastname': 'Faschingbauer',
        'svnr': '1037190666',
    },
    {
        'firstname': 'Caro',
        'lastname': 'Faschingbauer',
        'svnr': '1234250497'
    },
    {
        'firstname': 'Hans',
        'lastname': 'Huber',
        'svnr': '6666'
    }
]

html_vom_grazer_melderegister = ''

for user in grazer_melderegister:
    s = user_to_html(user)
    html_vom_grazer_melderegister += s

html_vom_grazer_melderegister = '''
<html>
   <head>
     <title>Grazer Melderegister</title>
   </head>
   <body>
     <h1>Das ist die Ueberschrift</h1>
''' + html_vom_grazer_melderegister + '''
   </body>
</html>
'''

print(html_vom_grazer_melderegister)
