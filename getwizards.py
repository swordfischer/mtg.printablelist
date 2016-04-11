from BeautifulSoup import BeautifulSoup
import urllib2

text_file = open ('mtg.html', 'w')
text_file.write("<html !DOCTYPE html>\r\n\t<head>\r\n\t\t<link rel=stylesheet href=style.css>\r\n\t</head>\r\n\t<body>\r\n")


url = urllib2.urlopen("http://magic.wizards.com/en/game-info/products/card-set-archive")

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
            except (NameError,TypeError):
              mtg_set = 'N/A'
            try:
              mtg_date = li.find("span", {"class" : "releaseDate"}).text
            except (NameError,TypeError):
              mtg_date = 'N/A'
            mtg_list.append([mtg_icon,mtg_set,mtg_date])



for item in mtg_list:
    text_file.write("\t\t<div class='container'>\r\n")
    text_file.write("\t\t\t<div class='symbol'><img src='" + item[0] + "'></div>\r\n")
    text_file.write("\t\t\t<div class='fullinfo'>\r\n")
    text_file.write("\t\t\t\t<div class='set'><p>" + item[1] + "</p></div>\r\n")
    text_file.write("\t\t\t\t<div class='date'><p>" + item[2] + "</p></div>\r\n")
    text_file.write("\t\t\t</div>\r\n")
    text_file.write("\t\t</div>\r\n")
    text_file.write("\t\t<div class='ruler'></div>\r\n")


text_file.write("\t</body>\r\n</html>\r\n")

text_file.close()
