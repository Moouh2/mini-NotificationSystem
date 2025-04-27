from notification_manager import NotificationManager
from sms_adapter import SMSAdapter
from newsletter import Newsletter, Subscriber

# 1. Singleton (NotificationManager)
manager = NotificationManager.get_instance()

# 2. Adapter (SMSAdapter)
sms_adapter = SMSAdapter()

# 3. Observer (Newsletter + Subscriber)
newsletter = Newsletter()
subscriber1 = Subscriber()
newsletter.subscribe(subscriber1)

# Test 1 : Envoi via Singleton + Adapter
manager.send_notification("Hello via SMS !", sms_adapter)

# Test 2 : Notification via Observer
newsletter.notify_all("Nouvelle promo disponible !")
