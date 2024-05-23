import sqlite3
import random
import string
from fpdf import FPDF

class User:
    """Represents a User that buys a cinema seat"""
    # costructor
    def __init__(self, name):
        self.name = name
        
    def buy(self, seat, card):
        """Buys the seat if the card is valid """
        if seat.is_free() == True:
            if card.validate(seat.get_price()):
                seat.occupy()
                # generate pdf ticket here
                ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
                ticket.to_pdf()
                return "purchase was succesful!!!"
            else:
                return "there was a problem with your card"
        else:
            return "Seat is Taken!!!"
    
class Seat:
    """Represents a cinema seat that can be purchased by a user"""
    database = 'cinema.db'
    
    # constructor
    def __init__(self, seat_id):
        self.seat_id = seat_id
        
    # method to get price of the seat from the db
    def get_price(self):  
        """Get the price of a certain seat from the DB"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT price FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat_id])
        price = cursor.fetchall()[0][0] # [(1000,)]
        return price
    # a method to check if a seat is free
    def is_free(self):
        """Checks in the db if a seat is taken(free) or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT taken  FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat_id])
        result = cursor.fetchall()[0][0] # 1 for taken or 0 for not taken
        
        if result == 0:
            return True 
        else:
            return False
        
    # a method to occupy a seat if it is free
    def occupy(self):
        """Changes the value of taken in the DB from 0 to 1 if seat is free"""
        if self.is_free():
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            query = "UPDATE seats SET taken = ? WHERE seat_id = ?"
            cursor.execute(query, [1, self.seat_id])
            connection.commit()
            connection.close()
class Card(object):
    """Represents a bank card neede to finalize a seat purchase"""

    database = 'cinema.db'
    
    # constructor
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
    def validate(self, price):
        """Checks if card is  valid and has balance, substract price of thr seat from card balance"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT balance FROM card WHERE number = ? AND cvc = ?"
        cursor.execute(query, [self.number, self.cvc])
        result = cursor.fetchall() #[(2000,)]
        
        if result:
            balance = result[0][0]
            if balance >= price:
                query = "UPDATE card  SET balance = ? WHERE number = ? AND cvc = ?"
                cursor.execute(query, [(balance - price), self.number, self.cvc])
                connection.commit()
                connection.close()
                return True
                
   
class Ticket:
    """Represents a cinema ticket purchased by a user"""
    
    # constructor
    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number
        self.id = "".join([random.choice(string.ascii_uppercase) for i in range(10)])
        
        # a method to generate the pdf
    def to_pdf(self):
        """Creates a pdf Ticket"""
        pdf = FPDF(orientation='p', unit='pt', format='A4')
        pdf.add_page()
        
        # create the ticket title 
        pdf.set_font('Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt='CPL Digital Cinema Ticket', border=1, ln=1, align='C')
        
        
        # CREATE THE USER NAME CELL
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Name:', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        
        # create tickt id cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Ticket ID:', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        
        # Create the price cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Ticket Price:', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=f"{self.price}", border=1, ln=1)
        
        # create the seat number cell
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt='Seat Number:', border=1)
        pdf.set_font('Times', style='B', size=14)
        pdf.cell(w=0, h=25, txt=self.seat_number, border=1, ln=1)
        
        # outpu the pdf ticket 
        pdf.output(f"{self.user.name}_{self.id}_{self.seat_number}.pdf")
        
    
    
    # RUN APP HERE 
if __name__ == '__main__':
    name = input('Enter your full names: ')
    seat_id = input('Preffered seat: ')
    card_type = input('Your card type: ')
    card_number = input('Your card number: ')
    card_cvc = input('Your card cvc: ')
    card_holder = input('card holder name: ')
       
       
    # CREATE OBJECT HERE
    user = User(name)
    seat = Seat(seat_id)
    card = Card(card_type, card_number, card_cvc, card_holder)
    
    # BUY THE SEAT
    print(user.buy(seat, card))