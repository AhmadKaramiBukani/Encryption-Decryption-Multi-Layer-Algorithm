# Encryption-Decryption-Multi-Layer-Algorithm
This encryption and decryption multi-layer algorithm was coded in Python by the algorithm's designer, Ahmad Karami Bukani from Rojhalat Kurdistan.

Encryption Decryption Multi-Layer algorithm is in the form of several layers and each layer performs a specific action, in total, this algorithm has eight layers, four layers are for encryption and four layers are for decryption, and these layers guarantee that the best The method of encryption and decryption of very important data.

There are different ways to encrypt and decrypt the data to protect the data with low level security to high level but a new solution was formed in my mind which helps to encrypt and decrypt the data in a certain way, according to the existence of four layers for encryption and four layers for decryption, various operations take place on the data to ensure that when the data is sent or received over the wireless network or the wired network, when If the data is eavesdropped or falls into the hands of hackers, it will not be recoverable, even if part of the two-step encryption is recoverable, they will not be able to understand the content of the data, Although it is written in English, misleading and fake information has fallen into the hands of hackers.

I used the Python 3.12 programming language and described the entire set of commands along with the layers of the EDML algorithm, but the layers of this algorithm include two parts: Although it is written in English, misleading and fake information has fallen into the hands of hackers.

Part A- Data encryption consists of four layers.  
1- Adding useless text data to useful text data (INSERT GAP TEXT LAYER) 
2- Hiding all useful text data and useless text data and converting all data to useless data (Hide TEXT LAYER)
3- Inserting the encryption of all useless textual data in the format of step one (INSERT ENCRYPTION RANDOM LAYER) 
4-  insert re-encryption of all encrypted data in the form of the second step (INSERT ENCRYPTION GAP LAYER)

Part B - Data decryption consists of four layers.  
1- Delete all encrypted data in the second step for decryption (DELETE DECRYPTION GAP LAYER) 
2- Deleting all encrypted data of step one to decrypt and convert it to all useless text data (DELETE DECRYPTION RANDOM LAYER)
3- Convert all useless data to useful text data and useless text data and display it (SHOW TEXT LAYER) 
4- Deleting all useless text data and revealing useful text data (DELETE GAP TEXT LAYER)

The data encryption layers deliver data from top to bottom, and the data decryption layers deliver data from bottom to top, and the act of sending data in networks It is done by the INSERT ENCRYPTION GAP layer and the operation of receiving data in the networks is done by the DELETE GAP TEXT layer.

 
