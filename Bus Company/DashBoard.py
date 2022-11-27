# DashBoard.py
from Login import Login
from Passenger import *
from tabulate import *
class DashBoard(Login,Passenger):
    def __init__(self, Username, email, Password):
        super().__init__(Username, email, Password)
        
    def Option(self):
        # Display  a welcome message
        print("Kaliita Bus Ticketing System") 
        # use tabulate to display the options
        print(tabulate([["1. Customer Login"], ["2. Admin Login"], ["3. Help"], ["4. Exit"]], headers=["Options"]))
        
        
        option = int(input("Enter your option: "))
        if option == 1:
            self.CustomerLogin()
            
        elif option == 2:
            self.AdminLogin()
            
        elif option == 3:
            self.Help()
            
        elif option == 4:
            self.Exit()       
    def CustomerLogin(self):
        print("**"*50)
        print("Customer Login")
        self.Username = input("Enter your Username: ")
        self.Password = input("Enter your Password: ")
        
        if self.Username == "Saidi" and self.Password == "Saidi":
            print("Welcome to the Customer Dashboard")
            print("."*50)
            passenger=Passenger()
            passenger.options()
            
        else:
            print("Invalid Username or Password")
            self.CustomerLogin()
            
            
    def AdminLogin(self):
        print("Admin Login")
        self.Username = input("Enter your Username: ")
        self.Password = input("Enter your Password: ")
        
        if self.Username == "Admin" and self.Password == "Admin":
            print("Welcome to the Admin Dashboard")
            # passenger.Passenger()
            
        else:
            print("Invalid Username or Password")
            self.AdminLogin()
            
    def Help(self):
        print("Help Information")
        # Display Help Information
        print("Contact the Admin")
        
    def Exit(self):
        print("Thank you for using this system")
        exit()
        


    