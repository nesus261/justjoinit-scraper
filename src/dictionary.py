import json

class Dictionary:
    def __init__(self, lang: str):
        with open(f"./src/dictionaries/{lang}.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def job_offer(self):
        return self.data.get("job_offer")

    def offer(self):
        return self.data.get("offer")
    
    def company(self):
        return self.data.get("company")

    def url(self):
        return self.data.get("url")
    
    def working_mode(self):
        return self.data.get("working_mode")

    def working_time(self):
        return self.data.get("working_time")

    def experience_level(self):
        return self.data.get("experience_level")

    def remote_interview(self):
        return self.data.get("remote_interview")
    
    def location(self):
        return self.data.get("location")
    
    def required_skills(self):
        return self.data.get("required_skills")
    
    def nice_to_have_skills(self):
        return self.data.get("nice_to_have_skills")
    
    def languages(self):
        return self.data.get("languages")
    
    def earnings(self):
        return self.data.get("earnings")
    
    def multilocation(self):
        return self.data.get("multilocation")

    def yes(self):
        return self.data.get("yes")
    
    def no(self):
        return self.data.get("no")