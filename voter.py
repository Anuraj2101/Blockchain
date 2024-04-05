from wallet import Wallet
# from transact import Transact
from candidate import Candidate

class Voter:
    
    def __init__(self, name, verification_status=True):
        self.name = name
        self.wallet = Wallet("Voter")
        self.verification_status = verification_status

    def get_voter_info(self):
        return {"Name": self.name, "Wallet Address": self.wallet.get_wallet_addr(), "Verification Status": self.verification_status}
    
    def cast_vote(self, candidate: Candidate):
        if type(candidate) != Candidate:
            return "Can only cast vote to candidate..."
        if self.wallet.get_balance() <= 0 or self.wallet.get_balance() > 1:
            return "Invalid wallet balance: Vote has already been cast or wallet balance exceeds 1"
        elif self.verification_status != True:
            return "Unverified Voter... Reject vote"
        else:
            candidate.wallet.recieve(self.wallet.withdraw())
            return f"1 vote token transferred to {candidate.get_info()} from {self.get_voter_info()}"