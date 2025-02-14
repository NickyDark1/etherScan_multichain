import requests
import json

class EtherscanAPI:
    def __init__(self, api_key, chain_id=1, base_url="https://api.etherscan.io/api"):
        self.api_key = api_key
        self.chain_id = chain_id
        self.base_url = base_url
    
    def _make_request(self, module, action, **kwargs):
        params = {"module": module, "action": action, "apikey": self.api_key, **kwargs}
        response = requests.get(self.base_url, params=params)
        return response.json()
    
    def get_contract_abi(self, contract_address):
        return self._make_request("contract", "getabi", address=contract_address)

    def get_contract_creation(self, contract_addresses):
        return self._make_request("contract", "getcontractcreation", contractaddresses=",".join(contract_addresses))

    def get_ether_balance(self, address):
        return self._make_request("account", "balance", address=address, tag="latest")

    def get_multi_ether_balance(self, addresses):
        return self._make_request("account", "balancemulti", address=",".join(addresses), tag="latest")

    def get_transactions(self, address, **kwargs):
        return self._make_request("account", "txlist", address=address, **kwargs)

    def get_internal_transactions(self, address, **kwargs):
        return self._make_request("account", "txlistinternal", address=address, **kwargs)

    def get_internal_transactions_by_txhash(self, txhash):
        return self._make_request("account", "txlistinternal", txhash=txhash)

    def get_erc20_transfers(self, address, contract_address=None, **kwargs):
        params = {"address": address, **kwargs}
        if contract_address:
            params["contractaddress"] = contract_address
        return self._make_request("account", "tokentx", **params)

    def get_erc721_transfers(self, address, contract_address=None, **kwargs):
        params = {"address": address, **kwargs}
        if contract_address:
            params["contractaddress"] = contract_address
        return self._make_request("account", "tokennfttx", **params)

    def get_erc1155_transfers(self, address, contract_address=None, **kwargs):
        params = {"address": address, **kwargs}
        if contract_address:
            params["contractaddress"] = contract_address
        return self._make_request("account", "token1155tx", **params)

    def get_mined_blocks(self, address, block_type="blocks", **kwargs):
        return self._make_request("account", "getminedblocks", address=address, blocktype=block_type, **kwargs)

    def get_beacon_withdrawals(self, address, **kwargs):
        return self._make_request("account", "txsBeaconWithdrawal", address=address, **kwargs)

    def get_historical_balance(self, address, block_no):
        return self._make_request("account", "balancehistory", address=address, blockno=block_no)

