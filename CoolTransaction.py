from CoolTransactionInterface import CoolTransactionInterface
from CoolCoinBlockChain import CoolCoinBlockChain


class CoolTransactionCMD(CoolTransactionInterface):
    def perform_transaction(sender: str, recipent: str, block_chain: CoolCoinBlockChain) -> None:
        previous_block = block_chain.get_previous_block()
        block_chain.add_new_data(
            sender=sender,
            recipient=recipent,
        )
        last_hash = previous_block.calculate_hash()
        block = block_chain.construct_block(last_hash)
        print("Checking if transaction is valid...")
        if(CoolCoinBlockChain.check_validity(block, previous_block)):
            print("Transaction is valid, saved!")
        else:
            print("Invalid transaction!")
        pass

    def show_last_transaction() -> None:
        pass

    def show_all_transactions(block_chain: CoolCoinBlockChain) -> None:
        print(block_chain.chain)
        pass
