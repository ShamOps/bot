import requests
import re
from bs4 import  BeautifulSoup as bs
from colorama import Fore, Back
from pyowm import  OWM
import io, sys
from emails import  Email

from emails import from_template
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout


t_url = "https://trends24.in/pakistan/"
tt = "Twitter Trends In Pakistan"
r = requests.get(t_url)
soup = bs(r.text, "html.parser")
ft = set()
print(tt.center(50))
for x in soup.find_all('a', text=re.compile(".*#.*")):
    tags = x.text
    if tags not in ft:
        haha = "Nothing"
    ft.add(tags)
for u in ft:
    print("==============================")
    print(Fore.MAGENTA+'Tag: '+Fore.GREEN+u+Fore.RESET)
    tl = 'https://mobile.twitter.com/search?q=trend&src=typed_query'
    fu = u.replace('#','%23')
    link = tl.replace('trend',fu)
    print(Fore.MAGENTA+'Link: '+Fore.RESET+Fore.YELLOW+link+Fore.RESET)
    



print("==============================")
print('')
# Uni Stuff
'''
u_url = "https://www.aup.edu.pk/all_news.php"
tit = "University Notifications"
r = requests.get(u_url)
soup = bs(r.text, "html.parser")
print(tit.center(50))
for x in soup.findAll('a', class_='link'):
    print("==============================")
    tb = x.getText()
    lk = x['href']
    print(Fore.MAGENTA+'Notification: '+Fore.GREEN+tb.title()+Fore.RESET)
    print('')
    print(Fore.MAGENTA+'Link: '+Fore.LIGHTYELLOW_EX +'https://aup.edu.pk/'+lk)
print("==============================")    
'''
# Weather Details

owm = OWM('93d57cf20cccb6bc3971657bec3802c7')
print(Fore.GREEN)
mgr = owm.weather_manager()
lat = 34.300186
long = 71.722663
ob = mgr.weather_at_coords(lat, long)
w = ob.weather
print("Status: ", w.status)
print("Deep Status: ", w.detailed_status)
p = w.pressure
print('Pressure: ', p['press'])
print('Sea Level:', p['sea_level'])
print("Heat: ", w.heat_index)
print("Humidity: ", w.humidity)
wd = w.wind()
print('Wind Speed: ', wd['speed'])
print('Wind Degree ', wd['deg'])
print("Rain: ", w.rain)
print("Sun Rise: ", w.srise_time)
print("Sun Set: ", w.sset_time)
t = w.temperature('celsius')
print('Temperature: ', t['temp'])
print('Maximum Temperature: ', t['temp_max'])
print('Minimum Temperature: ', t['temp_min'])
print('Feels Like: ', t['feels_like'])
print(Fore.RESET)

output = new_stdout.getvalue()

sys.stdout = old_stdout

print(output)

#send data in mail


smtp_config = {
    'sender': 'zenalex786@gmail.com',
    'host': 'smtp.gmail.com',
    'port': 587,
    'password': 'kixxmyaxx'
}
template = {
    'smtp_config': smtp_config,
    'subject': 'How are you?',
    'body': output
}
my_email = from_template(template)

my_email.send('toorhat@gmail.com')

