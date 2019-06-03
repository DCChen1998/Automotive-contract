pragma solidity ^0.5.0;

import "./CarHelper.sol";

contract CarRenter is CarHelper, CarOwnership {
    uint16 basic_renttime = 1;
    
    function Create_Vtoken(string memory _name, uint16 _age) public { //called by car wallet
        Add_Car(_name, _age, msg.sender);
    }
    
    function Rent_Car(uint _tokenId) public payable { //called by user
        require(Is_Rented(_tokenId) == false && msg.value >= 1 ether, "Failed to rent a car!");
        cars[_tokenId].rent_time = now + basic_renttime;
        approve(msg.sender, _tokenId);
        cars[_tokenId].owner.transfer(1 ether); //for bail
        AvailableCarNum--;
        emit RentCar(_tokenId, msg.sender, cars[_tokenId].owner);
    }

    function Return_Car(uint _tokenId, uint _oil, uint16 crashes, uint16 rate) public /*payable*/ returns(uint) {
        require(msg.sender == cars[_tokenId].renter, "Failed to return a car!");
        uint to_owner;
        //uint to_renter; //return the bail

        cars[_tokenId].renter = cars[_tokenId].owner;
        cars[_tokenId].rate_sum += rate;
        cars[_tokenId].rate_num++;

        to_owner = Calculate_Price(_tokenId, _oil, crashes);
        emit Price(to_owner);
        return to_owner;
        /*
        if (now <= cars[_tokenId].rent_time && crashes == 0) { // no crash and return on time
            to_renter = 1;
            to_owner = cars[_tokenId].price + _oil * 50;
            msg.sender.transfer(1 ether);
            cars[_tokenId].owner.transfer(to_owner * 1 szabo);
        }
        else {
            to_owner = cars[_tokenId].price + _oil * 50;
            if (crashes != 0){
                to_owner += crashes * 10;
            }
            cars[_tokenId].owner.transfer(to_owner * 1 szabo);
        }
        */
    }

    function Pay_Owner(uint _tokenId) public payable {
        cars[_tokenId].owner.transfer(msg.value);
        AvailableCarNum++;
    }

    function Return_Bail(uint _tokenId) public payable {
        cars[_tokenId].renter.transfer(msg.value);
    }

}
