import requests
import os
from dotenv import load_dotenv

muscle_query = []

general_api_url = "https://api.api-ninjas.com/v1/exercises"
load_dotenv()
api_key = os.getenv("FITNESS_API_KEY")

# response = requests.get(general_api_url, headers={'X-Api-Key': 'API KEY'}) #last number is 5
# if response.status_code != 200:
#     print("UNSUCCESSFULL API Launch")

def search_by_muscle(muscle):
    api_url = general_api_url + f"?muscle={muscle}"
    response = requests.get(api_url,headers={'X-Api-Key': api_key})
    json = response.json() #keys: name, type, muscle, equipment, difficulty, instructions
    if len(json) == 0: #If there is nothing returned, search was unsuccessful
        print("Nothing found...Error")
        return -1
    return json

def search_by_name(name):
    api_url = general_api_url + f"?name={name}"
    response = requests.get(api_url,headers={'X-Api-Key': api_key})
    json = response.json() #keys: name, type, muscle, equipment, difficulty, instructions
    if len(json) == 0:
        print("Nothing found...Error")
        return -1
    return json


if __name__ == "__main__":
    search_by_name('hammer') #Testing the input
    print(api_key)







