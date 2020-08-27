#!/usr/bin/env python3
from requests import Session
from bs4 import BeautifulSoup as bs
import re

from secrets import USER, PASS

payload = {
    'Account': USER,
    'Password': PASS,
    'AccountMode': '9'
}

logon_url='https://oneweb.indianatech.edu/OneWeb/Account/LogOn'
meal_url='https://oneweb.indianatech.edu/OneWeb/Financial/CWMealPlanStatus'

def get_session():
    s = Session()
    logon = bs(s.get(logon_url).content, 'html.parser')
    form = logon.find('form', action='/OneWeb/Account/LogOn')
    payload['__RequestVerificationToken'] = form.find('input', attrs={'name': '__RequestVerificationToken'})['value']
    p = s.post(logon_url, data=payload)
    return s

def get_remaining_meals(s: Session):
    page = bs(s.get(meal_url).content, 'html.parser')
    status = page.find('td', attrs={'data-title': 'Status:'})
    meals = re.search(r'.*=([0-9]+)', status.text).group(1)
    return meals

if __name__ == "__main__":
    meals = get_remaining_meals(get_session())
    print('Meals remaining for this week: ', meals)

