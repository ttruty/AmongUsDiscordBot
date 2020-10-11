import os
import random
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint


GIPHY_KEY = os.environ['GIPHY_KEY']

# Create an instance of the API class
api_instance = giphy_client.DefaultApi()
config = {
    'api_key': GIPHY_KEY,  # Giphy API Key,
    'limit': 20,
    'rating': 'r'
}

def get_gif(message):
    try:
        api_response = api_instance.gifs_search_get(config['api_key'], limit=config['limit'], rating=config['rating'],
                                                    q=message)
        lst = list(api_response.data)
        gif = random.choices(lst)
        return gif[0].url

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_trending_get: %s\n" % e)

