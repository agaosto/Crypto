# Crypto - CoolCoin
> Project made by Radosław Strublewski & Agata Ostolska
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

