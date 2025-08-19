from web3 import Web3
import httpx

api_url = "your_api"
web3 = Web3(Web3.HTTPProvider(api_url))

connected = web3.is_connected()
if connected:
    print(f"successfully connected to chain!")
else:
    print(f"error connected, try again")
    
def status_code():
    with httpx.Client() as client:
        response = client.get(api_url)
        print(f"status code - {response}")
status_code()

class Wallets:
    def __init__(self):
        self.wallets = {
    
        "user1" : "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
        "user2" : "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f",
        "user3" : "0x6B175474E89094C44Da98b954EedeAC495271d0F",
        "user4" : "0x9f8F72aA9304c8B593d555F12ef6589cC3A579A2",
        
        }
        
    def check_balance(self, web3):
        for user, address in self.wallets.items():
            try:
                checksum_address = web3.to_checksum_address(address)
                balance_account = web3.eth.get_balance(checksum_address)
                eth_balance = Web3.from_wei(balance_account, 'ether')
                
                print(f"{checksum_address} balance - {eth_balance: .4f}")
            except ValueError:
                print(f"your address incorrect")
                
if __name__ == "__main__":
    addresses = Wallets()
    addresses.check_balance(web3)
