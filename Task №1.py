import requests

def identifying_smartest(name_heroes):
    url = "https://akabab.github.io/superhero-api/api//all.json"
    respons = requests.get(url=url)
    list_heroes = name_heroes.split(', ')
    heroes = {}
    value_intelligence = []
    for i in respons.json():
        if i.get('name') in list_heroes:
            heroes[i['name']] =  i['powerstats']['intelligence']
    for number in heroes.values():
        value_intelligence.append(int(number))
    for key, value in heroes.items():
        if value == max(value_intelligence):
            res = f'Самый умный герой: {key} c количеством интеллекта  {value}'
    return print(res)

if __name__ == '__main__':
    identifying_smartest('Captain America, Thanos, Hulk')