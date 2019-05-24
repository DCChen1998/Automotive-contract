const CarBase = artifacts.require("./CarBase.sol");

module.exports = function(deployer) {
  deployer.deploy(CarBase);
};
