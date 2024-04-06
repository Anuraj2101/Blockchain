import hashlib
import datetime
import random

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
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.stakeholders = {}
    
    def create_genesis_block(self):
        voter_data = {}
        return Block(0, voter_data, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        # new_block.previous_hash = self.get_latest_block().hash
        # new_block.hash = new_block.calculate_hash()
        self.chain.append(Block(len(self.chain), data, self.get_latest_block().hash))

    def get_chain(self):
        for block in self.chain:
            print(block.get_info())
    
    def proof_of_stake(self, wallet_address):
        if wallet_address in self.stakeholders:
            return self.stakeholders[wallet_address]
        else:
            return 0