from block import Block
from blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some transactions and blocks
    block1 = Block(blockchain.get_latest_block().hash, ["Transaction 1", "Transaction 2"])
    blockchain.add_block(block1)

    block2 = Block(blockchain.get_latest_block().hash, ["Transaction 3", "Transaction 4"])
    blockchain.add_block(block2)

    # Check if the blockchain is valid
    print("Is blockchain valid?", blockchain.is_chain_valid())
