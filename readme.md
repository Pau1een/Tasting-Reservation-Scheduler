# Take Home Challenge: Melon Tasting Reservation Scheduler App

## Contents

* [Setup](#setup)
  * [Install Python dependencies](#install-python-dependencies)
  * [Initialize the database](#initialize-the-database)
  * [Run Flask server](#run-flask-server)
* [File structure](#file-structure)
* [Flask routes](#flask-routes)
  * [`GET` /](#get-)
  * [`POST` /login](#post-login)
    * [Request parameters](#request-parameters)
  * [`POST` /register](#post-register)
    * [Request parameters](#request-parameters-1)
  * [`GET` /goals](#get-goals)
  * [`POST` /goal/new](#post-goalnew)
    * [Request parameters](#request-parameters-2)
  * [`POST` /goal/<goal_id>/edit](#post-goalgoal_idedit)
  * [Request parameters](#request-parameters-3)

<!-- vim-markdown-toc -->

## Setup

Before you begin the setup and installation process below, you'll need to have
the following installed:

- Python 3.0 or above
- PostgreSQL 11

### Install Python dependencies

Create a virtual environment

```
python3 -m venv env

# Alternatively, if you have virtualenv installed
virtualenv env
```

Activate the environment and install dependencies from `requirements.txt`

```
source env/bin/activate
pip3 install -r requirements
```

### Initialize the database

Create a PostgreSQL database called `melon`

```
createdb melon
```

Run this command to create tables and test data

```
python3 model.py --init
```

### Run Flask server

Now you can run the server with

```
python3 server.py
```

The site will be accessible at http://localhost:5000.

## File structure

static/
  Contains static assets. 
  `login.css`
  `reservations.css`
  `search.css`
  `login.jpg`
  `reservations.jpg`
  `melon.jpg`
      
templates/
  Jinja2 templates
model.py
  Database schema and ORM classes written with SQLAlchemy
server.py
  Flask routes

