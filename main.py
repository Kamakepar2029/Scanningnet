import os
from datetime import datetime
import requests as r

lol = r.get('https://raw.githubusercontent.com/Kamakepar2029/allnerwork/main/res.txt')

f = open("res.txt", "a")
f.write(lol.text)
f.close()

res = open("res.txt","r").read()

example = 'Host: 175.119.133.197 ()	Status: Up'

mass = res.split('\n')

start = 0
end = len(mass)

html = ''

while start < end:
  pol = mass[start].split(' ')
  print(pol)
  if pol[0] == 'Host:':
    if pol[2] == '()\tStatus:':
      if pol[3] == 'Up':
        print('New Host: '+pol[1]+' Status: '+pol[3])
        html = html + '<p class="all"><a class="status">Status: '+pol[3]+'</a><a class="href" href="http://'+pol[1]+'">'+pol[1]+'</a></p>'
      else:
        print('No hot up')
    else:
      print('No new Host up')
  else:
    print('No new Host down or up')
  start+=1

os.system('mkdir '+datetime.today().strftime('%d.%m.%Y'))
ls = datetime.today().strftime('%d.%m.%Y')
f = open(ls+"/index.html", "a")
f.write(html)
f.close()

print(html)
