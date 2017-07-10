from mtgsdk import Set
import calendar
from time import strptime

html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link href="//cdn.jsdelivr.net/npm/keyrune@latest/css/keyrune.css" rel="stylesheet" type="text/css" />
    <link rel='stylesheet' href='style.css'>
  </head>
  <body>
{}
  </body>
</html>
'''

sets = Set.all()
sets.sort(key=lambda x: x.release_date, reverse=True)

mtg_list = []

for set in sets:
    if set.online_only != 1:
        mtg_list.append({
            'code': set.code.lower(),
            'name': set.name,
            'month': calendar.month_name[strptime(set.release_date, '%Y-%m-%d').tm_mon],
            'year': strptime(set.release_date, '%Y-%m-%d').tm_year
        })

items = []

for item in mtg_list:
    items.append('''
    <div class='container'>
        <div class='symbol'>
            <i class='ss ss-{code}'></i>
        </div>
        <div class='fullinfo'>
            <div class='set'><p>{name}</p></div>
            <div class='date'><p>{month}, {year}</p></div>
        </div>
    </div>
    <div class='ruler'>
    </div>
    '''.format(**item))

items = '\n'.join(items)
with open('mtg.html', 'w') as text_file:
    text_file.write(html.format(items))
text_file.close()

