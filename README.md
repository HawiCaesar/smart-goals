[![Build Status](https://travis-ci.org/HawiCaesar/smart-goals.svg?branch=develop)](https://travis-ci.org/HawiCaesar/smart-goals)
[![Coverage Status](https://coveralls.io/repos/github/HawiCaesar/smart-goals/badge.svg?branch=challenge1)](https://coveralls.io/github/HawiCaesar/smart-goals?branch=challenge1)

# Smart Goals

What would you like to do in the next few years? Climbs a mountain? Learn to
ride a bike? It's important to keep track of what you have already done and
what you are yet to achieve.
Smart Goals allows you to register and achieve all these feats and also
allow you to tick off what you have done.

## Prerequistes
The `requirements.txt` file has all requirements for this application

### Installing
Install python on your system

On Linux:
```
sudo apt install python3
```

On Windows:

```
run python-3.5.2.exe
```

Clone the repository using the url:

```
git clone https://github.com/HawiCaesar/smart-goals_app.git
```
Install pip
Install virtual environment and virtual environment wrapper to use this 
You can use pip
```
pip install virtualenv
pip install virtualenvwrapper
```
Activiate your environment (Linux)

```
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv --python=/usr/bin/python3 nameOfEnvironment
```
To get all the requirments like Flask,Jinja, WTF Forms, nosetests
```
pip install -r requirement.txt
```

## Implemented Features
#### Register with the application
#### Create a bucket list(s) and its description
#### View all bucket lists
#### Create a bucket list activity
#### View all bucket list activites


## Tests
To run tests

```
nosetests tests/test_app.py
```

## Authors

* **Brian Hawi Odhiambo**

## Acknowledgements

* Python 3.5 Documentation
* Flask 0.12.2 Documentation
* Various internet resources and Friends
