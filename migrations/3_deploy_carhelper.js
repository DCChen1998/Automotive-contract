const CarHelper = artifacts.require("./CarHelper.sol");

module.exports = function(deployer) {
  deployer.deploy(CarHelper);
};
