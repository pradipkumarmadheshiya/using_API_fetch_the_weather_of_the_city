import requests
url="https://api.openweathermap.org/data/2.5/weather?q="
userInput=input("Enter the City Name: ")
city=userInput
apiKey="947f6a04c9ce2de25f27d713abb269d6"
completeUrl=url+userInput+"&appid="+apiKey
response=requests.get(completeUrl)
data=response.json()
c=round((data["main"]["temp"])-273.15,2)
print("The Temperature in",city,"is",str(c)+"°c")