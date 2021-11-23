class CoolTransactionInterface:
    def perform_transaction(sender: str, recipient: str) -> None:
        pass

    def show_last_transaction() -> None:
        pass

    def show_all_transactions() -> None:
        pass
