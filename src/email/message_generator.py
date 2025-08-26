import json
from src.dictionary import Dictionary

class MessageGenerator:
    def __init__(self, dictionary: Dictionary): 
        self.dictionary = dictionary

    def message(self, offer: dict):
        title = offer.get('title')
        company_name = offer.get('companyName')
        city = offer.get('city')
        street = offer.get('street')
        multilocation = json.dumps(
            offer.get('multilocation'), 
            ensure_ascii=False, 
            indent=4
        )
        link = f'https://justjoin.it/job-offer/{offer.get("slug")}'
        workplace_type = offer.get('workplaceType')
        working_time = offer.get('workingTime')
        experience_level = offer.get('experienceLevel')
        remote_interview = self.dictionary.yes() if offer.get('remoteInterview') else self.dictionary.no()
        employment_types = json.dumps(
            offer.get('employmentTypes'), 
            ensure_ascii=False, 
            indent=4
        ) # zarobki 
        required_skills = json.dumps(
            offer.get('requiredSkills'), 
            ensure_ascii=False, 
            indent=4
        )
        nice_to_have_skills = json.dumps(
            offer.get('niceToHaveSkills'), 
            ensure_ascii=False, 
            indent=4
        )
        languages = json.dumps(
            offer.get('languages'), 
            ensure_ascii=False, 
            indent=4
        )
        subject = f'{self.dictionary.job_offer()}: {title}'
        body = f'\
        <html>\
            <body>\
            {self.dictionary.offer()}: {title}<br>\
            {self.dictionary.company()}: {company_name}<br>\
            {self.dictionary.url()}: {link}<br>\
            {self.dictionary.working_mode()}: {workplace_type}<br>\
            {self.dictionary.working_time()}: {working_time}<br>\
            {self.dictionary.experience_level()}: {experience_level}<br>\
            {self.dictionary.remote_interview()}: {remote_interview}<br>\
            {self.dictionary.location()}: {city} {street}<br>\
            {self.dictionary.required_skills()}: <pre>{required_skills}</pre><br>\
            {self.dictionary.nice_to_have_skills()}: <pre>{nice_to_have_skills}</pre><br>\
            {self.dictionary.languages()}: <pre>{languages}</pre><br>\
            {self.dictionary.earnings()}: <pre>{employment_types}</pre><br>\
            {self.dictionary.multilocation()}: <pre>{multilocation}</pre><br>\
            </body>\
        </html>'
        return subject, body
