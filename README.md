## SVP - A Python-based API testing microframework
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/joshmgrant/svp) 
[![CircleCI](https://circleci.com/gh/joshmgrant/svp.svg?style=svg)](https://circleci.com/gh/joshmgrant/svp)


Automating testing is no easy task. Luckily, we're here to help - with API testing. All you need to do is ask.

## Why a microframework? 

The goal of this project is to be as lightweight as possible and make use of common Python approaches and libraries. We depend on [requests](https://requests.kennethreitz.org/en/master/) to do most of the actual API-level work, and endeavour to only have a small number of files that could be copied into projects if needed.

## Installation

The latest version of SVP can be installed via pip

```
pip install svp
```

or this repository can be cloned and SVP can be installed directly

```
python setup.py install
```


### Usage

The goal of SVP is to provide lightweight help to get an API testing framework up and running. The main component of the project is the `API` class, which is designed to be subclassed. This provides all the basic functionality needed to wrap the API under test into neat methods, including the usual GET, POST, PUT, PATCH and DELETE verbs for HTTP requests.

Each `API` instance methods return an `APIResponse`, which is a wrapper class around a request response. `APIResponse`s allow for neat and tidy testing since they are dictionaries, so assertions can look like this:

```python
response = api.get_account_details('id#123')

assert response['accountName'] == 'Josh'
```

Instead of raising an error if particular fields aren't present, `APIResponse` simply returns `None` if the key doesn't exist. Also provided are constructs such as status code, content and headers, also easily accessible in a dict-like format.

Also provided are some `APIAssert` utility functions to make assertions a bit easier for routine checking such as if status codes are 200- or 400-level codes.

### Please - I need help

This is a lightweight project that is also early in its development. Please post an issue if you'd like some help or [find me on Twitter](https://twitter.com/joshin4colours) if you'd like.

### Additional Resources

- [Requests project](https://requests.kennethreitz.org/en/master/)
- [Pytest project](https://pytest.org/en/latest/)
- [Sample API templates in a variety of languages](https://github.com/mwinteringham/api-framework)
