# Chainlink external adapter for Quandl API

![Test, Build and push Docker image](https://github.com/willianpaixao/cl-ea-quandl/workflows/Test,%20Build%20and%20push%20Docker%20image/badge.svg?branch=master)
![CodeQL](https://github.com/willianpaixao/cl-ea-quandl/workflows/CodeQL/badge.svg?branch=master)
![Snyk](https://github.com/willianpaixao/cl-ea-quandl/workflows/Snyk%20vulnerability%20scan/badge.svg?branch=master)

## Getting started
**REQUIRED:** First step is creating an account at [Quandl](https://www.quandl.com/sign-up) and creating an API key.

Once you have it, simply run the image:
``` bash
$ docker container run --rm --detach --name cl-ea-quandl --publish 8080:8080 --env QUANDL_API_KEY=[INSERT HERE YOUR KEY] willianpaixao/cl-ea-quandl:latest
```
> NOTE: don't forget to replace with your API key

To quickly test, make a request using `curl`:
``` bash
$ curl --request POST --header "Content-Type: application/json" --data '{"id": 1, "data": {"dataset": "FRED/GDP"}}' localhost:8080
{
  "data": 21157.635, 
  "jobRunID": 1, 
  "result": 21157.635, 
  "statusCode": 200
}
```

## Quandl API
Now that you have a running adapter, look at the [Quandl API documentation](https://docs.quandl.com) for all possible parameters that can be passed
and at the [Quandl feed explorer](https://www.quandl.com/search) to pick the data you need.

### Examples
You can explore the free (as in "free of charge") data feeds [here](https://www.quandl.com/search?filters=%5B%22Free%22%5D).
Most common usages are for macroeconomic data and financial indexes, some examples are:

| Dataset           | Description                      |
| ----------------- | -------------------------------- |
|`FRED/GDP`         | USA's Gross Domestic Product     |
|`FRED/UNRATE`      | USA's Civilian Unemployment Rate |
|`FRED/GFDEBTN`     | USA's Federal Public Debt        |
|`NASDAQOMX/OMXS30` | OMX Stockholm 30 Index           |
|`BCB/11`           | Brazilian interest rate          |

> NOTE: You can purchase a premium feed but this is out of the scope of this service.

## Development
You can easily build with Docker, by running:
``` bash
$ docker image build --tag cl-ea-quandl:latest .
```
### Testing
Make sure you have installed all dependencies using `Pipfile`, then run:
```
$ FLASK_ENV=testing pytest --setup-show
```