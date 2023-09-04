import pandas as pd
from abc import ABC, abstractmethod

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_securuty = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    watermark = "The Real Estate Company"

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing the avaliable attribute"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is avaliable"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


class Ticket(ABC):
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}"""
        return content

    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    @staticmethod
    def convert(amount):
        return amount * 1.2


hotel1 = Hotel("188")
hotel2 = Hotel("134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(hotel2.watermark)

ticket = ReservationTicket("alexander levkin", hotel1)
print(ticket.the_customer_name)
print(ticket.generate())

converted = ReservationTicket.convert(100)
print(converted)


class DigitalTicket(Ticket):
    def generate(self):
        return "Digital ticket generated"

    def download(self):
        pass
