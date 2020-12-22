# from uuid import uuid4

# from blockchain import Blockchain
# from utility.verification import Verification
# from wallet import Wallet


# class Node:
#     """The node which runs the local blockchain instance.

#     Attributes:
#         :id: The id of the node.
#         :blockchain: The blockchain which is run by this node.
#     """

#     def __init__(self):
#         # self.wallet = str(uuid4())
#         self.wallet = Wallet()
#         self.wallet.create_keys()
#         self.blockchain = Blockchain(self.wallet.public_key)

#     def get_transaction_value(self):
#         """ Returns the input of the user (a new transaction amount) as a float. """

#         # Get the user input, transform it from a string to a float and store it in user_input
#         print('-' * 30, '\nNew Transaction Form\n', '-' * 30, sep='')
#         tx_receiver = input('Enter recipient name: ')
#         tx_amount = float(input('Enter new transaction amount: '))
#         return (tx_receiver, tx_amount)

#     def get_user_choice(self):
#         """Prompts the user for its choice and return it."""
#         user_input = input('\nEnter choice: ')
#         return user_input

#     def print_blockchain_elements(self):
#         """ Output all blocks of the blockchain. """

#         # Output the blockchain list to the console
#         for block in self.blockchain.chain:
#             print('\n', '-' * 60, '\nOutputting Block:\n', '-' * 60, sep='')
#             print(block)

#     def listen_for_input(self):
#         """Starts the node and waits for user input."""
#         waiting_for_user_input = True

#         # A while loop for the user input interface
#         # It's a loop that exits once waiting_for_input
#         # becomes False or when break is called
#         while waiting_for_user_input:
#             print('\nPlease choose from Menu\n' + '-' * 30)
#             print('1: Add a new transaction')
#             print('2: Mine a new block')
#             print('3: Output the blockchain blocks')
#             print('4: Check transactions')
#             print('5: Create Wallet')
#             print('6: Load Wallet')
#             print('7: Save Keys')
#             print('q: Quit')
#             user_choice = self.get_user_choice()

#             if user_choice == '1':
#                 tx_data = self.get_transaction_value()
#                 # Unpacking Tuple -below-
#                 recipient, amount = tx_data
#                 # Add the transaction amount to the blockchain
#                 signature = self.wallet.sign_transaction(
#                     self.wallet.public_key, recipient, amount)

#                 if self.blockchain.add_transaction(recipient, self.wallet.public_key, signature, amount=amount):
#                     print('\nTransaction added successfully!')
#                 else:
#                     print('\nTransaction Failed! Insufficient Balance')
#                 print('\nopen_transactions\n', '-' * 30)
#                 print(self.blockchain.get_open_transactions())
#             elif user_choice == '2':
#                 if not self.blockchain.mine_block():
#                     print(
#                         '\nMining Failed! Got no Wallet? Create your own Wallet by Pressing - 5')
#             elif user_choice == '3':
#                 self.print_blockchain_elements()
#             elif user_choice == '4':
#                 if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
#                     print("\nAll transactions are valid")
#                 else:
#                     print("\n Invalid Transactions present!")
#             elif user_choice == '5':
#                 self.wallet.create_keys()
#                 self.blockchain = Blockchain(self.wallet.public_key)
#             elif user_choice == '6':
#                 self.wallet.load_keys()
#                 self.blockchain = Blockchain(self.wallet.public_key)
#             elif user_choice == '7':
#                 self.wallet.save_keys()
#             elif user_choice == 'q' or user_choice == 'Q':
#                 # This will lead to the loop to exist because it's running condition becomes False
#                 waiting_for_user_input = False
#             else:
#                 print('\nInput was invalid! Please pick a value from the list')
#             if not Verification.verify_chain(self.blockchain.chain):
#                 print('\nInvalid Blockchain!')
#                 # Break out of the loop
#                 break
#             # print(f'\nBalance of {owner}: {get_balance(owner):6.2f} ')
#             print('\nBalance of {}: {:6.2f} '.format(
#                 self.wallet.public_key, self.blockchain.get_balance()))
#         else:
#             print('\nUser Left!')
#         print('Exiting...')


# if __name__ == '__main__':
#     node = Node()
#     node.listen_for_input()
