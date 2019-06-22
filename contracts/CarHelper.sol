pragma solidity ^0.5.0;
import "./CarBase.sol";
import "./erc721.sol";

contract CarHelper is CarBase {
    modifier OnlyOwnerOf(uint _id) {
        require(cars[_id].owner == msg.sender, "Not the owner!");
        _;
    }
    
    function ChangeName(uint _id, string memory _newname) public OnlyOwnerOf(_id) {
        cars[_id].name = _newname;
    }

    function ChangeAge(uint _id, uint _newage) public OnlyOwnerOf(_id) {
        cars[_id].age = _newage;
    }
}

contract CarOwnership is CarBase, ERC721 {
    string public constant name = "Vtoken";
    string public constant symbol = "V";

    function balanceOf(address _owner) public view returns (uint256 _balance) {
        return ownerTokenCount[_owner];
    }

    function ownerOf(uint _tokenId) public view returns (address _owner) {
        return cars[_tokenId].owner;
    }

    function approve(address _to, uint _tokenId) public { // approval is used for renting car
        address payable addr = address(uint160(_to)); //turn _to from address to address payable
        cars[_tokenId].renter = addr;

        emit Approval(cars[_tokenId].owner, _to, _tokenId);
    }

    function getApproved(uint _tokenId) public view returns(address _operator) {
        address addr = cars[_tokenId].renter;
        return addr;
    }

    function transferFrom(address _from, address _to, uint _tokenId) public {
        require(msg.sender == _from && _from == cars[_tokenId].owner, "Failed to tranfer!");

        address payable addr_to = address(uint160(_to));
        /*address payable addr_from = address(uint160(_from));*/
        car2owner[_tokenId] = addr_to;
        ownerTokenCount[_from].sub(1);
        ownerTokenCount[_to].add(1);
        cars[_tokenId].owner = addr_to;
        emit Transfer(_from, _to, _tokenId);
    }
}