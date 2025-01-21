from utils.compiler import ContractCompiler
from utils.deployer import ContractDeployer
from config import TATUM_API_KEY, SEPOLIA_RPC, CONTRACTS
import json
import os

def main():
    # Setup
    headers = {
        "x-api-key": TATUM_API_KEY,
        "Content-Type": "application/json"
    }
    
    compiler = ContractCompiler()
    deployer = ContractDeployer(SEPOLIA_RPC, "YOUR_PRIVATE_KEY")
    
    deployed_contracts = {}
    
    # Deploy all contracts
    for contract_name, file_name in CONTRACTS.items():
        print(f"Deploying {contract_name}...")
        
        try:
            # Compile
            compiled = compiler.compile_contract(file_name)
            
            # Deploy
            address, abi = deployer.deploy_contract(compiled, file_name.split('.')[0])
            
            deployed_contracts[contract_name] = {
                'address': address,
                'abi': abi
            }
            
            print(f"{contract_name} deployed at: {address}")
            
            # Save deployment info
            with open(f'../deployed/{contract_name}.json', 'w') as f:
                json.dump({
                    'address': address,
                    'abi': abi
                }, f, indent=2)
                
        except Exception as e:
            print(f"Error deploying {contract_name}: {str(e)}")
    
    # Save full deployment info
    with open('../deployed/deployment_info.json', 'w') as f:
        json.dump({
            'network': 'sepolia',
            'deployer_address': deployer.account.address,
            'contracts': deployed_contracts
        }, f, indent=2)

if __name__ == "__main__":
    main()