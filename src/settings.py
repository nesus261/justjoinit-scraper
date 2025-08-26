from pyaml_env import parse_config

class Settings:
    def __init__(self):
        data = parse_config("settings.yaml")
        self.search_criteria_list = data.get('search_criteria_list', [])
        self.email = data.get('email_service', {})
        self.frequency_of_checking = data.get("frequency_of_checking_in_seconds", 1800)
        self.lang = data.get("language", "en")

    def language(self):
        return self.lang
    
    def frequency(self): 
        return self.frequency_of_checking

    def search_criteria(self):
        return self.search_criteria_list

    def smtp_server(self):
        return self.email.get('smtp_server')
    
    def smtp_port(self):
        return self.email.get('smtp_port')
        
    def sender_email(self):
        return self.email.get('sender_email')
        
    def email_password(self):
        return self.email.get('password')
    
    def receiver_email(self):
        return self.email.get('receiver_email')