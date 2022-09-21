import requests
from os import environ as env
from dotenv import load_dotenv
import json


class ConfluenceAPI:

    def __init__(self):
        self.session = requests
        load_dotenv()

    def get_content(self, page_id):
        querystring = {"expand": "metadata.labels,childTypes.page,history.lastUpdated"}
        headers = {"Authorization": "Basic " + env['BASIC_AUTH_TOKEN']}
        url = f"{env['URL_ROOT']}rest/api/content/{page_id}"

        print(querystring)
        print(headers)
        print(url)

        response = self.session.get(url, headers=headers, params=querystring)
        return dict(json.loads(response.text))

    def get_children(self, space_id):
        querystring = {"expand": "metadata.labels,childTypes.page,history.lastUpdated"}
        headers = {"Authorization": "Basic " + env['BASIC_AUTH_TOKEN']}
        url = f"{env['URL_ROOT']}rest/api/content/{space_id}/child/page?type=page"

        print(querystring)
        print(headers)
        print(url)

        response = self.session.get(url, headers=headers, params=querystring)

        return dict(json.loads(response.text))['results']
        

