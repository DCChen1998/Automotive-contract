from flask import Flask, jsonify, request
import CarRenter

app = Flask(__name__)
users = [{'owner': CarRenter.owner, 'customer': CarRenter.customer}]

#get /user
@app.route('/user')
def get_users():
    return jsonify(users)

#get /car
@app.route('/car')
def get_cars():
    return jsonify(CarRenter.Get_Available_Car())



app.run(port=5000, debug=True)#host=

'''
Create_Vtoken(_name, _age)
Rent_Car(_tokenId)
Return_Car(_tokenId, _oil, crashes, rate)
Is_Rented(_id)
Get_Available_Car()
owner = web3.eth.accounts[0]
customer = web3.eth.accounts[1]
'''
#print(CarRenter.owner, CarRenter.customer)