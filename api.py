
import time
from hashlib import md5
import requests as rq

def get_characters():
  public_key = '89f253273663427e2246320e29453ef1'
  private_key = '4de088feb76a6430ff2b5981b7e6ac0b9b2e0daa'
  ts = str(time.time())  
  hash_str = md5(f"{ts}{private_key}{public_key}".encode("utf8")).hexdigest()
  
  params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash_str,
        "orderBy": "name",
        "limit":1
    } 
  try:
    response = rq.get('https://gateway.marvel.com:443/v1/public/characters', params=params) 
  except Exception as e:
    return False, e
  else:
    return response.json()

response = get_characters()
print(response)