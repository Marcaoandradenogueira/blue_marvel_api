
import time
from hashlib import md5
import requests as rq
import json
import datetime
from tempfile import NamedTemporaryFile
import os
import boto3

def get_characters(information):
  public_key = '89f253273663427e2246320e29453ef1'
  private_key = '4de088feb76a6430ff2b5981b7e6ac0b9b2e0daa'
  ts = str(time.time())  
  hash_str = md5(f"{ts}{private_key}{public_key}".encode("utf8")).hexdigest()
  
  params = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash_str,
        "orderBy": "name"
    } 
  try:
    response = rq.get(f'https://gateway.marvel.com:443/v1/public/{information}', params=params) 
  except Exception as e:
    return False, e
  else:
    return response.json()

def _write_to_file(tempfile, data):
        with open(tempfile.name, "a") as f:
            f.write(json.dumps(data) + "\n")

def _write_file_to_s3(s3, key, tempfile):
    s3.put_object(
        Body=tempfile,
        Bucket=os.environ['BUCKET_NAME_RAW'],
        Key=key
    )

def write(data, information):
    s3 = boto3.client('s3')
    tempfile = NamedTemporaryFile()
    key = f"marvel_lake_raw/day-summary/{information}/extracted_at={datetime.datetime.now().date()}/{datetime.datetime.now()}.json"
    _write_to_file(tempfile=tempfile, data=data)
    _write_file_to_s3(s3, key, tempfile)


def handler(event, context):
    informations = ['characters', 'comics']
    for information in informations:
        response = get_characters(information)
        write(response, information)
