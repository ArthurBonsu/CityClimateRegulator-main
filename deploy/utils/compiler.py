from solcx import compile_standard, install_solc
import json
import os

class ContractCompiler:
    def __init__(self, contracts_dir="../contracts"):
        self.contracts_dir = contracts_dir
        install_solc("0.8.0")

    def compile_contract(self, file_name):
        with open(os.path.join(self.contracts_dir, file_name), 'r') as file:
            source_code = file.read()
            
        compiled_sol = compile_standard({
            "language": "Solidity",
            "sources": {
                file_name: {"content": source_code}
            },
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        }, solc_version="0.8.0")
        
        return compiled_sol