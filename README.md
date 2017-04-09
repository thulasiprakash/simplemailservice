# Simple Mail Service
Please follow the below instructions to setup Simple Mail Service Application

## Why?
   ### Angular
   - Better Plug & Play Components
   - Faster application development
   - Allows Parallel Development
   - Handless Dependencies
   ### Flaskweb
   - Built-in development server and debugger
   - Restful request dispatching
   - Integrated unit testing
   ### Send Grid
   - Low cost
   - Easy to integrate
   - Great documentation
   ### Heroku
   - Very easy to integrate add-ons like Send Grid, PostGresSql, etc.
   - Easy to get started, only need to install heroku toolkit.
   - Simple deployment procedure. 
## Setup 
**For Linux/Mac OS** 
   1. Install Flask 
      ```   
      $ sudo pip install virtualenv
      ```
      ```
      $ sudo apt-get install python-virtualenv
      ```
      ```
      cd simplemailservice
      ```
      ```
      virtualenv venv
      ```
      ```
      . venv/bin/activate
      ```
      > Flask activated in your virtualenv:
      ```
      $ pip install Flask
      ```
      > System Wide Installation
      ```
      $ sudo pip install Flask
      ```
   2. Install Send Grid
      ```
      pip install sendgrid
      ```
**For Windows** http://flask.pocoo.org/docs/0.12/installation/#windows-easy-install
## Run application
   `python app.py`

To see a **demo deployed on heroku** visit : https://peaceful-castle-40736.herokuapp.com/
