from CoolCoinBlockChain import CoolCoinBlockChain
from CoolTransaction import CoolTransactionCMD


class CommmandLineHandler:
    def __init__(self):
        self.printMenu()
        self.programLoop()

    def printMenu(self):
        print("[0] Exit")
        print("[1] Add transaction")
        print("[2] Show all transactions")

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

            self.printMenu()
            option = int(input("Enter your option: "))
