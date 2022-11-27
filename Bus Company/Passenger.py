from Login import Login
from tabulate import *
class Passenger:
    def __init__(self):
        pass
        
    def options(self):
        # Ask user if they want to book or make Payment
        # Use Tabulate to display booking and payment options
        print(tabulate([["1.Booking"], ["2.Payment"], ["3.Exit"]], headers=["Services"]))
        option = int(input("Enter your option: "))
       
        if option == 1:
            self.bookTicket()
            
        elif option == 2:
            self.makePayment()
            
            
    def bookTicket(self):
        # Booking Options
        # Use Tabulate to display the options
        print(tabulate([["1. Booking Status "], ["2. Bus Booking "], ["3.Booking Payment "], ["4.Booking Status"],["5.LogOut"]], headers=["Options"]))
        
        MainChoice = int(input("Enter your option: "))
        if MainChoice == 1:
            self.bookingStatus()
            
        elif MainChoice == 2:
            print("................Bus Booking section..............")
            # Ask the User to enter the Number of Seats being booked
            # Bus type
            print("*"*50)
            #Use Tabulate to display the Bus Types
            print(tabulate([["1.Luxury Bus "], ["2.Ordinary"]], headers=["Bus Types"]))
            self.BusType = int(input("Enter your option: "))
            if self.BusType == 1:
                self.Luxury=50000
                self.NumberOfSeats = int(input("Enter the number of seats: "))
                while self.NumberOfSeats > 60:
                    print("The number of seats should not exceed 60")
                    self.NumberOfSeats = int(input("Enter the number of seats: "))
                    
                else:
                    self.Total = self.Luxury * self.NumberOfSeats
                    print("The total amount is: ", self.Total)
                    # Generate Receipt Number baing on the Steps
                    print(f"Receipt:L{MainChoice}{self.BusType}")
                    print("*"*50)
                    
                    # Ordinary Bus
            elif self.BusType == 2:
                self.Ordinary=25000
                self.NumberOfSeats = int(input("Enter the number of seats: "))
                while self.NumberOfSeats > 60:
                    print("Sorry, you can only book 60 seats")
                    self.NumberOfSeats = int(input("Enter the number of seats: "))
                    
                else:
                    self.Total = self.Ordinary * self.NumberOfSeats
                    print("The total amount is: ", self.Total)
                    # Generate Receipt Number basing
                    print(f"Receipt:L{MainChoice}{self.BusType}")
                    print("*"*50)
                    
                    # Payment
                    print("Do you want to proceed with payment?")
                    entry=input("Enter Yes or No: ")
                    if entry=="Yes":
                        print("..............Booking Payment.............")
                        ReceiptNumber=str(input("Enter the ReceiptNumber: "))
                        Amount=int(input("Enter the Amount Paid: "))
                        
                        if Amount < self.Total:
                            Balance=Amount-self.Total
                            print(f"Balance: {Balance}")
                            
                            print("Please Enter Amont >= to your Total Bill:    ")
                            Amount=int(input("Enter the Amount Paid: "))
                            
                        elif Amount > self.Total:
                            self.Change=Amount-self.Total
                            print(f"Change: {self.Change}")
                            
                
                
                
        elif MainChoice==4:
            print("Booking Reports: ")
            
        
        elif MainChoice==5:
            exit()
            
        else :
            print("Invalid Entry")
            self.bookTicket()
                
    # def Welcome(self):
                
            
                    
                