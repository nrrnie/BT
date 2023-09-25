import hashlib
import time

class Block:
    def __init__(self, previous_hash, transactions):
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = None
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
        def merkle_tree(transactions):
            if len(transactions) == 1:
                return transactions[0]
            new_tr = []

            for i in range(0, len(transactions) -1, 2):
                combination = transactions[i] + transactions[i + 1]
                new_tr.append(hashlib.sha256(combination.encode()).hexdigest())

            if len(transactions) % 2 == 1:
                new_tr.append(transactions[-1])
            return merkle_tree(new_tr)
        return merkle_tree(self.transactions)
        
