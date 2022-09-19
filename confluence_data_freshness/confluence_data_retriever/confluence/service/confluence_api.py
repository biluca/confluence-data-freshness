import requests
from os import environ as env
from dotenv import load_dotenv
import json


class ConfluenceAPI:

    def __init__(self):
        self.session = requests
        load_dotenv()

    def get_content(self, space_id):
        querystring = {"expand": "metadata.labels,childTypes.page,history.lastUpdated"}
        headers = {"Authorization": "Basic " + env['BASIC_AUTH_TOKEN']}
        url = f"{env['URL_ROOT']}rest/api/content/{space_id}"

        print(querystring)
        print(headers)
        print(url)

        response = self.session.get(url, headers=headers, params=querystring)
        return str(response.text)

    def get_child(self, space_id):
        querystring = {"expand": "metadata.labels,childTypes.page,history.lastUpdated"}
        headers = {"Authorization": "Basic " + env['BASIC_AUTH_TOKEN']}
        url = f"{env['URL_ROOT']}rest/api/content/{space_id}/child/page?type=page"

        print(querystring)
        print(headers)
        print(url)

        
        #s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
        #json_acceptable_string = s.replace("'", "\"")

        response = self.session.get(url, headers=headers, params=querystring)
        json_response = json.loads(response.text)
        return json_response
        

