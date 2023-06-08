import requests as r


def get_dog_img():
  url = 'https://random.dog/woof.json'
  resp = r.get(url).json()
  return resp['url']


 def make_template(filename):
  with open(f'')

