from web3 import Web3
from eth_account import Account
import json
import os

class ContractDeployer:
    def __init__(self, web3_provider, private_key):
        self.w3 = Web3(Web3.HTTPProvider(web3_provider))
        self.account = Account.from_key(private_key)
        
    def deploy_contract(self, compiled_contract, contract_name):
        bytecode = compiled_contract["contracts"][contract_name][contract_name]["evm"]["bytecode"]["object"]
        abi = compiled_contract["contracts"][contract_name][contract_name]["abi"]
        
        Contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        
        transaction = Contract.constructor().build_transaction({
            'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gas': 2000000,
            'gasPrice': self.w3.eth.gas_price
        })
        
        signed_txn = self.account.sign_transaction(transaction)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        
        return tx_receipt.contractAddress, abi