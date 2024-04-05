from block import Block, Blockchain
from voter import Voter
from candidate import Candidate

if __name__ == "__main__":
    bc1 = Blockchain()
    voter1 = Voter("Sam")
    voter2 = Voter("Bob")
    cand1 = Candidate("Alice", "Democratic")
    print(type(cand1) == Candidate)
    print("Voter Balance", voter1.wallet.get_balance())
    print("Candidate Balance", cand1.wallet.get_balance())
    vote = voter1.cast_vote(cand1)
    print("Voter Balance", voter1.wallet.get_balance())
    print("Candidate Balance", cand1.wallet.get_balance())
    bc1.add_block(vote)
    print(bc1.get_chain())
    