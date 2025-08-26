from src.settings import Settings
from src.email.email_service import EmailService
from src.known_offers import KnownOffers

class NewOffersFinder:
    def __init__(self, settings: Settings, email_service: EmailService, known_offers: KnownOffers):
        self.settings = settings
        self.email_service = email_service
        self.known_offers = known_offers
        
    def run(self, data: list):
        new_offers = [offer for offer in data if offer.get('guid', '0') not in self.known_offers.get()]
        print(f"Found {len(new_offers)} new offers")
        for offer in new_offers:
            if self.email_service.send_email(offer):
                self.known_offers.add_offer(offer.get('guid', '0'))
        
        self.known_offers.save_new_offers()