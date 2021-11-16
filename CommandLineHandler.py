from CoolTransaction import CoolTransactionCMD


class CommmandLineHandler:
    def __init__(self):
        self.printMenu()
        self.programLoop()

    def printMenu(self):
        print("[0] Exit")
        print("[1] Add transaction")
        print("[2] Show all transactions")
        print("[3] Exit and show all transactions")

    def programLoop(self):
        tr = CoolTransactionCMD
        blockchain = CoolCoinBlockChain()
        option = int(input("Enter your option: "))
        while option != 0:
            if option == 1:
                sender = (input("Enter sender: "))
                receiver = (input("Enter receiver: "))
                tr.perform_transaction(sender, receiver, blockchain)
            elif option == 2:
                tr.show_all_transactions(blockchain)
            elif option == 3:
                previous_block = blockchain.get_previous_block()
                last_hash = previous_block.calculate_hash()
                blockchain.construct_block(last_hash)
                tr.show_all_transactions(blockchain)
                break

            self.printMenu()
            option = int(input("Enter your option: "))
