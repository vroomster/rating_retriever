from .client import Client
from .header import Header
from .github_obj.search_results import SearchResults
#from requests import Request, Session

#session = Session()

#session.headers.update(headers)
#params = {"orderMethod":"pickup", "location":"POINT(-121.42600251 37.73958206)", "pageSize":"100"}
#&locationMode=PICKUP
#facetSet=umamiV2
#pageSize=20
#hideHateos=true
#searchMetrics=true

#geohash=9q9wsyk2cpfp&facet=open_now%3Atrue&radius=5&includeOffers=true&sortSetId=umamiv3&sponsoredSize=3&countOmittingTimes=true&pageNum=1&searchId=34aa530c-eeff-11ea-8a71-4fb827cbe562
#response = session.get("https://api-gtm.grubhub.com/restaurants/search/search_listing", params=params)
#print("Response status code: {}".format(response.status_code))
#print(response.json())

class GrubhubApiClient:

    def __init__(self, api_key):
        #headers = {"Authorization": "Bearer {}".format(""), 'Content-Type': 'application/json'}
        self.api_client = Client(header=Header(api_key=api_key, add_content_type_json=True))

    def get_restaurants(self, longitude, latitude, page_size=100, page_number=1):
        api_url = "https://api-gtm.grubhub.com/restaurants/search/search_listing"
        #"orderMethod":"pickup"

        params = {"location":"POINT({} {})".format(longitude, latitude), "pageSize":str(page_size), "pageNum":str(page_number),
        "orderMethod": "pickup", "radius":"10", "locationMode": "PICKUP"}

#facetSet: umamiV2
#pageSize: 20
#hideHateos: true
#searchMetrics: true
#preciseLocation: true
#geohash: 9q9wfdbrbtnu

#includeOffers: true
#sortSetId: umamiv3
#sponsoredSize: 3
#countOmittingTimes: true}

        response = self.api_client.make_get_request(url=api_url, params=params)
        #print(response.json())
        search_results = SearchResults(response.json())
        #print(search_results)
        return search_results



# orderMethod=pickup&locationMode=PICKUP&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&location=POINT(-121.83073426%2037.67948913)&preciseLocation=true&geohash=9q9q7emdfju7&facet=open_now%3Atrue&radius=5&includeOffers=true&sortSetId=umamiv3&sponsoredSize=3&countOmittingTimes=true
#        orderMethod=delivery&locationMode=DELIVERY&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&location=POINT(-121.83073426%2037.67948913)&preciseLocation=true&geohash=9q9q7emdfju7&facet=open_now%3Atrue&includeOffers=true&sortSetId=umamiv3&sponsoredSize=3&countOmittingTimes=true&pageNum=2&searchId=71e0b0a9-efae-11ea-be1d-572d001b2f42"
