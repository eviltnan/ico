import populus
from eth_utils import from_wei
from populus.utils.accounts import is_account_locked
from populus.utils.cli import request_account_unlock
from eth_utils import to_wei

from ico.utils import check_succesful_tx


def main():
    # Which network we deployed our contract
    chain_name = "ropsten"

    # Owner account on geth
    owner_address = "0x2087c59c9524bc0a0e1088a422537d74b7b413d1"

    # Where did we deploy our token
    contract_address = "0x6b5111eb3ab92cf760a80948217d5b9de6734002"

    project = populus.Project()
    with project.get_chain(chain_name) as chain:
        web3 = chain.web3
        print("Web3 provider is", web3.currentProvider)
        print("Owner address is", owner_address)
        print("Owner balance is", from_wei(web3.eth.getBalance(owner_address), "ether"), "ETH")

        # Goes through geth account unlock process if needed
        if is_account_locked(web3, owner_address):
            request_account_unlock(chain, owner_address, None)
        chain.registrar.set_contract_address("AllocatedCrowdsale", contract_address)
        Contract = chain.provider.get_base_contract_factory("AllocatedCrowdsale")
        contract = Contract(address=contract_address)

        print("Checking state...")
        state = contract.call().getState()
        print("Crowdsale state: %s" % state)


if __name__ == "__main__":
    main()
