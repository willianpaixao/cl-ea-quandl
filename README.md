``` bash
docker image build -t cl-ea-quandl:latest .
```

``` bash
docker container run --rm --detach --name cl-ea-quandl --publish 8080:8080 --env QUANDL_API_KEY=[INSERT HERE YOUR KEY] cl-ea-quandl:latest
```
