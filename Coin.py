class Coin:
    id = 0

    def increment_id():
        Coin.id += 1

    def get_coin_id():
        Coin.increment_id()
        return Coin.id-1
