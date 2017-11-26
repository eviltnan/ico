#!/usr/bin/env bash
geth --testnet --rpc --rpcport 8546 --rpcaddr 127.0.0.1 --rpccorsdomain "*" --rpcapi "eth,web3" --unlock 0x0DBc7F3504bc285F24816D1b50DeEE8B9C1E116f --networkid 3

