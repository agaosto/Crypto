from CoolCoinBlockChain import CoolCoinBlockChain
from CoolTransaction import CoolTransactionCMD
def main() -> None:
    blockchain = CoolCoinBlockChain()
    print("Starting chain")
    tr = CoolTransactionCMD
    tr.perform_transaction("Adam", "Ewa",blockchain)
    tr.perform_transaction("Ewa", "Adam",blockchain)
    tr.show_all_transactions(blockchain)
if __name__ == "__main__":
    main()