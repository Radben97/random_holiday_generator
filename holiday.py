from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def Get_Holiday(country = "India"):
    request_url = f"https://api.api-ninjas.com/v1/holidays?country={country}"
    response = requests.get(request_url, headers={'X-Api-Key': os.getenv("API_KEY")}).json()
    return response

if __name__ == "__main__":
    print("\n****Get the holidays of your country****\n")
    country = input("Enter a country: ")
    if not country:
        country = "India"
    holiday_data = Get_Holiday(country)
    print("\n")
    pprint(holiday_data)