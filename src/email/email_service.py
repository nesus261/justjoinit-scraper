import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.email.message_generator import MessageGenerator
from src.settings import Settings

class EmailService:
    def __init__(self, settings: Settings, message_generator: MessageGenerator):
        self.settings = settings
        self.message_generator = message_generator

    def send_email(self, offer: dict):
        print(f'Sending an email with an offer with a guid: {offer.get("guid", "0")}')
        subject, body = self.message_generator.message(offer)
        msg = MIMEMultipart()
        msg["From"] = self.settings.sender_email()
        msg["To"] = self.settings.receiver_email()
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "html"))

        try:
            with smtplib.SMTP(self.settings.smtp_server(), self.settings.smtp_port()) as server:
                server.starttls()
                server.login(self.settings.sender_email(), self.settings.email_password())
                # wysłanie wiadomości
                server.sendmail(self.settings.sender_email(), self.settings.receiver_email(), msg.as_string())
            print(f'Successfully sent email with offer with guid: {offer.get("guid", "0")} ✅')

        except Exception as e:
            print('An error occurred while sending the email: ', e)
            return False
        return True
        
