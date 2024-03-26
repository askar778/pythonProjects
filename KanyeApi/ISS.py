from datetime import *
import requests
import smtplib

today = datetime.now()

iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_lat = float(iss_response.json()["iss_position"]["latitude"])
iss_long = float(iss_response.json()["iss_position"]["longitude"])

my_lat = float(7.2476)
my_long = float(-82.6325)

parameter = {"lat": my_lat, "lng": my_long, "formatted": 0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter, )
sunrise = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])


def location_checker():
    if (my_lat - 5 < iss_lat < my_lat + 5) & (my_long - 5 < iss_long < my_long + 5):
        if sunrise > today.hour > sunset:
            return True
        else:
            return False
    else:
        return False


if location_checker():
    my_email = "7788askar@gmail.com"
    password = "lnfs qxyv siwh oqwd"
    to_address = "788askar@gmail.com"
    message = "look up"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)

