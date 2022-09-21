from .model.response import ConfluenceResponse
from .service.confluence_api import ConfluenceAPI


class Extractor:
    def __init__(self) -> None:
        self.all_pages = []
        self.confluence_api = ConfluenceAPI()

    def append_hub_page(self, page_id, level):
        content = self.confluence_api.get_content(page_id)

        if content is None:
            return
        elif content.get("type") == "page":
            return self.extract_itens(content, level)
        return

    def append_children_pages(self, page_id, level):
        children = self.confluence_api.get_children(page_id)

        if children is None:
            return
        for child in children:
            if child.get("type") == "page":
                self.extract_itens(child, level)
                self.append_children_pages(child["id"], level)

        return
    
    def extract_labels(self, result_labels):
        labels = []

        for label in result_labels:
            labels.append(label['label'])

        return labels

    def extract_itens(self, item, level):

        docs = ConfluenceResponse(
            page_title=item["title"],
            page_level=level,
            create_data=item["history"]["createdDate"],
            last_updated_data=item["history"]["lastUpdated"]["when"],
            last_updated_user=item["history"]["createdBy"]["publicName"],
            page_id=item.get("id"),
            create_user=item["history"]["createdBy"]["publicName"],
            labels=self.extract_labels(item["metadata"]["labels"]["results"]),
        )
        
        #I NEED TO IMPLEMENT THE SKIP LABELS LOGIC!

        return self.all_pages.append(docs.create_dict())

    def get_all_pages(self):
        return self.all_pages
    



