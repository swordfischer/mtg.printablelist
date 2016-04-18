from BeautifulSoup import BeautifulSoup
import urllib2

html = '''
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <link rel='stylesheet' href='style.css'>
  </head>
  <body>
{}
  </body>
</html>
'''


url = urllib2.urlopen(
    'http://magic.wizards.com/en/game-info/products/card-set-archive')

content = url.read()

soup = BeautifulSoup(content)

mtg_list = []

divs = soup.findAll("div", { "class" : "card-set-archive-table" })

for div in divs:
    for li in div.findAll("li"):
        if li['class'] != 'title':
            try:
                mtg_icon = li.find("span", {"class" : "icon"}).img['src']
            except (NameError, TypeError):
                mtg_icon = 'none.png'
            try:
                mtg_set = li.find("span", {"class" : "nameSet"}).text
            except (NameError, TypeError):
                mtg_set = 'N/A'
            try:
                mtg_date = li.find("span", {"class" : "releaseDate"}).text
            except (NameError, TypeError):
                mtg_date = 'N/A'
            mtg_list.append({
                'icon': mtg_icon,
                'set': mtg_set,
                'date':mtg_date
            })


items = []
for item in mtg_list:
    items.append('''
    <div class='container'>
      <div class='symbol'>
        <img src='{icon}'>
      </div>
      <div class='fullinfo'>
        <div class='set'><p>{set}</p></div>
        <div class='date'><p>{date}</p></div>
      </div>
    </div>
    <div class='ruler'>
    </div>
    '''.format(**item))


items = '\n'.join(items)
with open('mtg.html', 'w') as text_file:
    text_file.write(html.format(items))

text_file.close()
