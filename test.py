from CryptoNetwork import CryptoNetwork
from User import User
from Edge import Edge
from Node import Node
def prep_network():
    crypto_network = CryptoNetwork()
    #create network users
    sam = User("sam")
    bob = User("bob")
    ann = User("ann")
    #create nodes
    node_1 = Node(sam)
    node_2 = Node(bob)
    node_3 = Node(ann)
    #create edges
    edge_1 = Edge(node_1, node_2)
    edge_2 = Edge(node_1, node_3)
    edge_3 = Edge(node_2, node_1)
    #add edges to network
    crypto_network.add_edge(edge_1)
    crypto_network.add_edge(edge_2)
    crypto_network.add_edge(edge_3)
    return crypto_network

def test_make_turn_():
    crypto_network = prep_network()
    crypto_network.create_genesis_block()
    nodes = crypto_network.get_all_nodes()
    node_1 = nodes.pop()
    node_2 = nodes.pop()
    node_3 = nodes.pop()
    print("Checkout:")
    print(node_1.user.name+":"+" "+str(node_1.checkout()))
    print(node_2.user.name+":"+" "+str(node_2.checkout()))
    print(node_3.user.name+":"+" "+str(node_3.checkout()))
    node_1.add_transaction_to_pending(node_2.user.public_key, node_1.checkout())
    node_2.add_transaction_to_pending(node_3.user.public_key, node_2.checkout())
    crypto_network.broadcast_transaction_to_other_users_with_probability(node_1, 2)
    crypto_network.broadcast_transaction_to_other_users_with_probability(node_2, 2)
    crypto_network.make_turn()
    print("Checkout:")
    print(node_1.user.name+":"+" "+str(node_1.checkout()))
    print(node_2.user.name+":"+" "+str(node_2.checkout()))
    print(node_3.user.name+":"+" "+str(node_3.checkout()))
def test_make_turn_double_spending():
    crypto_network = prep_network()
    crypto_network.create_genesis_block()
    nodes = crypto_network.get_all_nodes()
    node_1 = nodes.pop()
    node_2 = nodes.pop()
    node_3 = nodes.pop()
    print("Checkout:")
    print(node_1.user.name+":"+" "+str(node_1.checkout()))
    print(node_2.user.name+":"+" "+str(node_2.checkout()))
    print(node_3.user.name+":"+" "+str(node_3.checkout()))
    node_1.add_transaction_to_pending(node_2.user.public_key, node_1.checkout())
    node_2.add_transaction_to_pending(node_3.user.public_key, node_2.checkout())
    node_2.add_transaction_to_pending(node_3.user.public_key, node_2.checkout())
    crypto_network.broadcast_transaction_to_other_users_with_probability(node_1, 2)
    crypto_network.broadcast_transaction_to_other_users_with_probability(node_2, 2)
    crypto_network.broadcast_transaction_to_other_users_with_probability(node_2, 2)
    crypto_network.make_turn()
    print("Checkout:")
    print(node_1.user.name+":"+" "+str(node_1.checkout()))
    print(node_2.user.name+":"+" "+str(node_2.checkout()))
    print(node_3.user.name+":"+" "+str(node_3.checkout()))

    
def main():
    test_make_turn_()
    #test_make_turn_double_spending()
    pass

if __name__ == "__main__":
    main()