from datetime import datetime
from os import environ as env

from dotenv import load_dotenv

load_dotenv()


class ConfluenceResponse:
    def __init__(
        self,
        page_title,
        page_id,
        page_level,
        last_updated_user,
        last_updated_data,
        create_data,
        create_user,
        labels,
    ):
        self.page_title = page_title
        self.page_id = page_id
        self.page_level = page_level
        self.last_updated_user = last_updated_user
        self.last_updated_data = last_updated_data
        self.create_data = create_data
        self.create_user = create_user
        self.labels = labels

    def compare_dates(self, date):
        start_date = datetime.strptime(date.split("T")[0], "%Y-%m-%d")
        end_date = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")
        delta = end_date - start_date
        return delta

    def create_dict(self):
        return {
            "id": self.page_id,
            "page_title": self.page_title,
            "page_level": self.page_level,
            "last_updated_user": self.last_updated_user,
            "last_updated_date": self.last_updated_data,
            "days_from_last_update": self.compare_dates(self.last_updated_data),
            "days_from_creation": self.compare_dates(self.last_updated_data),
            "create_date": self.create_data,
            "create_user": self.create_user,
            "labels": self.labels,
            "color": "#FFFAE2",
            "page_link": f"{env['URL_ROOT']}/engineering/pages/{self.page_id}",
        }
