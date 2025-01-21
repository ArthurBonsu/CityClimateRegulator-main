import asyncio
from blockchain_workflow import BlockchainWorkflow
 // contract_addresses = **0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
contract_addresses = {
    'CityRegister': '0x...',
    'CompanyRegister': '0x...',
    'CityEmissionsContract': '0x...',
    'RenewalTheoryContract': '0x...',
    'CityHealthCalculator': '0x...',
    'TemperatureRenewalContract': '0x...'
}

workflow = BlockchainWorkflow('YOUR_WEB3_PROVIDER_URL', contract_addresses)
workflow.load_contract('CityRegister', 'path/to/CityRegister.json')
# Load other contracts similarly

asyncio.run(workflow.run_complete_workflow('CityData.csv', 'CompanyData.csv'))
