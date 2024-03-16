# flask-tutorial

Basic blog application on python to learn flask and github ci/cd. It's based on the official [Flask tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/).

Table of content
- [Installation instructions](#installation-instructions)
  - [Getting the project code](#getting-the-project-code)
  - [Virtual environment](#virtual-environment)
  - [Project dependencies](#project-dependencies)
- [Project structure](#project-structure)
- [Run The App](#run-the-app)
  - [Start the server](#start-the-server)
  - [In browser](#in-browser)
- [Testing](#testing)
- [Resorces](#resorces)

## Installation instructions

### Getting the project code

```sh
$ git clone https://github.com/yurkov74/flask-tutorial.git
```

### Virtual environment

```sh
cd flask-tutorial                     # go to the project's folder
# linux
python3 -m pip install --upgrade pip          # upgrade global pip
python3 -m venv venv                          # install virtual environment
source venv/bin/activate                      # activate virtual environment
(venv) python3 -m pip install --upgrade pip   # upgrade pip in the venv
# windows
pip install --upgrade pip                     # upgrade global pip
python -m venv venv                           # install virtual environment
venv/bin/activate                             # activate virtual environment
(venv) python -m pip install --upgrade pip    # upgrade pip in the venv
```

Deactivate virtual environment:
```sh
(venv) deactivate
```

### Project dependencies
```sh
(venv) pip install -r requirements.txt        # app dependencies
(venv) pip install -r requirements.dev.txt    # dev and testing dependencies
```

### Install the project

To work properly project needs to be installed into the virtual environment. This step requires pyproject.toml file to be in the project's root.

```
(venv) pip install -e .
```

This tells pip to find pyproject.toml in the current directory and install the project in editable or development mode. Editable mode means that as you make changes to your local code, you’ll only need to re-install if you change the metadata about the project, such as its dependencies.

You can observe that the project is now installed with 'pip list'.

## Project structure

Main folders
- flaskr/, a Python package containing your application code and files.
- flaskr/templates, templates are files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document. Flask uses the Jinja template library to render templates.
- flaskr/static, static files for our web app.
- tests/, a directory containing test modules.
- venv/, a Python virtual environment where Flask and other dependencies are installed.

Full scheme
```
flask-tutorial/
├── flaskr/
│   ├── static/
│   |   └── style.css
│   ├── templates/
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── blog/
│   │   │   ├── create.html
│   │   │   ├── index.html
│   │   │   └── update.html
│   │   └── base.html
│   ├── __init__.py
│   ├── auth.py
│   ├── blog.py
│   ├── db.py
│   └── schema.sql
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── hello.py
├── LICENCE
├── MANIFEST.in
<!-- ├── pyproject.toml -->
├── README.md
├── requirements.dev.txt
└── requirements.txt
```

## Run The App

### Initialize DB

The blog app is using SQLite DB natively supported by python. The db file by default is stored in the instance folder and before the first run you need to create it by running the following command:

```
(venv) flask --app flaskr init-db
```

DB file (flaskr.sqlite by default) should appear in the instance folder.

### Start the server

```
(venv) flask --app hello run              # run the simplest single-file app
(venv) flask --app flaskr run             # run the blog app
(venv) flask --app flaskr run --debug     # run the app in the debug mode
```

### In browser

- http://127.0.0.1:5000: app home page
- http://127.0.0.1:5000/hello: test page in the blog app
- http://127.0.0.1:5000/auth/register: register a user


## Testing

To test the project, collect test stats and measure the  coverage pytest and coverage libraries are used.

```
(venv) pytest                                     # run unit tests with default configuration
(venv) pytest -v                                  # run tests in the verbose mode
(venv) coverage run -m pytest                     # measure the code coverage of the tests
(venv) coverage report                            # generate coverage report in the terminal
(venv) coverage html                              # generate html coverage report
# linux
(venv) coverage run -m pytest && coverage report  # run both commands together
(venv) coverage run -m pytest && coverage html    # run both commands together
# windows
(venv) coverage run -m pytest; coverage report    # run both commands together
(venv) coverage run -m pytest; coverage html      # run both commands together
```

## Resorces

- [Flask official tutorial](https://flask.palletsprojects.com/en/3.0.x/tutorial/)
- [Flask CLI](https://flask.palletsprojects.com/en/3.0.x/cli/)
- [Jinja templates](https://jinja.palletsprojects.com/templates/)