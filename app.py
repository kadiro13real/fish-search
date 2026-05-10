import requests
from flask import Flask,render_template,request
import time
import threading

class Fish:
    def __init__(self, lat=None, lon=None, month=None, day=None, hour=None, coords=None):
        self.lat = lat
        self.lon = lon
        self.month = month
        self.day = day
        self.hour = hour
        self.coords = coords

    



app = Flask(__name__)

def keep_alive()
    while True
        try:
            requests.get("https://fish-search.onrender.com")
        except:
            pass
        time.sleep(600)


threading.Thread(target=keep_alive, daemon=True).start()





@app.route('/')
def home():
    fish = request.args.get("fish")
    if fish == None:
      fish = "moray eel"
    descripiton = "none"
    img = "logo.png"
    amount = "5"
    lat = "0"
    lon = "0"
    month = "1"
    day = "1"
    hour = "1"
    coords = []
    test = 0
    map_url = "https://static-maps.yandex.ru/1.x/?ll=0,0&z=1&size=600,400&l=map&pt=0,-0,pm2ntm"
    
    url = f"https://api.inaturalist.org/v1/taxa?q={fish}&per_page=1"
    response = requests.get(url)
    if response.status_code == 200:
         response_json = response.json()
         try:
            img = response_json["results"][0]["default_photo"]["medium_url"]
         except:
            img = "logo.png"

    
    else:
        test = 0
        #print(f"Failed: {response.status_code}")

    headers = { "User-Agent": "GFishingApp/1.0 (https://fishing-website.onrender.com/index.html)" }
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{fish}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
         response_json = response.json()
         try:
            descripiton = response_json["extract"]
         except:
            descripiton = "NONE"
         
    
    else:
        test = 0
        #print(f"Failed: {response.status_code}")



    url = f"https://api.inaturalist.org/v1/observations?taxon_name={fish}&per_page=50"
    response = requests.get(url)
    

    if response.status_code == 200:
         response_json = response.json()
         print(response_json)
         try:
            fishes = []
            for i in range(50):
               day = response_json["results"][i]["created_at_details"]["day"]
               month = response_json["results"][i]["created_at_details"]["month"]
               hour = response_json["results"][i]["created_at_details"]["hour"]
               coords = response_json["results"][i]["geojson"]["coordinates"]

               #fish = Fish(name=f"Fish {i}")
               fishes.append(fish)
               lat = coords[1]
               lon = coords[0]
               print(coords)
               print("hello")
               map_url += f"~{lon},{lat},pm2blm"
               

         except:
            lat = "0"
            lon = "0"
            month = "1"
            day = "1"
            hour = "1"
            coords = [0,0]
            print("world")
         
    
    else:
        print(f"Failed: {response.status_code}")
    


    
    



    return render_template("index.html",img = img,fish = fish,descripiton = descripiton,map_url = map_url)


@app.route("/map_file")
def map_file():
   return render_template("map.html")
        
