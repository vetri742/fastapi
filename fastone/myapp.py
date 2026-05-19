from fastapi import FastAPI

app=FastAPI()

'''
Usage:Application root
RestAPIurl:http://localhost:8000/
method type: get 
required fields:none
access type:public

'''

@app.get("/")
def index_page():
    return {"message":"Index page"}

'''
Usage: About page
RestAPIurl:http://localhost:8000/about
method type: get 
required fields:none
access type:public

'''
@app.get("/about")
def about_page():
    return {"message":"About page"}

@app.get("/services")
def services():
    return{ "player name":"virat kohli"}
