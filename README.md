# Crypto - CoolCoin
> Project made by Radosław Strublewski & Agata Ostolska
## 2nd sprint
The project has been improved. main.py cointains use cases that show all the features. Users, User and Chain Manager classes has been added. Users are created and coins are distributed between them initially. Transactions are stored in JSON format.

The whole blockchain is displayed at the end.
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

