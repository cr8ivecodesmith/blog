Matt Lebrun's Blog
==================

NOTE:

Clone this repo then clone the theme repo within this directory.


## Requirements

- Ubuntu 16.04+
- Python 3.5+
- Git
- [Zenmatt](https://github.com/cr8ivecodesmith/zenmatt) theme


## Development setup

1) Make a virtual environment and install the requirements

```
$ python3 -m venv v
$ . v/bin/activate
(v) $ pip install -r requirements.txt
```

2) Run the dev server

```
(v) $ ./develop_server.sh start
```

3) Open your [browser](http://localhost:8000)

4) Deploy changes

```
(v) $ make github
```
