# Observer (Abonné)
class Subscriber:
    def update(self, message):
        print(f"[Subscriber] Reçu : '{message}'")

# Observable (Newsletter)
class Newsletter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_all(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)