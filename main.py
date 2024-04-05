from block import Block, Blockchain
from voter import Voter
from candidate import Candidate

if __name__ == "__main__":
    bc1 = Blockchain()
    voter1 = Voter("Sam")
    voter2 = Voter("Bob")
    cand1 = Candidate("Alice", "Democratic")
    print(type(cand1) == Candidate)
    vote = voter1.cast_vote(cand1)
    bc1.add_block(vote)
    bc1.get_chain()
    print(voter1.wallet.balance)