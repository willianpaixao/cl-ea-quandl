# Chainlink external adapter for Quandl API

![Build](https://github.com/willianpaixao/cl-ea-quandl/workflows/Build%20and%20push%20Docker%20image/badge.svg?branch=master)
![CodeQL](https://github.com/willianpaixao/cl-ea-quandl/workflows/CodeQL/badge.svg?branch=master)

## Getting started
**REQUIRED:** First step is creating an account at [Quandl](https://www.quandl.com/sign-up) and creating an API key.

Once you have it, simply run the image:
``` bash
$ docker container run --detach --name cl-ea-quandl --publish 8080:8080 --env QUANDL_API_KEY=[INSERT HERE YOUR KEY] willianpaixao/cl-ea-quandl:latest
```
> NOTE: don't forget to replace with your API key

To quickly test, make a request using `curl`:
``` bash
$ curl localhost:8080?dataset=FRED%2FGDP
21157.635
```

## Quandl API
Now that you have a running adapter, look at the [Quandl API documentation](https://docs.quandl.com) for all possible parameters that can be passed
and at the [Quandl feed explorer](https://www.quandl.com/search) to pick the data you need.

## Development
You can easily build with Docker, by running:
``` bash
$ docker image build -t cl-ea-quandl:latest .
```