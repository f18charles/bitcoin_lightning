import requests, json

def rpc(method, params=None, wallet=None):
    url = "http://127.0.0.1:18443/"
    if wallet:
        url = f"{url}wallet/{wallet}"
        
    data = json.dumps({
        "jsonrpc": "1.0", 
        "id": "explorer",
        "method": method,
        "params": params or []
    })
    
    resp = requests.post(url, data=data, auth=("bootcamp", "bootcamp123"))
    return resp.json()
    
# Blockchain info
def show_blockchain_info():
    """
    TODO:
    1. Call rpc("getblockchaininfo")
    2. Print: chain, blocks, difficulty
    """
    
    data = rpc("getblockchaininfo")
    info = data['result']
    
    print("===BlockChain Info===")
    print(f"Chain:          {info['chain']}")
    print(f"Blocks:          {info['blocks']}")
    print(f"Difficulty:          {info['difficulty']}")

# Wallet Balance
def show_wallet_balance(wallet_name):
    """
    TODO:
    1. Load wallet (try/except)
    2. Call rpc("getbalance", [], wallet=wallet_name)
    3. Print the balance
    """
    
    try:
        rpc("loadwallet", [wallet_name])
    except:
        pass
    
    balance = rpc("getbalance", [], wallet_name)
    print(f"=== Wallet: {wallet_name} ===")
    print(f"Balance: {balance['result']} BTC")
    
# List transactions
def list_transactions(wallet_name, count=5):
    """
    1. call rpc("listtransactions", ["*", count], wallet=wallet_name)
    2. for each tx: print direction, amount, txid
    """
    
    try:
        rpc("loadwallet", [wallet_name])
    except:
        pass
    
    data = rpc("listtransactions", ["*", count], wallet_name)
    txs = data['result']
    
    for tx in txs:
        if tx['category'] in ('receive', 'generate', 'immature'):
            direction = "IN"
        else:
            direction = "OUT"
        
        print(f"{direction} {tx['amount']:+8f} BTC")
        
# Decode tx
def decode_transactions(txid):
    """
    TODO:
    1. Call rpc("getrawtransaction", [txid True])
    2. Print inputs(vin) and outputs(vout)
    """
    
    data = rpc("getrawtransaction", [txid, True])
    tx = data['result']
    
    print(f"Size: {tx['size']} bytes")
    
    print("\nInputs:")
    for vin in tx['vin']:
        if 'coinbase' in vin:
            print("  COINBASE (mining reward)")
        else:
            print(f"   From: {vin['txid'][:20]}...")

    print("\nOutputs:")
    for vout in tx['vout']:
        addr = vout['scriptPubKey'].get('address', '?')
        print(addr)
        
# Block details
def show_block(blockhash=None):
    """
    TODO:
    1. If no hash: rpc("getbestblockhash)
    2. Call rpc("getblock", [blockhash, 1])
    3. Print: height, hash, time, tx count
    """
    
    if blockhash is None:
        blockhash = rpc("getbestblockhash")['result']
        
    data = rpc("getblock", [blockhash, 1])
    block = data['result']
    
    print(f"===Block #{block['height']} ===")
    print(f"Hash: {block['hash'][:32]}...")
    print(f"Time: {block['time']}")
    print(f"Transactions: {block['nTx']}")

# show_blockchain_info()
# show_wallet_balance("alice")
# list_transactions("alice", 3)
# decode_transactions("ce5a80ac46928829d4ed23edd00b1441a470c81ced80b6359730069f031304cd")
show_block()
