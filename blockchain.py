import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, created_at, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.created_at = created_at
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_str = str(self.index) + self.previous_hash + str(self.created_at) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_str.encode()).hexdigest()

    def __getitem__(self):
        return self.hash

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the hash of the block is valid
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous_hash of the current block matches the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True




blockchain = Blockchain()
blockchain.add_block(Block(1, blockchain.get_latest_block().hash, int(time.time()), "Transaction 1"))
blockchain.add_block(Block(2, blockchain.get_latest_block().hash, int(time.time()), "Transaction 2"))

print(blockchain.get_latest_block)
print("Is blockchain valid?", blockchain.is_valid())
