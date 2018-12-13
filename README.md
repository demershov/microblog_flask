## A small microblogging on the flask with api.
View - https://mblog-flask.herokuapp.com/ (Search does not work).

Commands to run a project:

    λ git clone https://github.com/dm1tr/microblog_flask.git
    
    λ cd microblog_flask
    # Create a virtual environment
    λ python -m venv venv
    # Once you’ve created a virtual environment, you may activate it.
    # On Unix or MacOS, run:
    λ source venv/bin/activate
    # On Windows, run
    λ venv\Scripts\activate.bat
    
    λ pip install -r requirements.txt
    # Set Environment Variable on Linux
    λ export FLASK_APP=microblog.py
    # Set Environment Variable on Window
    λ set FLASK_APP=microblog.py
    λ flask run
	  # If you want to enable search, you need to run elasticsearch.

