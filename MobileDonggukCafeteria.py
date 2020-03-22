# made by Yangjin Cho.
# Check for latest release at https://github.com/sheepjin99/DonggukCafeteria/releases.

import time
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import logging


d = datetime.datetime.now()
d = d.replace(minute=00, hour=00, second=00)
d = (int(time.mktime(d.timetuple())))  # one day = 86400
posix = "&sday="+str(d)

secs = time.time()
tm = time.localtime(secs)
hour = tm.tm_hour

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler("MobileDonggukCafeteria.py.log")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

html = urlopen("http://dgucoop.dongguk.edu/mobile/menu.html?code=5"+posix)
logger.info("Sangrokwon3f DGUcoop Website Opened")
sang3f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=1' + posix)
logger.info("Sangrokwon2f DGUcoop Website Opened")
sang2f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=7'+posix)
logger.info("Sangrokwon1f DGUcoop Website Opened")
sang1f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=2'+posix)
logger.info("Grutergi DGUcoop Website Opened")
grutergi_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=0'+posix)
logger.info("Pan & Noodle DGUcoop Website Opened")
pan_noodle_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=9'+posix)
logger.info("GardenCook DGUcoop Website Opened")
gardencook_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=8'+posix)
logger.info("Dormitory DGUcoop Website Opened")
dorm_source = html.read()
html.close()

##############################################################################
d += 86400
posix = "&sday="+str(d)

html = urlopen("http://dgucoop.dongguk.edu/mobile/menu.html?code=5"+posix)
logger.info("Tomorrow Sangrokwon3f DGUcoop Website Opened")
tomorrow_sang3f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=1' + posix)
logger.info("Tomorrow Sangrokwon2f DGUcoop Website Opened")
tomorrow_sang2f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=7'+posix)
logger.info("Tomorrow Sangrokwon1f DGUcoop Website Opened")
tomorrow_sang1f_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=2'+posix)
logger.info("Tomorrow Grutergi DGUcoop Website Opened")
tomorrow_grutergi_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=0'+posix)
logger.info("Tomorrow Pan & Noodle DGUcoop Website Opened")
tomorrow_pan_noodle_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=9'+posix)
logger.info("Tomorrow GardenCook DGUcoop Website Opened")
tomorrow_gardencook_source = html.read()
html.close()

html = urlopen('http://dgucoop.dongguk.edu/mobile/menu.html?code=8'+posix)
logger.info("Tomorrow Dormitory DGUcoop Website Opened")
tomorrow_dorm_source = html.read()
html.close()

