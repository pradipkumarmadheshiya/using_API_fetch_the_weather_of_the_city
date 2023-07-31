import requests

url="https://api.openweathermap.org/data/2.5/weather?q="
userInput=input("Enter the City Name: ")
apiKey="947f6a04c9ce2de25f27d713abb269d6"

completeUrl=url+userInput+"&appid="+apiKey
response=requests.get(completeUrl)

if response.json()["cod"]!=200:
    print("Invalid city")
else:
    cel=round((response.json()["main"]["temp"])-273.15,2)
    print("The Temperature in",userInput,"is",str(cel)+"°c")