import json
import config
import searchMusic
import requests, json

lyrics_url = "https://openapi.naver.com/v1/papago/n2mt"
lan_url = "https://openapi.naver.com/v1/papago/detectLangs"

searchMusic.init()

lan_params = {
    "query" : searchMusic.lyric
}

headers = {
     "Content-Type": "application/json",
     "X-Naver-Client-Id": config.CLIENT_ID,
     "X-Naver-Client-Secret": config.CLIENT_SECRET,
}

response = requests.post(lan_url, json.dumps(lan_params), headers=headers)
if response.json()["langCode"] == "ko":
    print(searchMusic.lyric)
    
else:
    lyrics_params = {
        "source" : response.json()["langCode"],
        "target" : "ko",
        "text" : searchMusic.lyric.replace("\n", " "),
    }

    response = requests.post(lyrics_url, json.dumps(lyrics_params), headers=headers)
    print(response.json()["message"]["result"]["translatedText"])