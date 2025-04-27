# Service SMS externe (interface incompatible)
class SMSService:
    def send_sms(self, text):
        print(f"[SMSService] SMS envoyé : '{text}'")

# Adapter pour rendre SMSService compatible
class SMSAdapter:
    def __init__(self):
        self.sms_service = SMSService()

    def send(self, message):
        self.sms_service.send_sms(message)