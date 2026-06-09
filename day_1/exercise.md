# HANDS-ON EXERCISES

## EXERCISE 1: CHECK YOUR NODE

```sh
#check blockchain info
bitcoin-cli -regtest getblockchaininfo

{
  "chain": "regtest",
  "blocks": 101,
  "headers": 101,
  "bestblockhash": "35102a5763c9c5e5ad3de5d48f0de0d140ea8b472d3c20d90a9e35300d28c865",
  "bits": "207fffff",
  "target": "7fffff0000000000000000000000000000000000000000000000000000000000",
  "difficulty": 4.656542373906925e-10,
  "time": 1780926817,
  "mediantime": 1780926816,
  "verificationprogress": 0.6493093131325991,
  "initialblockdownload": false,
  "chainwork": "00000000000000000000000000000000000000000000000000000000000000cc",
  "size_on_disk": 30290,
  "pruned": false,
  "warnings": [
    "This is a pre-release test build - use at your own risk - do not use for mining or merchant applications"
  ]
}

# check network info
bitcoin-cli -regtest getnetworkinfo

{
  "version": 319900,
  "subversion": "/Satoshi:31.99.0/",
  "protocolversion": 70016,
  "localservices": "0000000000000c09",
  "localservicesnames": [
    "NETWORK",
    "WITNESS",
    "NETWORK_LIMITED",
    "P2P_V2"
  ],
  "localrelay": true,
  "timeoffset": 0,
  "networkactive": true,
  "connections": 0,
  "connections_in": 0,
  "connections_out": 0,
  "networks": [
    {
      "name": "ipv4",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "ipv6",
      "limited": false,
      "reachable": true,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "onion",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "i2p",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    },
    {
      "name": "cjdns",
      "limited": true,
      "reachable": false,
      "proxy": "",
      "proxy_randomize_credentials": false
    }
  ],
  "relayfee": 0.00000100,
  "incrementalfee": 0.00000100,
  "localaddresses": [
  ],
  "warnings": [
    "This is a pre-release test build - use at your own risk - do not use for mining or merchant applications"
  ]
}
```

## EXERCISE 2: CREATE WALLETS

```sh
# create Alice's wallet
bitcoin-cli -regtest createwallet "alice"

{
  "name": "alice"
}

# create Bob's wallet
bitcoin-cli -regtest createwallet "bob"

{
  "name": "bob"
}

```

## EXERCISE 3: GENERATE ADDRESSES

```sh
# Get address for alice
bitcoin-cli -regtest -rpcwallet=alice getnewaddress

bcrt1qzr2aajc5g8fleufhu24hdew3jf0j2dthdvdtjg

# Get address for bob
bitcoin-cli -regtest -rpcwallet=bob getnewaddress

bcrt1qk4gvexveszy6z20sjna57hwl93hpte0x2xta8f

# check Alice's balance
bitcoin-cli -regtest -rpcwallet=alice getbalance

0.00000000
```

## EXERCISE 4: MINE BLOCKS

```sh
# Store Alice's address in a variable
ALICE=$(bitcoin-cli -regtest -rpcwallet=alice getnewaddress)

# No out put

# Mine 101 blocks to Alice
bitcoin-cli -regtest generatetoaddress 101 "$ALICE"

[
  "45d66b2fc00782ffcafd84cd7ace862d08366ba1567a292287b13cfa8fa6acf8",
  "6395b5c6d26b0d16bf5a28121d821c6ca73935a303bfb61c6b41bd52b01bc9c3",
  "3077407c9a1aa58e21d8fc3ff320bff7034bb3c11963187c5048306f5c0a85de",
  "367be1f0cd1a380328749c8b5e87cca0ecb90c077556bd5903738fe27e0cbc8e",
  "699b6c43929e79557fd9e5fe8d47922f650251c239f6eaeb69d80b30c84a6ce5",
                            ...
]

# Check balance now
bitcoin-cli -regtest -rpcwallet=alice getbalance

50.00000000

```

## EXERCISE 5: SEND TRANSACTION

