from notification_factory import NotificationFactory

def notify_user(notification_type, message):
    factory = NotificationFactory()
    notification = factory.create_notification(notification_type)  # Factory creates the notification
    notification.send(message)


notify_user("email", "Your order has been shipped!")
notify_user("sms", "Your OTP is 123456")
notify_user("push", "You have a new friend request")
