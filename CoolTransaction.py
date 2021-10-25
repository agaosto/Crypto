from CoolTransactionInterface import CoolTransactionInterface
from CoolCoinBlockChain import CoolCoinBlockChain

class CoolTransactionCMD(CoolTransactionInterface):
    def perform_transaction(sender:str,recipent:str, block_chain:CoolCoinBlockChain) -> None:
        #get previous block
        previous_block = block_chain.get_previous_block()
        #add new data to transaction
        block_chain.add_new_data(
            sender=sender,  
            recipient=recipent,  
        )
        last_hash = previous_block.calculate_hash()
        #create block
        block = block_chain.construct_block(last_hash)
        #verify if transaction is okey
        if(CoolCoinBlockChain.check_validity(block, previous_block)):
            print("Transaction is Valid,  Saved!")
        else:
            print("Invalid trasnaction, rollback?")
        pass

    def show_last_transaction() -> None:
        pass

    def show_all_transactions(block_chain:CoolCoinBlockChain) -> None:
        print(block_chain.chain)
        pass