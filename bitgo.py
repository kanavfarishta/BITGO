import requests
import json
import pandas as pd



# blockInfo =r"https://blockstream.info/api/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
# #url=r"https://blockstream.info/api/tx/132c01e494d114aee972000f15e7772e395ca8c52043acb36304a09791d7a928"
# reqResp = requests.get(blockInfo)
# print(reqResp.text)
# jsonData = json.loads(reqResp.text)

bHash = "000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732"
blockInfo =r"https://blockstream.info/api/block/000000000000000000076c036ff5119e5a5a74df77abf64203473364509f7732/txids"
reqResp = requests.get(blockInfo)

#List of transactions in that block
transactions = json.loads(reqResp.text)
op = {}
for transaction in transactions:
    url = r"https://blockstream.info/api/tx/"+ str(transaction)
    reqResp = requests.get(url)
    txn = json.loads(reqResp.text)
    data = txn.get("vin")
    pvsId = data[0].get("txid")
    count = 0
    print("Transaction",transaction)
    while(True):
        print("PVSIDS",pvsId)
        if pvsId in op:
            count = op[pvsId] +1
            break
        if pvsId in transactions:
            count = count+1
            url = r"https://blockstream.info/api/tx/"+ str(pvsId)
            reqResp = requests.get(url)
            txn = json.loads(reqResp.text)
            data = txn.get("vin")
            pvsId = data[0].get("txid")
        else:
            break
    op[transaction] = count
#print(op)
print(sorted(op, key=op.get, reverse=True)[:10])



