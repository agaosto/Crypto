# Crypto - CoolCoin
> Project made by Radosław Strublewski & Agata Ostolska
## 4th sprint
During the final sprint the network has been decentralized. Each node (user) has their own copy of the blockchain and a list of pending transactions.
Each transaction is transmitted to all of the other nodes with 90% probability.

Proof of work is running in parallel. The first miner that finds the hash with specified number of zeros, proposes the new block to others. If all nodes reach a consensus, the block is added to the blockchain and the miner gets a coin in reward.

Bob, Ann and Sam have their coins:

![image](https://user-images.githubusercontent.com/61022689/151076110-1d88c030-78e4-445c-9de8-3323deb6f255.png)

When Sam pays 1 coin to Ann, and Ann pays 1 coin to Bob, and all the nodes reach consensus, we can see that Sam got a reward coin.

![image](https://user-images.githubusercontent.com/61022689/151076691-89a0f460-75a4-4173-a20a-c9c2d7a9101c.png)

When validation fails, there is a message:

![image](https://user-images.githubusercontent.com/61022689/151076720-7bfc905f-0df2-4348-8294-7dd350fec356.png)


## 3rd sprint
Users (and the Chain Manager) are now represented by their digital identity (public and private key). 512-bit keys are generated with Python-RSA package. Creating coins in genesis block is signed by the Chain Manager. Coins can be validated:

![image](https://user-images.githubusercontent.com/61022689/146995197-f3cd508b-9e5e-4eb5-9bc7-1a9c2e616c9c.png)

A new field in JSON transaction has been added. Transaction data now consists of:
- sender (public key)
- coins
- signature

![image](https://user-images.githubusercontent.com/61022689/146995792-a229ebf0-2b82-408d-9fcd-c27238263226.png)

Signature in JSON is encoded in Base64.

Use cases from the 2nd sprint were used in main.py.

## 2nd sprint
The project has been improved. main.py cointains use cases that show all the new features. Users, User and Chain Manager classes have been added. Users are created and coins are distributed between them initially. Coin distribution data is stored in the initial block.

![image](https://user-images.githubusercontent.com/61022689/143148094-c73e100f-c3e3-4f5e-aa46-75f76821fff1.png)

Transactions are stored in JSON format. Use cases 1 and 2 show transactions with single and multiple coins. 

![image](https://user-images.githubusercontent.com/61022689/143148148-6bc83dee-c26a-400d-8c96-ddc90204fea3.png)

Cases 3 and 4 show double-spending protection. If a user tries to spend a coin that they don't have, an error is displayed and the transaction is not validated.

![image](https://user-images.githubusercontent.com/61022689/143148191-4224a85f-f4dd-4f26-837b-18f0f2d87868.png)

Users can validate the blockchain. If the attacker calls the method that adds a new block to the blockchain, all the users will know that the blockchain is not valid.

![image](https://user-images.githubusercontent.com/61022689/143148326-915e2eb4-721f-4014-908e-92e9d8863643.png)

The whole blockchain is displayed at the end.

![image](https://user-images.githubusercontent.com/61022689/143148484-eb91e100-a933-430b-9afd-88e48e98e2f2.png)

## 1st sprint
The project allows the user to create a simple blockchain. After starting the program, the user interface can be seen in the terminal. The user can add another block / transaction (at this stage it is assumed that one block contains only one transaction) or display all blocks in the blockchain. Press [0] to exit.

![image](https://user-images.githubusercontent.com/61022689/138954168-df3d4ae8-9d22-42e4-899d-620adecc4e41.png)

After selecting option [1], the user must provide the names of sender and recipient.

![image](https://user-images.githubusercontent.com/61022689/138940756-670e10ef-ec91-41bb-80de-f92f55c412ff.png)

Then it is checked whether the hash in the new block is the same as the hash based on the data from the previous block. Information about both hashes and the validation process is displayed in the terminal.

![image](https://user-images.githubusercontent.com/61022689/138954300-b07dc5c2-ec12-4706-9957-98fa8f9a6866.png)

After selecting number [2], the entire blockchain is displayed. Block 0 is the initial block.

![image](https://user-images.githubusercontent.com/61022689/138954384-fbf9c4e4-f373-43ba-9418-12a137fe6672.png)

Number [3] displays the whole blockchain including the final block (that consists of previous block hash) and exits the program.

![image](https://user-images.githubusercontent.com/61022689/138954563-621de90d-f72f-4bab-8623-b3ab1fb95375.png)