def sangrok_3f(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang3f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang3f_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result


def sangrok_2f(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang2f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang2f_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result

def sangrok_1f(tr=1, td=1, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(sang1f_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_sang1f_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result

def grutergi(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(grutergi_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_grutergi_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result

def grutergi_pan_noodle(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(pan_noodle_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_pan_noodle_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result


def gardencook(tr, td, day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(gardencook_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_gardencook_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result

def dormitory(tr, td,day=0):
    if day is 0:
        tasty_soup = BeautifulSoup(dorm_source, "lxml")
    else:
        tasty_soup = BeautifulSoup(tomorrow_dorm_source, "lxml")
        table = tasty_soup.find("table")
        tables = table
        menu_table = tables  # second table is the menu table what we are looking for
        menu_tr = menu_table.find_all('tr')  # tr number will be index of cafeteria
        cafeteria = menu_tr[tr]
        for span in tasty_soup.find_all("span"):
            span.replace_with("\n")
        menu_td = cafeteria.find_all('td')
        result = str(menu_td[td].text)
        if result is "":
            result = "데이터가 없습니다."
        return result

sangrok_3f_jipbab_lunch = sangrok_3f(1,1)
sangrok_3f_jipbab_dinner = sangrok_3f(1,2)
sangrok_3f_hangurut_lunch = sangrok_3f(2,1)
sangrok_3f_hangurut_dinner = sangrok_3f(2,2)
sangrok_3f_vegeterian = sangrok_3f(3,1)

sangrok_2f_bakban_lunch = sangrok_2f(1,1)
sangrok_2f_bakban_dinner = sangrok_2f(1,2)
sangrok_2f_ilpum_lunch = sangrok_2f(2,1)
sangrok_2f_ilpum_dinner = sangrok_2f(2,2)
sangrok_2f_western_lunch = sangrok_2f(3,1)
sangrok_2f_western_dinner = sangrok_2f(3,2)
sangrok_2f_ttukbaegi_lunch = sangrok_2f(4,1)
sangrok_2f_ttukbaegi_dinner = sangrok_2f(4,2)

sangrok_1f_menu = sangrok_1f()

grutergi_A_lunch = grutergi(1,1)
grutergi_A_dinner = grutergi(1,2)
grutergi_B_lunch = grutergi(2,1)
grutergi_B_dinner = grutergi(2,2)

grutergi_pan_lunch = grutergi_pan_noodle(1,1)
grutergi_pan_dinner = grutergi_pan_noodle(1,2)
grutergi_noodle_lunch = grutergi_pan_noodle(2,1)
grutergi_noodle_dinner = grutergi_pan_noodle(2,2)


gardencook_salad = gardencook(1, 1)
gardencook_pasta = gardencook(2, 1)
gardencook_risotto = gardencook(3, 1)
gardencook_fried_rice = gardencook(4, 1)
gardencook_pizza = gardencook(5, 1)

dormitory_buffet_breakfast = dormitory(1,1)
dormitory_a_lunch = dormitory(2,2)
dormitory_a_dinner = dormitory(2,3)
dormitory_b_lunch = dormitory(3,2)
dormitory_b_dinner = dormitory(3,3)
dormitory_foodcourt_lunch = dormitory(4,2)
dormitory_foodcourt_dinner = dormitory(4,3)

###############################################################################

tomorrow_sangrok_3f_jipbab_lunch = sangrok_3f(1,1,1)
tomorrow_sangrok_3f_jipbab_dinner = sangrok_3f(1,2,1)
tomorrow_sangrok_3f_hangurut_lunch = sangrok_3f(2,1,1)
tomorrow_sangrok_3f_hangurut_dinner = sangrok_3f(2,2,1)
tomorrow_sangrok_3f_vegeterian = sangrok_3f(3,1,1)

tomorrow_sangrok_2f_bakban_lunch = sangrok_2f(1,1,1)
tomorrow_sangrok_2f_bakban_dinner = sangrok_2f(1,2,1)
tomorrow_sangrok_2f_ilpum_lunch = sangrok_2f(2,1,1)
tomorrow_sangrok_2f_ilpum_dinner = sangrok_2f(2,2,1)
tomorrow_sangrok_2f_western_lunch = sangrok_2f(3,1,1)
tomorrow_sangrok_2f_western_dinner = sangrok_2f(3,2,1)
tomorrow_sangrok_2f_ttukbaegi_lunch = sangrok_2f(4,1,1)
tomorrow_sangrok_2f_ttukbaegi_dinner = sangrok_2f(4,2,1)

tomorrow_sangrok_1f_menu = sangrok_1f()

tomorrow_grutergi_A_lunch = grutergi(1,1,1)
tomorrow_grutergi_A_dinner = grutergi(1,2,1)
tomorrow_grutergi_B_lunch = grutergi(2,1,1)
tomorrow_grutergi_B_dinner = grutergi(2,2,1)

tomorrow_grutergi_pan_lunch = grutergi_pan_noodle(1,1,1)
tomorrow_grutergi_pan_dinner = grutergi_pan_noodle(1,2,1)
tomorrow_grutergi_noodle_lunch = grutergi_pan_noodle(2,1,1)
tomorrow_grutergi_noodle_dinner = grutergi_pan_noodle(2,2,1)


tomorrow_gardencook_salad = gardencook(1, 1,1)
tomorrow_gardencook_pasta = gardencook(2, 1,1)
tomorrow_gardencook_risotto = gardencook(3, 1,1)
tomorrow_gardencook_fried_rice = gardencook(4, 1,1)
tomorrow_gardencook_pizza = gardencook(5, 1,1)

tomorrow_dormitory_buffet_breakfast = dormitory(1,1,1)
tomorrow_dormitory_a_lunch = dormitory(2,2,1)
tomorrow_dormitory_a_dinner = dormitory(2,3,1)
tomorrow_dormitory_b_lunch = dormitory(3,2,1)
tomorrow_dormitory_b_dinner = dormitory(3,3,1)
tomorrow_dormitory_foodcourt_lunch = dormitory(4,2,1)
tomorrow_dormitory_foodcourt_dinner = dormitory(4,3,1)


print(sangrok_3f_jipbab_lunch)