import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

total_cases = soup.find('div', class_='maincounter-number').find('span').text

table = soup.find('table', id='main_table_countries_today')

world_rows = table.find_all('tr', class_='total_row_world')
world_today = world_rows.pop()

new_cases_today = world_today.find_all('td')[3].text

table = soup.find('table', id='main_table_countries_yesterday')
world_rows = table.find_all('tr', class_='total_row_world')
world_yesterday = world_rows.pop()

yesterday_data = world_yesterday.find_all('td')
cases_yesterday, new_cases_yesterday = yesterday_data[2].text, yesterday_data[3].text

del yesterday_data, world_rows

percent_change = int(new_cases_today[1:].replace(',', '')) - int(new_cases_yesterday[1:].replace(',', ''))
percent_change /= int(new_cases_yesterday[1:].replace(',', ''))

fmt_str = "Total Cases:\t\t{}".format(total_cases)
fmt_str += "\nCases Yesterday:\t\t{}".format(cases_yesterday)
fmt_str += "\nNew Cases:\t\t{}\n".format(new_cases_yesterday)
fmt_str += "Percent Change:\t\t{:2.2%}".format(percent_change)

print(fmt_str)

from pynotifier import Notification
import pathlib

directory = pathlib.Path(__file__).parent.absolute().as_posix() + '/codevid.ico'

Notification(
    title='CODEVID Tracking',
    description=fmt_str,
    icon_path=directory,
    duration=15,
    urgency=Notification.URGENCY_NORMAL
).send()
