import requests

def getLocation():
    url = "http://api.openweathermap.org/data/2.5/"
    key = "41fbe04a4f6b918a4a2b748bd32f1a34"

    try:
        response = requests.get(url)
    except:
        print("\nError: connection to server failed\n")
        exit()
    else:
        print("\nConnection to server successful!\n")
        while response.status_code != 200:
            loc = input("Please enter a city or zip code: ")
            try:
                response = requests.get(f"{url}forecast?q={loc}&appid={key}&units=imperial")
            except:
                print("\nError: connection to server failed\n")
                exit()    
            if response.status_code == 404:
                print("Error: city not found")

        return response.json()

def getForecast(location):
    url = "http://api.openweathermap.org/data/2.5/"
    key = "41fbe04a4f6b918a4a2b748bd32f1a34"
    lat = location["city"]["coord"]["lat"]
    lon = location["city"]["coord"]["lon"]

    try:
        forecast = requests.get(f"{url}onecall?lat={lat}&lon={lon}&appid={key}&units=imperial")
    except:
        print("\nError: connection to server failed\n")
        exit()
    else:
        return forecast.json()


def displayForecast(location, forecast):
    city = location["city"]["name"]
    country = location["city"]["country"]

    print(f"\nForecast for {city}, {country}:\n")
    for x in range (8):
        print(f"{'Today' if x == 0 else f'Day {x}'}:")
        print(f"\tWeather: {forecast['daily'][x]['weather'][0]['main']}")
        print(f"\tHigh: {round(forecast['daily'][x]['temp']['max'])}F")
        print(f"\tLow: {round(forecast['daily'][x]['temp']['min'])}F")
    

def main():
    response = "yes"
    print("\nWelcome!")

    while response == "yes" or response == "y":
        location = getLocation()
        forecast = getForecast(location)
        displayForecast(location, forecast)

        response = input("\nWould you like to check the forcast for another city? (yes or no): ")
        while response != "yes" and response != "y" and response != "no" and response != "n":
            print("Error: invalid entry")
            response = input("Would you like to check the forcast for another city? (yes or no): ")

    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()