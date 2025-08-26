# JUSTJOINIT-SCRAPER
## What is this?

Justjoinit-scraper is a simple Python program used to search for new job offers on the popular justjoin.it platform that match your criteria and send them to your email. You can set the frequency of job searches and run the program on any Python-enabled server to regularly receive notifications of new job offers that meet your criteria.


## How to run? 

Install git: https://git-scm.com/downloads  
Install python and pip: https://www.python.org/downloads/  
Run the commands below:
```sh
git clone https://github.com/nesus261/justjoinit-scraper.git
cd justjoinit-scraper
```

Create an .env file based on .env-example.
```sh
EMAIL_SENDER=email address to send notification
EMAIL_SENDER_PASSWORD=application password - look here: https://support.google.com/accounts/answer/185833?hl=pl
EMAIL_RECEIVER=email address to notify
```
Set the settings.yaml file to suit your needs.
```yaml
language: pl
frequency_of_checking_in_seconds: 1800
email_service:
  smtp_server: smtp.gmail.com
  smtp_port: 587
  sender_email: !ENV ${EMAIL_SENDER}
  password: !ENV ${EMAIL_PASSWORD}
  receiver_email: !ENV ${EMAIL_RECEIVER}
search_criteria_list: 
  - remoteWorkOptions[]: 
    - remote
    sortBy: published
    employmentTypes[]: 
    - internship
    experienceLevels[]:
    - junior
```
Install the dependencies and run the program.
```sh
pip install -r requirements.txt
python main.py
```
