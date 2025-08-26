
from src.settings import Settings
from src.scraper import Scraper
from src.new_offers_finder import NewOffersFinder
from src.email.email_service import EmailService
from src.known_offers import KnownOffers
from src.dictionary import Dictionary
from src.email.message_generator import MessageGenerator
from dotenv import load_dotenv
import time
from datetime import datetime

class Main:
    def main(self):
        load_dotenv('.env')
        settings = Settings()
        dictionary = Dictionary(settings.language())
        while True:
            print(f"Checking new offers... {datetime.now()}")
            data = Scraper().run(settings.search_criteria())
            NewOffersFinder(
                settings, 
                EmailService(settings, MessageGenerator(dictionary)), 
                KnownOffers()
            ).run(data)
            print(f"Task done, I wait {settings.frequency()} seconds")
            time.sleep(settings.frequency())
Main().main()
