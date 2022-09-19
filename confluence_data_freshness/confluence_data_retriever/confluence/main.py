from service.confluence_api import ConfluenceAPI

if __name__ == "__main__":
    confluence_api = ConfluenceAPI()
    response = confluence_api.get_content(981794872)