class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Utilisateur notifié ({self.name}) : {message}")

class Newsletter:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)

    def notify_all(self, message):
        for user in self.subscribers:
            user.update(message)
