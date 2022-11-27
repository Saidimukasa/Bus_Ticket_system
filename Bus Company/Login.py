from tabulate import *
from abc import ABC, abstractmethod
class Login(ABC):
    def __init__(self, Username, email, Password):
        self.Username = Username
        self.email = email
        self.Password = Password
    @abstractmethod
    def Option(self):
        pass
    @abstractmethod
    def CustomerLogin(self):
        pass
    @abstractmethod
    def AdminLogin(self):
        pass
    @abstractmethod
    def Help(self):
        pass
    @abstractmethod
    def Exit(self):
        pass
    
    