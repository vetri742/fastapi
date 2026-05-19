from fastapi import FastAPI
from routes.userrouter import router

# Create a fastapi application
app=FastAPI()


'''
usage:Applicaton root
Rest api url:http://127.0.0.1:8000/
method type:GET
required fields:None
access type: public

'''
@app.get('/')
def userroot():
    return {'MSG':'APPLICATION USER ROOT'}

'''
usage:Applicaton about
Rest api url:http://127.0.0.1:8000/about
method type:GET
required fields:None
access type: public
'''

@app.get('/about')
def aboutuser():
    return {'msg':'Application about user'}

app.include_router(router)
