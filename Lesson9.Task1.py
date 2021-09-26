from pprint import pprint
import requests

def intell_hero(Hero):

    url = ("https://superheroapi.com/api/2619421814940190/search/" + Hero)
    date = {}
    carakter = {}
    resp = requests.get(url, timeout=5)
    date = resp.json()
    carakter[Hero] = date['results'][0]['powerstats']['intelligence']
    return carakter


def best_heroes(Hero1, Hero2, Hero3):
   zet = {}
   zet = {**intell_hero(Hero1), **intell_hero(Hero2), **intell_hero(Hero3)}
   zet_zero = list(zet.values())
   max_st = 0
   max_i = 999
   for i, st in enumerate(zet_zero):
       if int(st) > int(max_st):
           max_st = st
           max_i = i

   zet_result = list(zet.keys())
   print(f"Самый интеллектуальный супергерой: '{zet_result[max_i]}'")
   return

best_heroes('Hulk', 'Captain America', 'Thanos')


