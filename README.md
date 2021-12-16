# Autotest interaction with Yandex Pictures

A python test cases for the test problem using selenium

## Table of Contents

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Ref](#ref)


## Installation

To install pychrome, simply:

```
$ pip install pytest
```
To install selenium:
```
$ pip install -U selenium
```

## Getting Started

To test some site, you must change this line:

``` 
self.base_url = "https://your.site/" # in BaseApp.py
```

Then execute pytest in test.py

After running the script, you will see that the browser has opened and followed your link

## Ref

* [Selenium Documentation](https://www.selenium.dev/documentation/)
* [Pytest Documentation](https://docs.pytest.org/en/6.2.x/contents.html)