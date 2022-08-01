from .client import Client
from .header import Header
from .yelp_obj.business_matches import BusinessMatches

class YelpApiClient:

    def __init__(self):
        """
        Client ID
        yQI_C5jXcgovEPWtApC-GA

        API Key
        OUN-zIE_FKUbK9jCHumKC94QnNcuLnGrctpSkcO-b1ge6vMdVxVhr1GXsTpeVL4WHL6SWiLrZD1b3Uphp9oFEYu4wH3N0mnnw21nC1DH4cZBbp_p5iKNPIRVKeM2X3Yx

        Business Match endpoint when you have precise info like name & address
        Business Search endpoint when you have general info on the biz like name & location but don't know the address
        Phone Search endpoint when you only have the phone number or less confident about other matching criteria
        """
        self.base_url = "https://api.yelp.com{}"
        self.api_url = ""
        api_key = "OUN-zIE_FKUbK9jCHumKC94QnNcuLnGrctpSkcO-b1ge6vMdVxVhr1GXsTpeVL4WHL6SWiLrZD1b3Uphp9oFEYu4wH3N0mnnw21nC1DH4cZBbp_p5iKNPIRVKeM2X3Yx"
        self.api_client = Client(header=Header(api_key=api_key, add_content_type_json=False))

    def search_by_business_id(self, business_id):
        self.api_url = self.base_url.format("/v3/businesses/{business_id}".format(business_id=business_id))
        response = self.api_client.make_get_request(url=self.api_url)
        print(response)

    def search_by_phone(self, phone):
        return BusinessMatches(self._make_api_get_call("/v3/businesses/search/phone", {"phone":phone}))

    def search(self):
        self.api_url = self.base_url.format("/v3/businesses/search")


    def search_matches(self, name, address1, city, state, country):
        return BusinessMatches(self._make_api_get_call("/v3/businesses/matches",
            {"name":name, "address1":address1, "city":city, "state":state, "country":country}))


    def _make_api_get_call(self, api_path, params):
        response = self.api_client.make_get_request(url=self.base_url.format(api_path), params=params)
        return response.json()


    def set_api_url(self, api_path):
        self.api_url = self.base_url.format(api_path)

# orderMethod=pickup&locationMode=PICKUP&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&location=POINT(-121.83073426%2037.67948913)&preciseLocation=true&geohash=9q9q7emdfju7&facet=open_now%3Atrue&radius=5&includeOffers=true&sortSetId=umamiv3&sponsoredSize=3&countOmittingTimes=true
#        orderMethod=delivery&locationMode=DELIVERY&facetSet=umamiV2&pageSize=20&hideHateos=true&searchMetrics=true&location=POINT(-121.83073426%2037.67948913)&preciseLocation=true&geohash=9q9q7emdfju7&facet=open_now%3Atrue&includeOffers=true&sortSetId=umamiv3&sponsoredSize=3&countOmittingTimes=true&pageNum=2&searchId=71e0b0a9-efae-11ea-be1d-572d001b2f42"
