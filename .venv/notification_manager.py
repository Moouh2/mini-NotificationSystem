class NotificationManager:
    _instance = None

    @staticmethod
    def get_instance():
        if NotificationManager._instance is None:
            NotificationManager._instance = NotificationManager()
        return NotificationManager._instance

    def send_notification(self, message, notifier):
        print(f"[NotificationManager] Envoi centralisé en cours...")
        notifier.send(message)