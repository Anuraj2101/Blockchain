import hashlib
import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()).hexdigest()

    def get_info(self):
        return {"Index": self.index, "Timestamp": self.timestamp, "Data": self.data, "Previous Hash": self.previous_hash, "Hash": self.hash}

class Blockchain:
    def __init__(self, voters, candidates):
        self.chain = [self.create_genesis_block()]
        self.stakeholders = {"Voters": voters, "Candidates": candidates}
    
    def create_genesis_block(self):
        voter_data = {}
        return Block(0, voter_data, "0")

    def get_latest_block(self):
        return self.chain[-1]
    
    #Only adds block if vote has been cast, i.e token has been staked    
    def add_block(self, data):
        Staked = False
        if data.startswith("1 vote token transferred"):
            Staked = True
        else:
            Staked = False
            print("Cannot append block if vote has not been cast.")
        if Staked:
            self.chain.append(Block(len(self.chain), data, self.get_latest_block().hash))

    def get_chain(self):
        for block in self.chain:
            print(block.get_info())
    
