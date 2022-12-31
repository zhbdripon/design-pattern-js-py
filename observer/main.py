class Subscriber:
    def __init__(self, username) -> None:
        self.username = username

    def set_notification(self, notification):
        print(f"{self.username} got notified about: {notification}")

class Publisher:
    def __init__(self) -> None:
        self.subscribers = []

    def publish(self, notification):
        for subscriber in self.subscribers:
            subscriber.set_notification(notification)

    def add_subscriber(self, new_subscriber):
        self.subscribers.append(new_subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

class Netflix(Publisher):

    def __init__(self) -> None:
        super().__init__()
        self.series = []


    def add_series(self, new_series):
        self.series.append(new_series)
        self.publish(new_series)

if __name__ == "__main__":

    netflix = Netflix()
    subscriber_1 = Subscriber("redoan")
    subscriber_2 = Subscriber("ziaul")
    subscriber_3 = Subscriber("monjurul")
    subscriber_4 = Subscriber("yakin")

    netflix.add_subscriber(subscriber_1)
    netflix.add_subscriber(subscriber_3)
    netflix.add_subscriber(subscriber_4)

    netflix.add_series("Stranger things")
    
"""
output:
redoan got notified about: Stranger things
monjurul got notified about: Stranger things
yakin got notified about: Stranger things
"""




