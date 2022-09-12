import threading
import requests
from bs4 import BeautifulSoup
from application.data_layer import uow

uow.real_estate_dao.drop_real_estate()
uow.real_estate_dao.create_real_estate()

BASE_URL = 'https://www.nekretnine.rs'
LIST_URL = BASE_URL + '/stambeni-objekti/lista/po-stranici/10/stranica/'
SELECTORS = {
    'LIST_ITEM_TITLE': 'offer-title text-truncate w-100',
    'LOCATION': 'property__location',
    'SHORT_DETAILS': 'property__main-details',
    'FULL_DETAILS': '#detalji > div:nth-child(2)',
    'OTHER_DETAILS': '#detalji > div:nth-child(3)',
}

def page_spider(max_pages):
    page = 1
    while page < max_pages:
        url = LIST_URL + str(page) + '/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for item in soup.findAll('h2', {'class': SELECTORS['LIST_ITEM_TITLE']}):
            href = BASE_URL + item.find('a')['href']
            if href is not None:
                t = threading.Thread(target=single_item_data, args=(href,))
                t.start()
        page += 1

def single_item_data(item_url):
    try:
        source_code = requests.get(item_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')

        type = 'stan' if item_url.__contains__('stanovi') else 'kuća'
        offer = None
        location = None
        quadrature = None
        year_built = None
        land_area = None
        total_floors = None
        floor = None
        registered = None
        heating_type = None
        rooms = None
        toilets = None
        parking = None
        equipment = None

        full_location = soup.find('div', {'class': SELECTORS['LOCATION']}).text.strip().split('\n')
        city = full_location[2] if len(full_location) >= 3 else ''
        city_district = full_location[3] if len(full_location) >= 4 else ''
        location = city + '-' + city_district

        details = soup.select_one(SELECTORS['FULL_DETAILS'])
        if details is not None:
            for el in details.find_all('li'):
                li = el.text.strip()
                if 'Transakcija' in li:
                    offer = li.split(':')[1].strip()
                if 'Kvadratura' in li:
                    quadrature = li.split(':')[1].strip().split(' ')[0].strip()
                    if quadrature is not None:
                        quadrature = float(quadrature)
                if 'Uknjiženo' in li:
                    registered = li.split(':')[1].strip()
                if 'Godina izgradnje' in li:
                    year_built = li.split(':')[1].strip()
                if 'Broj kupatila' in li:
                    toilets = li.split(':')[1].strip()
                if 'Površina zemljišta' in li:
                    land_area = li.split(':')[1].strip()

        details = soup.find('div', {'class': SELECTORS['SHORT_DETAILS']})
        if details is not None:
            for el in details.find_all('li'):
                li = el.text.strip()
                if 'Parking' in li:
                    parking = li.split(':')[1].strip()
                if 'Grejanje' in li:
                    heating_type = li.split(':')[1].strip()
                if 'Sobe' in li:
                    rooms = li.split(':')[1].strip()
                if 'Sprat' in li:
                    floor = li.split(':')[1].split('/')[0].strip()
                    total_floors = li.split(':')[1].split('/')[1].strip()

        details = soup.select_one(SELECTORS['OTHER_DETAILS'])
        if details is not None:
            equipment = ''
            for el in details.find_all('li'):
                equipment += el.text.strip() + ', '
            equipment = equipment[:-2]

        uow.real_estate_dao.insert_row_real_estate(type, offer, location, quadrature, year_built, land_area, total_floors, floor, registered,
                         heating_type, rooms, toilets, parking, equipment)
    except:
        print('Failed to parse page: ' + item_url)


page_spider(10)
