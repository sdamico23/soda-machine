#Lab #5
#Due Date: 02/08/2019, 11:59PM
########################################
#                                      
# Name: Stephen D'Amico 
# Collaboration Statement: I worked alone on this assignment.          
#
########################################


class SodaMachine:
    '''
        >>> m = SodaMachine('Coke', 10)
        >>> m.purchase()
        'Product out of stock'
        >>> m.restock(2)
        'Current soda stock: 2'
        >>> m.purchase()
        'Please deposit $10'
        >>> m.deposit(7)
        'Balance: $7'
        >>> m.purchase()
        'Please deposit $3'
        >>> m.deposit(5)
        'Balance: $12'
        >>> m.purchase()
        'Coke dispensed, take your $2'
        >>> m.deposit(10)
        'Balance: $10'
        >>> m.purchase()
        'Coke dispensed'
        >>> m.deposit(15)
        'Sorry, out of stock. Take your $15 back'
    '''
    def __init__(self, product, price):
    #-- start code here ---
        self.product = product
        self.price = price
        self.balance = 0
        self.stock = 0




    def purchase(self):
    #-- start code here ---
        change = 0
        if self.stock <=0: 
            return "Product out of stock"
        if self.balance<self.price:
            return "Please deposit ${}".format(self.price-self.balance)
        elif self.balance>self.price:
            self.stock -= 1
            change = self.balance-self.price
            self.balance = 0
            return "{} dispensed, take your ${}".format(self.product,change)
        elif self.balance == self.price:
            self.stock -= 1
            return "{} dispensed".format(self.product)
        else: 
            return "{} dispensed".format(self.product)

    def deposit(self, amount):

        if self.stock == 0:
            return "Sorry, out of stock. Take your ${} back".format(amount)
        else: 
            self.balance += amount
            return "Balance: ${}".format(self.balance)


    def restock(self, amount):
    #-- start code here ---
        self.stock += amount
        return "Current soda stock: {}".format(self.stock)
    

class Line:
    ''' 
        Creates objects of the class Line, takes 2 tuples. Class must have 2 PROPERTY methods
        >>> line1=Line((-7,-9),(1,5.6))
        >>> line1.distance
        16.648
        >>> line1.slope
        1.825
        >>> line2=Line((2,6),(2,3))
        >>> line2.distance
        3.0
        >>> line2.slope
        'Infinity'
    '''


    def __init__(self, coord1, coord2):
    #-- start code here ---
        self.pt1 = coord1
        self.pt2 = coord2

    

    @property
    def distance(self):
    #-- start code here ---
        return round(((self.pt2[1]-self.pt1[1])**2 + (self.pt2[0]-self.pt1[0])**2)**0.5, 3)
    #-- ends here ---
    @property   
    def slope(self):
    #-- start code here ---
        try: 
            return round((self.pt2[1]-self.pt1[1])/ (self.pt2[0] -self.pt1[0]),3)
        except:
            return "Infinity"
    #-- ends here ---


