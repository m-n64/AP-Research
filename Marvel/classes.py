import requests
import datetime
import hashlib

ts = datetime.datetime.now()
private = '30c73a4e3895c2f78b166636eb8f43bff7f6a465'
public = 'ad7bdc0c0a8f960f5e30974657f735fe'
hash = hashlib.md5(f'{ts}{private}{public}'.encode()).hexdigest()
print(hash)

