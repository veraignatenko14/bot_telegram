import requests as r
from jinja2 import Template


def get_dog_img():
 url = 'https://random.dog/woof.json'
 resp = r.get(url).json()
 return resp['url']


def make_template(filename):
  with open(f'templates/{filename}.html', 'r', encoding='utf-8') as f:
   text = f.read()
  template = Template(text)
  return template


def parse_horo(sign):
 url = f"https://horoscopes-ai.p.rapidapi.com/get_horoscope_en/{sign}/tomorrow/general"

 headers = {
  "X-RapidAPI-Key": "39b2fbbbfamshc9aeb391d0d535ap1e47c4jsn6ce62fa8951c",
  "X-RapidAPI-Host": "horoscopes-ai.p.rapidapi.com"
 }

 response = r.get(url, headers=headers)
 res = response.json()
 try:
  return res['general'][0]
 except:
  return'У владельца бота закончились запросы к API'