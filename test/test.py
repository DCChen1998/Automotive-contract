#from web3utils.web3 import Web3, HTTPProvider
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
#from web3utils.web3.contract import ConciseContract
#from web3.utils.currency import to_wei
#from web3utils.currency import to_wei


config = {
    "abi": [
    {
      "constant": True,
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "getApproved",
      "outputs": [
        {
          "name": "_operator",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_from",
          "type": "address"
        },
        {
          "name": "_to",
          "type": "address"
        },
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        },
        {
          "name": "_newname",
          "type": "string"
        }
      ],
      "name": "ChangeName",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "ownerOf",
      "outputs": [
        {
          "name": "_owner",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "Get_All_Cars",
      "outputs": [
        {
          "name": "",
          "type": "uint16[]"
        },
        {
          "name": "",
          "type": "address[]"
        },
        {
          "name": "",
          "type": "uint16[]"
        },
        {
          "name": "",
          "type": "uint16[]"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "name": "_balance",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [],
      "name": "renounceOwnership",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "name": "",
          "type": "address"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "isOwner",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "name": "",
          "type": "string"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": True,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        }
      ],
      "name": "Is_Rented",
      "outputs": [
        {
          "name": "",
          "type": "bool"
        }
      ],
      "payable": False,
      "stateMutability": "view",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_id",
          "type": "uint256"
        },
        {
          "name": "_newage",
          "type": "uint16"
        }
      ],
      "name": "ChangeAge",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "transferOwnership",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_from",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "_to",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "_owner",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "_approved",
          "type": "address"
        },
        {
          "indexed": False,
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "name": "_id",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "_renter",
          "type": "address"
        }
      ],
      "name": "RentCar",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "name": "_id",
          "type": "uint256"
        },
        {
          "indexed": False,
          "name": "_name",
          "type": "string"
        }
      ],
      "name": "NewCar",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "name": "_price",
          "type": "uint256"
        }
      ],
      "name": "Price",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "name": "previousOwner",
          "type": "address"
        },
        {
          "indexed": True,
          "name": "newOwner",
          "type": "address"
        }
      ],
      "name": "OwnershipTransferred",
      "type": "event"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_name",
          "type": "string"
        },
        {
          "name": "_age",
          "type": "uint16"
        }
      ],
      "name": "Create_Vtoken",
      "outputs": [],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "Rent_Car",
      "outputs": [],
      "payable": True,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        },
        {
          "name": "_oil",
          "type": "uint256"
        },
        {
          "name": "crashes",
          "type": "uint16"
        },
        {
          "name": "rate",
          "type": "uint16"
        }
      ],
      "name": "Return_Car",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": False,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "Pay_Owner",
      "outputs": [],
      "payable": True,
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "constant": False,
      "inputs": [
        {
          "name": "_tokenId",
          "type": "uint256"
        }
      ],
      "name": "Return_Bail",
      "outputs": [],
      "payable": True,
      "stateMutability": "payable",
      "type": "function"
    }
  ],
    "address": "0x6abf02023A05B19b3dDB488ACcc6cB8C5f963ad3",
}

web3 = Web3(HTTPProvider('http://localhost:8545'))
owner = web3.eth.accounts[0]
customer = web3.eth.accounts[1]
contract_instance = web3.eth.contract(address=config['address'], abi=config['abi']) 
eth = Web3.toWei(1, 'ether')


def Create_Vtoken(_name, _age):
    transact_hash = contract_instance.functions.Create_Vtoken(_name, _age).transact({'from': owner})
    return transact_hash

def Rent_Car(_tokenId):
    transact_hash = contract_instance.functions.Rent_Car(_tokenId).transact({'from': customer, 'value': eth})
    return transact_hash

def Return_Car(_tokenId, _oil, crashes, rate):
    #transact_hash = contract_instance.Return_Car(_tokenId, _oil, crashes, rate, transact={'from': customer})
    '''
    if (crashes == 0):
       transact_hash2 = contract_instance.Return_Bail(_tokenId, transact={'from': owner, 'value': eth})
    '''
    transact_hash = contract_instance.functions.Return_Car(_tokenId, _oil, crashes, rate).transact({'from': customer})
    transact_receipt = web3.eth.getTransactionReceipt(transact_hash)
    logs = contract_instance.events.Price().processReceipt(transact_receipt)
    print(logs[0]['args']['_price'])
    price = logs[0]['args']['_price']
    price = Web3.toWei(price, 'szabo') * 1000
    transact_hash2 = contract_instance.functions.Pay_Owner(_tokenId).transact({'from': customer, 'value': price})
    #transact_hash2 = contract_instance.Pay_Owner(_tokenId, transact={'from': customer, 'value': price})
    
    return transact_hash

def Is_Rented(_id):
    transact_hash = contract_instance.functions.Is_Rented(_id).call() #, transact={'from': owner}
    return transact_hash

#print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
#print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
#Create_Vtoken('b', 2)
#Return_Car(0,1,1)
Rent_Car(0)
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))
print(bool(Is_Rented(0)))
Return_Car(0, 1, 1, 5)
print(bool(Is_Rented(0)))
print(Web3.fromWei(web3.eth.getBalance(owner), 'ether'))
print(Web3.fromWei(web3.eth.getBalance(customer), 'ether'))