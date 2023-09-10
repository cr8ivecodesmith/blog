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

2) Clone the [zenmatt](https://github.com/cr8ivecodesmith/zenmatt) theme

```
(v) $ git clone git@github.com:cr8ivecodesmith/zenmatt.git
```

3) Copy the favicon to the theme folder

```
(v) $ cp favicon.ico zenmatt/static/img/
```

4) Run the dev server

```
(v) $ make html; PORT=8000 make serve-global
```

5) Open your [browser](http://localhost:8000)

6) Deploy changes

```
(v) $ make github
```
