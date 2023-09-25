import hashlib
import time

class Block:
    def __init__(self, previous_hash, transactions):
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.compute_merkle_root()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.previous_hash) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)

    def compute_merkle_root(self):
        def merkle_tree(txns):
            if len(txns) == 1:
                return txns[0]
            new_txns = []
            for i in range(0, len(txns) - 1, 2):
                combined = txns[i] + txns[i + 1]
                new_txns.append(hashlib.sha256(combined.encode()).hexdigest())
            if len(txns) % 2 == 1:
                new_txns.append(txns[-1])
            return merkle_tree(new_txns)

        return merkle_tree(self.transactions)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block("0", ["Genesis Transaction"])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            # Verify Merkle root
            if current_block.merkle_root != current_block.compute_merkle_root():
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some transactions and blocks
    block1 = Block(blockchain.get_latest_block().hash, ["Transaction 1", "Transaction 2"])
    blockchain.add_block(block1)

    block2 = Block(blockchain.get_latest_block().hash, ["Transaction 3", "Transaction 4"])
    blockchain.add_block(block2)

    # Check if the blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())
import hashlib
import time

class Block:
    def __init__(self, previous_hash, transactions):
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = self.compute_merkle_root()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.timestamp) + str(self.previous_hash) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)

    def compute_merkle_root(self):
        def merkle_tree(txns):
            if len(txns) == 1:
                return txns[0]
            new_txns = []
            for i in range(0, len(txns) - 1, 2):
                combined = txns[i] + txns[i + 1]
                new_txns.append(hashlib.sha256(combined.encode()).hexdigest())
            if len(txns) % 2 == 1:
                new_txns.append(txns[-1])
            return merkle_tree(new_txns)

        return merkle_tree(self.transactions)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block("0", ["Genesis Transaction"])

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

            # Verify Merkle root
            if current_block.merkle_root != current_block.compute_merkle_root():
                return False

        return True

if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some transactions and blocks
    block1 = Block(blockchain.get_latest_block().hash, ["Transaction 1", "Transaction 2"])
    blockchain.add_block(block1)

    block2 = Block(blockchain.get_latest_block().hash, ["Transaction 3", "Transaction 4"])
    blockchain.add_block(block2)

    # Check if the blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())
