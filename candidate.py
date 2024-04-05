from wallet import Wallet

class Candidate:

    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.wallet = Wallet("Candidate")
    
    def get_info(self):
        return {"Candidate Name:": self.name, "Party": self.party, "Wallet": self.wallet.get_wallet_addr()}