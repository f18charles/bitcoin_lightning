# Get public keys
echo "Getting public keys..."
alice_addr=$(bitcoin-cli -regtest -rpcwallet=alice getnewaddress "")
bob_addr=$(bitcoin-cli -regtest -rpcwallet=bob getnewaddress "")

alice_pubkey=$(bitcoin-cli -regtest -rpcwallet=alice getaddressinfo $alice_addr | jq -r '.pubkey')
bob_pubkey=$(bitcoin-cli -regtest -rpcwallet=bob getaddressinfo $bob_addr | jq -r '.pubkey')

# create 2-of-2 multisig
echo "\nCreating channel multisig..."
multisig=$(bitcoin-cli -regtest createmultisig 2 "[\"$alice_pubkey\", \"$bob_pubkey\"]")
multisig_addr=$(echo $multisig | jq -r '.address')
redeem_script=$(echo $multisig | jq -r '.redeemScript')

echo "\nChannel Multisig Address: $multisig_addr"

# Fund channel from Alice's existing balance
echo "\nAlice funding channel with 10BTC from her existing wallet..."
txid=$(bitcoin-cli -regtest -rpcwallet=alice sendtoaddress $multisig_addr 10)

echo "\nmining confirmation..."
bitcoin-cli -regtest -rpcwallet=alice -generate 1

echo "\nChannel funded. Multisig balance: "
bitcoin-cli -regtest scantxoutset start "[\"addr($multisig_addr)\"]" | jq '.total_amount'

# Alice's remaining balance (decreased by 10 + fees)
echo "\nalice's balance:"
bitcoin-cli -regtest -rpcwallet=alice getbalance

# Bob's balance
echo "\nbob's balance:"
bitcoin-cli -regtest -rpcwallet=bob getbalance