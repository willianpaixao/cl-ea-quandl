# Quandl External Adapter for Chainlink

### Example with a Solidity Smart Contract
```
pragma solidity ^0.6.0;

import "https://raw.githubusercontent.com/smartcontractkit/chainlink/develop/evm-contracts/src/v0.6/ChainlinkClient.sol";

contract QuandlAPIConsumer is ChainlinkClient {

    uint256 public gdp;

    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    /**
     * Network: Rinkeby
     * Oracle: Chainlink - 0x795FB736ef447f649EBD462F35d6cC8437925fC0
     * Job ID: Chainlink - 32219aca13bc45d8b70e7de95d4ae59d
     * Fee: 0.1 LINK
     */
    constructor() public {
        setPublicChainlinkToken();
        oracle = 0x795FB736ef447f649EBD462F35d6cC8437925fC0;
        jobId = "32219aca13bc45d8b70e7de95d4ae59d";
        fee = 0.1 * 10 ** 18; // 0.1 LINK
    }

    function requestVolumeData() public returns (bytes32 requestId)
    {

        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        request.add("dataset", "FRED/GDP");
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    /**
     * Receive the response in the form of uint256
     */
    function fulfill(bytes32 _requestId, uint256 _gdp) public recordChainlinkFulfillment(_requestId)
    {
        gdp = _gdp;
    }
}
```

### Job Specification
```
{
    "initiators": [
        {
            "type": "runlog",
            "params": {
                "address": "0x795fb736ef447f649ebd462f35d6cc8437925fc0"
            }
        }
    ],
    "tasks": [
        {
            "type": "quandl",
            "confirmations": 0
        },
        {
            "type": "ethuint256"
        },
        {
            "type": "ethtx"
        }
    ]
}
```
