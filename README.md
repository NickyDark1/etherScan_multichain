# Etherscan API Wrapper

## Descripción
Este proyecto proporciona una clase `EtherscanAPI` que actúa como una envoltura para interactuar con la API de Etherscan. Permite recuperar información sobre contratos, balances de direcciones, transacciones y otros datos en la blockchain de Ethereum.

## Características
- Obtener ABI de contratos.
- Consultar información de creación de contratos.
- Obtener balances de ETH de una o múltiples direcciones.
- Consultar transacciones externas e internas.
- Obtener transferencias de tokens ERC-20, ERC-721 y ERC-1155.
- Consultar bloques minados por una dirección.
- Obtener historial de balance de una dirección.
- Consultar retiros en la Beacon Chain de Ethereum.

## Instalación
```sh
pip install requests
```

## Uso
### Inicialización
```python
from etherscan_api import EtherscanAPI

api_key = "TU_API_KEY"
etherscan = EtherscanAPI(api_key)
```

### Obtener balance de una dirección
```python
address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
balance = etherscan.get_ether_balance(address)
print(balance)
```

### Obtener ABI de un contrato
```python
contract_address = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413"
abi = etherscan.get_contract_abi(contract_address)
print(abi)
```

### Obtener transacciones de una dirección
```python
transactions = etherscan.get_transactions(address)
print(transactions)
```

## Configuración
Puedes especificar la `base_url` y `chain_id` al inicializar la API si deseas conectarte a redes de prueba.
```python
etherscan = EtherscanAPI(api_key, chain_id=11155111, base_url="https://api.etherscan.io/api") # "https://api-sepolia.etherscan.io/api"
```
