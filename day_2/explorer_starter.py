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
    
def show_blockchain_info():
    """
    TODO:
    1. Call rpc("getblockchaininfo")
    2. Print: chain, blocks, difficulty
    """
    
    data = rpc("getblockchaininfo")
    
    print("===BlockChain Info===")
    print(f"Chain: {data['chain']}")

show_blockchain_info()