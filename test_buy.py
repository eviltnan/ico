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
    # test_address = "0x2087c59c9524bc0a0e1088a422537d74b7b413d1"
    test_address = "0x84766026935672d3cab0b84a2332c3fb45e5d26b"
    # Where did we deploy our token
    contract_address = "0x6ba6113c594799f9394426bb9e45aa03f56d8229"

    project = populus.Project()
    with project.get_chain(chain_name) as chain:
        web3 = chain.web3
        print("Web3 provider is", web3.currentProvider)
        print("Owner address is", test_address)
        print("Owner balance is", from_wei(web3.eth.getBalance(test_address), "ether"), "ETH")

        # Goes through geth account unlock process if needed
        if is_account_locked(web3, test_address):
            request_account_unlock(chain, test_address, None)
        chain.registrar.set_contract_address("AllocatedCrowdsale", contract_address)
        Contract = chain.provider.get_base_contract_factory("AllocatedCrowdsale")
        contract = Contract(address=contract_address)

        print("Attempting test buy")
        txid = contract.transact({"from": test_address, "value": to_wei("0.01", "ether")}).buy()
        print("TXID", txid)
        check_succesful_tx(web3, txid)
        print("Transaction successful")


if __name__ == "__main__":
    main()
