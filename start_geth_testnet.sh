#!/usr/bin/env bash
geth --testnet --rpc --rpcport 8546 --rpcaddr 127.0.0.1 --rpccorsdomain "*" --rpcapi "eth,web3" --unlock 0x0dbc7f3504bc285f24816d1b50deee8b9c1e116f --networkid 3 --etherbase 0x0dbc7f3504bc285f24816d1b50deee8b9c1e116f


