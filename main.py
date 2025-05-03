from notification_manager import NotificationManager
from sms_adapter import SMSAdapter
from Newsletter import Newsletter, Subscriber

# 1. Singleton - Gestionnaire central
manager = NotificationManager.get_instance()

# 2. Adapter - Service SMS
sms_adapter = SMSAdapter()

# 3. Observer - Newsletter et Abonnés
Newsletter = Newsletter()

# Boucle interactive
while True:
    print("\n=== Menu ===")
    print("1. Envoyer une notification SMS")
    print("2. S'abonner à la newsletter")
    print("3. Envoyer une newsletter")
    print("4. Quitter")
    choix = input("Choix : ")

    if choix == "1":
        message = input("Message SMS à envoyer : ")
        manager.send_notification(message, sms_adapter)  # Singleton + Adapter

    elif choix == "2":
        user_name = input("Nom de l'utilisateur : ")
        new_user = Subscriber(user_name)
        Newsletter.subscribe(new_user)
        print(f"{user_name} abonné(e) !")

    elif choix == "3":
        message = input("Message de la newsletter : ")
        N1ewsletter.notify_all(message)  # Observer

    elif choix == "4":
        break

    else:
        print("Option invalide.")
