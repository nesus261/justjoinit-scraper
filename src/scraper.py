import requests
import urllib

class Scraper:
    default_search_criteria = {
        'currency': 'pln',
        'from': 0,
        'itemsCount': 100,
        'orderBy': 'DESC'
    }
    
    def run(self, search_criteria_list: list):
        data = []
        for search_criteria in search_criteria_list:
            merged_criteria = {**self.default_search_criteria, **search_criteria}
            
            new_data, next_cursor, next_count = self.send_req(merged_criteria)
            data += new_data
            while next_cursor is not None:
                merged_criteria['from'] = next_cursor
                merged_criteria['itemsCount'] = next_count
                new_data, next_cursor, next_count = self.send_req(merged_criteria)
                data += new_data

        return data

    def send_req(self, criteria: dict):
        params = urllib.parse.urlencode(criteria, doseq=True)
        req = requests.get(f'https://api.justjoin.it/v2/user-panel/offers/by-cursor?{params}')
        response = req.json()
        data = response.get('data', [])
        next_criteria = response.get('meta', {}).get('next', {})
        next_cursor = next_criteria.get('cursor')
        next_count = next_criteria.get('itemsCount')
        return data, next_cursor, next_count
    

