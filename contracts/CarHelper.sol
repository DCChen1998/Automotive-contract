pragma solidity ^0.5.0;
import "./CarRenter.sol";

contract CarHelper is CarRenter {
    modifier OnlyOwnerOf(uint16 _id) {
        require(vtokens[_id].owner == msg.sender);
        _;
    }
    
    function ChangeName(uint16 _id, string memory _newname) public OnlyOwnerOf(_id) {
        vtokens[_id].car.name = _newname;
    }

    function ChangeAge(uint16 _id, uint16 _age) public OnlyOwnerOf(_id) {
        vtokens[_id].car.age = _age;
    }
}