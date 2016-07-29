# Splitter
A serpent contract for preventing replay attacks.

When a blockchain forks, every account that had funds before the fork now has funds on both of the forks. If the clients on each fork still use the same transaction format, then transactions meant for only one chain can change the state of a different chain as well. This is call a replay attack.

This contract solves this problem by creating internal account identifiers(here on simply called *accounts*) which depend on a specific block hash. This results in accounts which are different on different blockchains. The contract also updates the block hash it uses to create accounts (about once a month), meaning that in the event of future forks, you can use the same method to move your funds again.

### API
This contract provides the following functions for safely transfering money to a new account. All input arguments and outputs have the ABI type int256.

* `blocks_till_update()`
  * This function takes no arguments, and returns the number of blocks till the block hash used for making accounts gets updated.

* `new_account()`
  * This function creates an new account by hashing (sha3) the sender's address concatenated to a specific block hash. The new account is returned, and is also logged.

* `deposit(account)`
  * This function updates an internal value to keep track of money sent to the contract. It only works if the account specified is owned by the sender. This returns 0 if the sender does not own the account, and 1 if the transaction succeeded. It logs the amount deposited and the new balance.

* `get_balance(account)`
  * This function returns the ammount deposited to this account.

* `withdraw(account, to)`
  * This function withdraws all funds from the account to a new address, and deletes the account. This function only works if called by the address which created the account. On failure, returns 0, otherwise logs the amount of funds sent and the receipt address, and returns 1.
