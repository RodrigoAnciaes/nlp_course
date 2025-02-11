import requests
import dotenv
import os

# load the GEMINI_API_KEY from the .env file
dotenv.load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# set the headers for the request
headers = {
    'Content-Type': 'application/json',
    'X-GEMINI-APIKEY': GEMINI_API_KEY,
    'X-GEMINI-PAYLOAD': '',
    'X-GEMINI-SIGNATURE': ''
}

# make the request to the Gemini API
response = requests.get('https://api.gemini.com/v1/symbols', headers=headers)

# print the response

print(response.json())
