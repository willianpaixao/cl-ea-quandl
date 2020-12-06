# Changelog

## [v1.0](https://github.com/willianpaixao/cl-ea-quandl/releases/tag/v1.0) - 2020-12-06
First stable version. Basic features are:
* Docker image published to Docker hub at [willianpaixao/cl-ea-quandl](https://hub.docker.com/repository/docker/willianpaixao/cl-ea-quandl)
* Github Actions used for building, testing and deployment
* Environmental variables used to fetch `QUANDL_API_KEY` on runtime
* `production`, `development` or `testing` can be set for `FLASK_ENV` to setup your application environment
* `dataset` and `rows` are the only parameter accepted at the moment
* Pytest is used to run a few raw tests
* Among other features.This is a preliminary release that should receive more documentation and tests soon 