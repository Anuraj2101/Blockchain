import hashlib
import datetime
import uuid

class Wallet:

    def __init__(self, wallet_type):
        self.wallet_addr = hashlib.sha256(str(uuid.uuid4()).encode()).hexdigest()
        self.timestamp = datetime.datetime.now()
        self.balance = 1
        self.wallet_type = wallet_type
   
    def get_wallet_addr(self):
        return self.wallet_addr
    
    def get_balance(self):
        return self.balance

    def withdraw(self):
        withdraw_amount = 1
        if self.wallet_type != "Voter":
            return "This wallet cannot vote, it must be a voter type wallet"
        self.balance = self.balance - withdraw_amount
        return withdraw_amount

    def recieve(self, recieve_amount):
        if self.wallet_type != "Candidate":
            return "This wallet cannot recieve votes, it must be a candidate type wallet"
        self.balance = self.balance + recieve_amount

    
        