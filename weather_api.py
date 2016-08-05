import urllib

APIKEY = "*******"

zipcode = "****"
base_url = "http://api.openweathermap.org/data/2.5/weather?zip="
options = {
    "zip": zipcode + ",us",
    "appid": APIKEY
}

# from rohan's notes
# gets data from the URL
def getDataFromURL(base_url, options):
    import urllib.request
    import urllib.parse
    import json
  
    data = None
    params_str = urllib.parse.urlencode(options)
    request_url = base_url + params_str
    with urllib.request.urlopen(request_url) as response:
        # first read the response from the response object
        data = response.read()
        # now decode it from bytes to string
        data = data.decode("utf-8")
        # now parse the string into a python object of dictionaries and lists
        data = json.loads(data)
    return data

# gets ID number from data
def getID(zipcode):
    base_url = "http://api.openweathermap.org/data/2.5/weather?zip="
    options = {
    "zip": zipcode + ",us",
    "appid": APIKEY
    }
    data = getDataFromURL(base_url, options)
    weather = data["weather"]
    return splitStuff(str(weather))

# get the ID code from string
# helper function of getID
def splitStuff(s):
    idStr = ""
    for i in s.split(","):
        if "'id':" in i:
            for char in i:
                if char in "0123456789":
                    idStr += char
    return int(idStr)

# uses getID
def weatherIDType(zipcode):
    num = getID(zipcode)
    if num < 300 and num >= 200:
        return "thunderstorm"
    elif num < 400 and num >= 300:
        return "drizzle"
    elif num < 600 and num >= 500: 
        return "rain"
    elif num <700 and num >= 600:
        return "snow"
    elif num == 800:
        return "clear"
    elif num < 900 and num > 800:
        return "cloudy"
    elif num == 962 or num == 961 or num == 902 or num == 906:
        return "DANGER"


# gets temp hi and low of the day from data
def getTempRange(zipcode):
    base_url = "http://api.openweathermap.org/data/2.5/weather?zip="
    options = {
    "zip": zipcode + ",us",
    "appid": APIKEY
    }
    data = getDataFromURL(base_url, options)
    return (data["main"]["temp_min"], data["main"]["temp_max"])

data = getDataFromURL(base_url, options)
weather = data["weather"]

