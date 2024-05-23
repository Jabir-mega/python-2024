import sqlite3
import random
import string
# from fpdf import FPDF
class user:
    """e a User that buys a cinema seat"""
    
class seat:
    """Represents a cinema seat that can be purchased by a user"""
    database = 'cinema.db'
    
    # constructor
    def __init__(self, seat_id):
        self.sseat_id = seat_id
        
    # method to get price of the seat from the db
    def get_price(self):
        """Get the price of a certain seat from the DB"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT price FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat-id])
        price = cursor.fetchall()[0][0] # [(1000,)]
        return price
    # a method to check if a seat is free
    def is_free(self):
        """Checks in the db if a seat is taken(free) or not"""
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        query = "SELECT price FROM seats WHERE seat_id = ?"
        cursor.execute(query, [self.seat-id])
        price = cursor.fetchall()[0][0] # [(1000,)]
        cursor.execute(query, [self.seat-id])
        result = cursor.fetchall()[0][0] # 1 for taken or 0 for not taken
        
        if result == 0:
            return
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
class card:
    def validate(self, price):
       result = """ Represents a bank card needed to finalize a seat purchase"""#cursor.fetchall() # [(2000,)]
    database = 'cinema.db'
    
    # constructor
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        
        
        
        
    def buy(self, seat, card):