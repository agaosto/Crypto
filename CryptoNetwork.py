from Edge import Edge
from Node import Node
from Coin import Coin 
from User import TransactionData
from RewardData import RewardData
from CoinBlock import CoinBlock
import multiprocessing as mp
import random
class CryptoNetwork: ###do as a singleton
    def __init__(self) -> None:
        self.list_of_edges = []
        self.max_nonce = 2 ** 32 # 4 billion
    def add_edge(self, edge:Edge):
        self.list_of_edges.append(edge)
    def get_adjacent_nodes(self, node):
        adjacent_nodes = []
        for edge in self.list_of_edges:
            current_node = edge.get_node()
            if(current_node == node):
                adjacent_node = edge.get_connected_node(current_node)
                adjacent_nodes.append(adjacent_node)
        return adjacent_nodes
    def update_node(self, updated_node:Node):
        for edge in self.list_of_edges:
            if(edge.get_node()== updated_node):
                edge.set_node(updated_node)
            elif(edge.get_connected_node(edge.get_node()) == updated_node):
                edge.set_connected_node(updated_node)
    def get_node(self, name_of_user):
        for edge in self.list_of_edges:
            if(edge.get_node().user.name == name_of_user):
                return edge.get_node()
            elif(edge.get_connected_node(edge.get_node()).user.name == name_of_user):
                return edge.get_connected_node(edge.get_node())
    def get_all_nodes(self):
        starting_node = self.list_of_edges[0].get_node()
        queue = []
        visited = set()
        visited.add(starting_node)
        queue.append(starting_node)
        while len(queue)!=0:
            current_node=queue.pop()
            visited.add(current_node)
            for adjacent_node in self.get_adjacent_nodes(current_node):
                if(adjacent_node not in visited):
                    visited.add(adjacent_node)
                    queue.append(adjacent_node)
        return visited
    def initialize_genesis_data(self):
        coins=[]
        for node in self.get_all_nodes():
            coins.append(Coin.get_coin_id())
            self.send_reward(node, coins)
            self.update_node(node)
            coins=[]
    def broadcast_transaction_to_other_users_with_probability(self, starting_node, probability):     
        nodes_to_broadcast = self.get_all_nodes()
        nodes_to_broadcast.remove(starting_node)
        transaction_data = starting_node.get_pending_transaction()
        while len(nodes_to_broadcast)>0:
            current_node=nodes_to_broadcast.pop()
            if(random.randint(0, 10)>=probability):
                current_node.pending_transactions.append(transaction_data)
                self.update_node(current_node)
    def broadcast_reward_to_other_users(self, starting_node, reward_data):     
        nodes_to_broadcast = self.get_all_nodes()
        nodes_to_broadcast.remove(starting_node)
        while len(nodes_to_broadcast)>0:
            current_node=nodes_to_broadcast.pop()
            current_node=current_node.add_reward_to_pending(reward_data)
            self.update_node(current_node)
    def send_reward(self, winner:Node, coin:list):
        reward_data = RewardData(winner.user, coin)
        winner.add_reward_to_pending(reward_data)
        self.update_node(winner)
        self.broadcast_reward_to_other_users(winner, reward_data)
    def create_genesis_block(self):
        self.initialize_genesis_data()
        for node in self.get_all_nodes():
            data=[]
            transactions = node.pending_transactions
            for transaction in transactions:
                if(isinstance(transaction, TransactionData)):
                    data.append(transaction.get_json_of_transaction())
                elif(isinstance(transaction, RewardData)):
                    data.append(transaction.get_json_of_reward())
            coin_block = CoinBlock(0, data)
            node.blockchain.append(coin_block.get_json_of_block())
            node.clear_pending_transactions()
            self.update_node(node)
    def make_all_nodes_verify_pt(self):
        for node in self.get_all_nodes():
            if(not(node.validate_transaction())):
                return False
        return True
    def add_block(self):
        if(self.make_all_nodes_verify_pt()):
            for node in self.get_all_nodes():
                data=[]
                transactions = node.pending_transactions
                for transaction in transactions:
                    if(isinstance(transaction, TransactionData)):
                        data.append(transaction.get_json_of_transaction())
                    elif(isinstance(transaction, RewardData)):
                        data.append(transaction.get_json_of_reward())
                coin_block = CoinBlock(node.calculate_hash(), data)
                node.blockchain.append(coin_block.get_json_of_block())
                node.clear_pending_transactions()
                self.update_node(node)
        print("TRANSACTION VERIFICATION FAILED")
    def worker(self, quit, foundit, node:Node, nodes_list):
        while not quit.is_set():
            if(node.proof_of_work(self.max_nonce, 20)):
                foundit.set()
                nodes_list.put(node)
                break


    def make_turn(self):
        quit = mp.Event()
        foundit = mp.Event()
        q = mp.Queue()
        nodes = self.get_all_nodes()
        for node in nodes:
            print(node.user.name)
            p = mp.Process(target=self.worker, args=(quit, foundit, node, q))
            p.start()
        foundit.wait()
        quit.set()
        winner_node = q.get()
        for node in nodes:
            if(node.user.name==winner_node.user.name):
                    winner_node = node
        coin_list = []
        coin_list.append(Coin.get_coin_id())
        self.send_reward(winner_node, coin_list)
        self.add_block()
        q.close()
        for node in nodes:
            for block in node.blockchain:
                print(block)
            pass                     
