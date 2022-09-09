import json
import requests
from flask import Flask, render_template , request
import datetime
import os

from flask import Flask, render_template , request
#import urllib.request

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def wind():
    if request.method == "POST":
        city = request.form["city"]
        print(city)
        api="eda9df689cbf0eee711bfdf442a51ebd"
        url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api+"&units=metric"
        print(url)

        response = requests.get(url).json()
        print(response)
        if response["cod"] == 200:

        #data = json.loads(response)
        #data = {"temp":response.get("main")["temp"]}# use this or next line
            data = {"temp": response["main"]["temp"],
                    "name":response["name"],
                    "lon": response["coord"]["lon"],
                    "lat": response["coord"]["lat"],
                    "sunrise": datetime.datetime.fromtimestamp(response.get('sys')['sunrise']),
                    "status": 200}
            #print(data["temp"])
            return render_template("home.html",data=data)
        elif response["cod"] == "404":
            data = {"message":response["message"], "status":404}
            return render_template("home.html", data=data)

    else:
        data = None
        return render_template("home.html",data=data)

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(port=port)