# Ejemplo de uso
if __name__ == "__main__":

    # https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts
    
    # JSON de blockchain
    blockchains = {
      "chains": [
        {"name": "Ethereum Mainnet", "chain_id": 1},
        {"name": "Sepolia Testnet", "chain_id": 11155111},
        {"name": "Holesky Testnet", "chain_id": 17000},
        {"name": "Abstract Mainnet", "chain_id": 2741},
        {"name": "Abstract Sepolia Testnet", "chain_id": 11124},
        {"name": "ApeChain Curtis Testnet", "chain_id": 33111},
        {"name": "ApeChain Mainnet", "chain_id": 33139},
        {"name": "Arbitrum Nova Mainnet", "chain_id": 42170},
        {"name": "Arbitrum One Mainnet", "chain_id": 42161},
        {"name": "Arbitrum Sepolia Testnet", "chain_id": 421614},
        {"name": "Avalanche C-Chain", "chain_id": 43114},
        {"name": "Avalanche Fuji Testnet", "chain_id": 43113},
        {"name": "Base Mainnet", "chain_id": 8453},
        {"name": "Base Sepolia Testnet", "chain_id": 84532},
        {"name": "Berachain Mainnet", "chain_id": 80094},
        {"name": "BitTorrent Chain Mainnet", "chain_id": 199},
        {"name": "BitTorrent Chain Testnet", "chain_id": 1028},
        {"name": "Blast Mainnet", "chain_id": 81457},
        {"name": "Blast Sepolia Testnet", "chain_id": 168587773},
        {"name": "BNB Smart Chain Mainnet", "chain_id": 56},
        {"name": "BNB Smart Chain Testnet", "chain_id": 97},
        {"name": "Celo Alfajores Testnet", "chain_id": 44787},
        {"name": "Celo Mainnet", "chain_id": 42220},
        {"name": "Cronos Mainnet", "chain_id": 25},
        {"name": "Fantom Opera Mainnet", "chain_id": 250},
        {"name": "Fantom Testnet", "chain_id": 4002},
        {"name": "Fraxtal Mainnet", "chain_id": 252},
        {"name": "Fraxtal Testnet", "chain_id": 2522},
        {"name": "Gnosis", "chain_id": 100},
        {"name": "Kroma Mainnet", "chain_id": 255},
        {"name": "Kroma Sepolia Testnet", "chain_id": 2358},
        {"name": "Linea Mainnet", "chain_id": 59144},
        {"name": "Linea Sepolia Testnet", "chain_id": 59141},
        {"name": "Mantle Mainnet", "chain_id": 5000},
        {"name": "Mantle Sepolia Testnet", "chain_id": 5003},
        {"name": "Moonbase Alpha Testnet", "chain_id": 1287},
        {"name": "Moonbeam Mainnet", "chain_id": 1284},
        {"name": "Moonriver Mainnet", "chain_id": 1285},
        {"name": "OP Mainnet", "chain_id": 10},
        {"name": "OP Sepolia Testnet", "chain_id": 11155420},
        {"name": "Polygon Amoy Testnet", "chain_id": 80002},
        {"name": "Polygon Mainnet", "chain_id": 137},
        {"name": "Polygon zkEVM Cardona Testnet", "chain_id": 2442},
        {"name": "Polygon zkEVM Mainnet", "chain_id": 1101},
        {"name": "Scroll Mainnet", "chain_id": 534352},
        {"name": "Scroll Sepolia Testnet", "chain_id": 534351},
        {"name": "Sonic Blaze Testnet", "chain_id": 57054},
        {"name": "Sonic Mainnet", "chain_id": 146},
        {"name": "Sophon Mainnet", "chain_id": 50104},
        {"name": "Sophon Sepolia Testnet", "chain_id": 531050104},
        {"name": "Taiko Hekla L2 Testnet", "chain_id": 167009},
        {"name": "Taiko Mainnet", "chain_id": 167000},
        {"name": "Unichain Mainnet", "chain_id": 130},
        {"name": "Unichain Sepolia Testnet", "chain_id": 1301},
        {"name": "WEMIX3.0 Mainnet", "chain_id": 1111},
        {"name": "WEMIX3.0 Testnet", "chain_id": 1112},
        {"name": "World Mainnet", "chain_id": 480},
        {"name": "World Sepolia Testnet", "chain_id": 4801},
        {"name": "Xai Mainnet", "chain_id": 660279},
        {"name": "Xai Sepolia Testnet", "chain_id": 37714555429},
        {"name": "XDC Apothem Testnet", "chain_id": 51},
        {"name": "XDC Mainnet", "chain_id": 50},
        {"name": "zkSync Mainnet", "chain_id": 324},
        {"name": "zkSync Sepolia Testnet", "chain_id": 300}
      ]
    }
    api_key = ""
    chain_id = blockchains['chains'][0]['chain_id']  # Ethereum Mainnet
    etherscan = EtherscanAPI(api_key,chain_id=chain_id)

    address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
    print(json.dumps(etherscan.get_ether_balance(address), indent=4))

    address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
    print(json.dumps(etherscan.get_ether_balance(address), indent=4))
    
    contract_address = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
    contract_addresses_list = [
        "0xB83c27805aAcA5C7082eB45C868d955Cf04C337F",
        "0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45",
        "0xe4462eb568E2DFbb5b0cA2D3DbB1A35C9Aa98aad",
        "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "0xf5b969064b91869fBF676ecAbcCd1c5563F591d0"
    ]

    # Obtener ABI del contrato
    abi_response = etherscan.get_contract_abi(contract_address)
    print("ABI Response:", json.dumps(abi_response, indent=4))

    # Obtener información de creación del contrato
    creation_response = etherscan.get_contract_creation(contract_addresses_list)
    print("Contract Creation Response:", json.dumps(creation_response, indent=4))


    get_multi_ether_balance=etherscan.get_multi_ether_balance(contract_addresses_list)
    print("Contract Creation Response:", json.dumps(get_multi_ether_balance, indent=4))