```sh
# Get Bob's address
BOB=$(bitcoin-cli -regtest -rpcwallet=bob getnewaddress)

# No output

# Send 10 BTC from Alice to Bob
bitcoin-cli -regtest -rpcwallet=alice sendtoaddress "$BOB" 10

48939d12b9dd192af9823b62c810baf557b1240390d893663d2991bb9b5e38ef

# Check mempool (unconfirmed transactions)
bitcoin-cli -regtest getmempoolinfo

{
  "loaded": true,
  "size": 1,
  "bytes": 141,
  "usage": 1224,
  "total_fee": 0.00000141,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00000100,
  "minrelaytxfee": 0.00000100,
  "incrementalrelayfee": 0.00000100,
  "unbroadcastcount": 1,
  "permitbaremultisig": true,
  "maxdatacarriersize": 100000,
  "limitclustercount": 64,
  "limitclustersize": 101000,
  "optimal": true
}

# check Bob's balance
bitcoin-cli -regtest -rpcwallet=bob getbalance     

0.00000000

# check Alice's balance
bitcoin-cli -regtest -rpcwallet=alice getbalance

39.99999859

```

## EXERCISE 6: CONFIRM IT

```sh
# Mine a block to confirm the transaction
bitcoin-cli -regtest generatetoaddress 1 "$ALICE"

[
  "59358f767d3214aeba4f9fb3ae7e1fc3618fd44e57359150b95788b86e97bb85"
]

# Check Bob's Balance
bitcoin-cli -regtest -rpcwallet=bob getbalance     

10.00000000

# Mempool should be empty now
bitcoin-cli -regtest getmempoolinfo

{
  "loaded": true,
  "size": 0,
  "bytes": 0,
  "usage": 64,
  "total_fee": 0.00000000,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00000100,
  "minrelaytxfee": 0.00000100,
  "incrementalrelayfee": 0.00000100,
  "unbroadcastcount": 0,
  "permitbaremultisig": true,
  "maxdatacarriersize": 100000,
  "limitclustercount": 64,
  "limitclustersize": 101000,
  "optimal": true
}

```

## EXERCISE 7: EXPLORE TRANSACTION

```sh
# List Alice's transactions
bitcoin-cli -regtest -rpcwallet=alice listtransactions

[
  {
    "address": "bcrt1qymlj2leaugxhsw5rhxw4rdvwggqnt7qns00v7v",
    "parent_descs": [
      "wpkh([c14f92ad/84h/1h/0h]tpubDCYip8nwnJgYtrgc9DoVFBzD81NSh3KUqWUf7DcrxFcyQbc9hDeJ8RhRvF6CQrhXSaSc4yfdH7yHuPYzUoaasMjFttRDbd4A4Ky4JhSf8em/0/*)#az0hc2wy"
    ],
    "category": "immature",
    "amount": 25.00000000,
    "label": "",
    "vout": 0,
    "abandoned": false,
    "confirmations": 9,
    "generated": true,
    "blockhash": "7c466dbf50c11ec1ad792e7b3c4793614230acd12ad9ead65663807fa601aa3d",
    "blockheight": 195,
    "blockindex": 0,
    "blocktime": 1780982515,
    "txid": "a65f635de321f7cf7434cd1a4904ae245dcaabf9c5f5dc224bff2bce78aa650b",
    "wtxid": "46301ba1935809300c16a5f750964b1ad108d5f297b6d2d6d12d55b2a8929961",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": 1780982501,
    "timereceived": 1780982501
  },
  {
    "address": "bcrt1qymlj2leaugxhsw5rhxw4rdvwggqnt7qns00v7v",
    "parent_descs": [
      "wpkh([c14f92ad/84h/1h/0h]tpubDCYip8nwnJgYtrgc9DoVFBzD81NSh3KUqWUf7DcrxFcyQbc9hDeJ8RhRvF6CQrhXSaSc4yfdH7yHuPYzUoaasMjFttRDbd4A4Ky4JhSf8em/0/*)#az0hc2wy"
    ],
    "category": "immature",
    "amount": 25.00000000,
    "label": "",
    "vout": 0,
    "abandoned": false,
    "confirmations": 8,
    "generated": true,
    "blockhash": "2bc1c48b969864ffb34e3e16efab311f260850eb7d70d7613182f1c4369e450c",
    "blockheight": 196,
    "blockindex": 0,
    "blocktime": 1780982515,
    "txid": "d76a42d91ce838ff35b5c67720c07bcb079c801768cb21a30dd1a1be67dcc805",
    "wtxid": "48b82bb931f9e46331ed64218b23ece6e6c4c15992dc258e8c8b39313ddbbf16",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": 1780982501,
    "timereceived": 1780982501
  },
  {
    "address": "bcrt1qymlj2leaugxhsw5rhxw4rdvwggqnt7qns00v7v",
    "parent_descs": [
      "wpkh([c14f92ad/84h/1h/0h]tpubDCYip8nwnJgYtrgc9DoVFBzD81NSh3KUqWUf7DcrxFcyQbc9hDeJ8RhRvF6CQrhXSaSc4yfdH7yHuPYzUoaasMjFttRDbd4A4Ky4JhSf8em/0/*)#az0hc2wy"
    ],
    "category": "immature",
    "amount": 25.00000000,
    "label": "",
    "vout": 0,
    "abandoned": false,
    "confirmations": 7,
    "generated": true,
    "blockhash": "6756b7b9929b35ec072a348d4bff1db3d3759c09f2258f2800db6cf86ba58a91",
    "blockheight": 197,
    "blockindex": 0,
    "blocktime": 1780982515,
    "txid": "8b430c22a7cfe4a64d02c8d5696286c14fd02c052e197670de0f56f2486003c3",
    "wtxid": "5b7d36f35bfc5bee41c1e43affe15fe5730663efaa5974fe100aee75c61f69c3",
    "walletconflicts": [
    ],
    "mempoolconflicts": [
    ],
    "time": 1780982501,
    "timereceived": 1780982501
  },
                                ...
]

# Get raw transaction (replace TXID with actual ID)
bitcoin-cli -regtest getrawtransaction "TXID" true
# failed to get transaction details

```

