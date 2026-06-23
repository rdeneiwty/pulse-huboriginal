from flask import Flask, redirect, url_for, render_template, request
#redirect: sends client to different url  | return redirect ('/home')
#url_for: builds a URL for a named route function | url_for('home")
#render_template: renders a Jinja2 HTML template from /templates folder
#request: gives acces to incoming request data

import os
#python standard lib for os interaction
#   filepaths | os.path.join(), os.path.exists()
#   directory ops | os.makedirs(), os.listdir()
#   running shell commands | os.system()

import datetime
#standard lib for working with date and times 
#   datetime.datetime.now()
#   datetime.date.today()
#   datetime.timedelta(days=7)

import click

#3rd party library for building command-line-interfaces(CLIs)
#   @cliack.command() | Turns functions into a CLI Command 
#   -Good for type validation, and autmatic help text 

from flask_sqlalchemy import SQLAlchemy
#3rd party module for working with databases 

#   db.Model | base class for defining tables
#   db.session | add, update, delete, and commit records
#   db.Column() | define column with types 

from sqlalchemy.exc import IntegrityError
#error exception raiseed when a database contraint is violated

from sqlalchemy.orm import DelarativeBase, Mapped, mapped_column
#   DeclarativeBase | Modern SQL Alchemy 2.0 base class for defining ORM Models
#   Mapped | sQLAlcemy 2.0 tpyed way to define model columns
#   mapped_column | goes with mapped

#create app is wrapped in a functions so app is only created
#at function call
def create_app(test_config=None):
    
    #creates my app, tells flask to look for config files in /instance
    app = Flask(__name__, instance_relative_config=True)

    #loads configs from file, silent=True means the app wont crash if file DNE 
    app.config.from_pyfile('config.py', silent=True)
    #SECRET KEY TO SIGN SESSION COOKIES (SEEMS LIKE SECURITY ISSUE <----Further learning neccecary)
    app.config.from_mapping(SECRET_KEY = 'dev')

    #trys to make a local directory for the app /data base files
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///event_database.db"
