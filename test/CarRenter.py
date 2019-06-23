#from web3utils.web3 import Web3, HTTPProvider
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
#from web3utils.web3.contract import ConciseContract
#from web3.utils.currency import to_wei
#from web3utils.currency import to_wei
import json

with open('/Users/ulf/Desktop/Automative-car/build/contracts/CarRenter.json' , 'r') as f:
    data = json.loads(f.read())

abi = data['abi']
for dic in data['networks']:
    #print(dic)
    address = data['networks'][dic]['address']

config = {
    'abi': abi,
    'address': address,
    
}

web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))
#owner = web3.eth.accounts[0]
#customer = web3.eth.accounts[1]
contract_instance = web3.eth.contract(address=config['address'], abi=config['abi']) 
eth = Web3.toWei(1, 'ether')
renting_dict = {}

def Get_Unused_Account(count):
    return web3.eth.accounts[count]

def Get_Balance(count):
    return Web3.fromWei(web3.eth.getBalance(web3.eth.accounts[count]), 'ether')

def Create_Vtoken(_name, _age, _owner):
    transact_hash = contract_instance.functions.Create_Vtoken(_name, _age).transact({'from': _owner})
    return transact_hash

def Rent_Car(_tokenId, _customer):
    transact_hash = contract_instance.functions.Rent_Car(_tokenId).transact({'from': _customer, 'value': eth})
    transact_receipt = web3.eth.getTransactionReceipt(transact_hash)
    logs = contract_instance.events.RentCar().processReceipt(transact_receipt)
    id = logs[0]['args']['_id']
    renter = logs[0]['args']['_renter']
    owner = logs[0]['args']['_owner']
    renting_dict[id] = [renter, owner]
    detail = {
        'id': id,
        'owner': owner,
        'renter': renter
    }
    return detail

def Return_Car(_tokenId, _oil, crashes, rate, customer):
    #transact_hash = contract_instance.Return_Car(_tokenId, _oil, crashes, rate, transact={'from': customer})
    renter = renting_dict[_tokenId][0]
    owner = renting_dict[_tokenId][1]
    if renter != customer:
        return False
    
    if (crashes == 0):
       transact_hash2 = contract_instance.functions.Return_Bail(_tokenId).transact({'from': owner, 'value': eth})
    
    transact_hash = contract_instance.functions.Return_Car(_tokenId, _oil, crashes, rate).transact({'from': renter})
    transact_receipt = web3.eth.getTransactionReceipt(transact_hash)
    logs = contract_instance.events.Price().processReceipt(transact_receipt)
    print(logs[0]['args']['_price'])
    price = logs[0]['args']['_price']
    price = Web3.toWei(price, 'szabo') * 1000
    transact_hash2 = contract_instance.functions.Pay_Owner(_tokenId).transact({'from': renter, 'value': price})
    detail = {'price': price}
    return detail

def Is_Rented(_id):
    transact_hash = contract_instance.functions.Is_Rented(_id).call() #, transact={'from': owner}
    return transact_hash

def Get_Available_Car(_customer):
    transact_hash = contract_instance.functions.Get_Available_Car_Num().call()
    print(transact_hash)

    transact_hash2 = contract_instance.functions.Get_All_Cars().transact({'from': _customer})
    transact_receipt = web3.eth.getTransactionReceipt(transact_hash2)
    logs = contract_instance.events.AvailableCar().processReceipt(transact_receipt)

    car_list = []
    for i in range(transact_hash):
        if logs[i]['args']['_rate_num'] == 0:
            rate = 0
        else:
            rate = logs[i]['args']['_rate_sum'] / logs[i]['args']['_rate_num']
        
        print("ID: {0} Name: {1} Rate: {2}".format(logs[i]['args']['_id'], logs[i]['args']['_name'], rate))
        car_list.append({'ID': logs[i]['args']['_id'], 'Name': logs[i]['args']['_name'], 'Rate': rate})
    return car_list
    
def Get_Renter(_id):
    transact_hash = contract_instance.functions.Get_Renter(_id).call()
    print(type(transact_hash))
    print(transact_hash)
    return transact_hash
'''
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
print('create')
Create_Vtoken('b', 2)
Create_Vtoken('c', 10)
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
print(bool(Is_Rented(0)))
Get_Available_Car()
print('rent')
Rent_Car(0)
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
print(bool(Is_Rented(0)))
Get_Available_Car()
print('return')
Return_Car(0, 1, 0, 5)
print(bool(Is_Rented(0)))
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
Get_Available_Car()
'''
