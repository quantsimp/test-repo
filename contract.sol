// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedValue;
event StoredValueUpdated(uint256 oldValue, uint256 newValue, address updatedBy);

    constructor(uint256 _initialValue) {
        storedValue = _initialValue;
    }

	uint256 oldValue = storedValue;
	storedValue = _newValue;
	emit StoredValueUpdated(oldValue, _newValue, msg.sender);
        storedValue = _newValue;
    }

    function getStoredValue() public view returns (uint256) {
        return storedValue;
    }
}