## EXERCISE 8: EXPLORE A TRANSACTION

```sh
# Get the latest block hash
bitcoin-cli -regtest getbestblockhash

59358f767d3214aeba4f9fb3ae7e1fc3618fd44e57359150b95788b86e97bb85

# get block details (replace HASH)
bitcoin-cli -regtest getblock "HASH" 1

{
  "hash": "59358f767d3214aeba4f9fb3ae7e1fc3618fd44e57359150b95788b86e97bb85",
  "confirmations": 1,
  "height": 203,
  "version": 805306368,
  "versionHex": "30000000",
  "merkleroot": "5305305c853fe33848b63818d40a24ce1e7c248ed87028cb399d7fa777d3ad80",
  "time": 1780983156,
  "mediantime": 1780982516,
  "nonce": 0,
  "bits": "207fffff",
  "target": "7fffff0000000000000000000000000000000000000000000000000000000000",
  "difficulty": 4.656542373906925e-10,
  "chainwork": "0000000000000000000000000000000000000000000000000000000000000198",
  "nTx": 2,
  "previousblockhash": "221db3c412634937a6150725aea24532e77f3b620f71e9bb9c8b554ffcbcc394",
  "strippedsize": 326,
  "size": 471,
  "weight": 1449,
  "coinbase_tx": {
    "version": 2,
    "locktime": 202,
    "sequence": 4294967294,
    "coinbase": "02cb00",
    "witness": "0000000000000000000000000000000000000000000000000000000000000000"
  },
  "tx": [
    "ce5a80ac46928829d4ed23edd00b1441a470c81ced80b6359730069f031304cd",
    "48939d12b9dd192af9823b62c810baf557b1240390d893663d2991bb9b5e38ef"
  ]
}

```

## EXERCISE 8: ADDRESS TYPES

``` sh
# legacy (oldest)
bitcoin-cli -regtest -rpcwallet=alice getnewaddress "" "legacy"

mtSAszJAJ57A8MugVUHaiJqctMECS57SyR

# Native segwit (recommended)
bitcoin-cli -regtest -rpcwallet=alice getnewaddress "" "bech32"

bcrt1qelxvcpa0prc6csgmlzqt2upr4vryvwkwv2q6r

# taproot(newest)
bitcoin-cli -regtest -rpcwallet=alice getnewaddress "" "bech32m"

bcrt1p62k2vp9kl6ssg4hjzgc770vjkyv0xcy66dgm8jwqexg5sdw68r4qvrfsu9


```

## DAY 1 SUMMARY

You learned:

- Configure Bitcoin Core for regtest

- Create wallets and generate addresses

- Mine blocks and earn coinbase rewards

- Send transactions between wallets

- Explore blocks and transactions via CLI

- Different address types and SegWit
