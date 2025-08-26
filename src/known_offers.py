import json

class KnownOffers:
    def __init__(self):
        self.src = 'src/known_offers.json'
        self.new_offers = []
        with open(self.src, "r", encoding="utf-8") as f:
            self.data = json.load(f)
    
    def get(self):
        return self.data

    def add_offer(self, id: str):
        self.new_offers.append(id)

    def save_new_offers(self):
        for offer in self.new_offers:
            self.data.append(offer)
        with open(self.src, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
