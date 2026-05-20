from fastapi import FastAPI
from routes.product import router

app=FastAPI()

'''
    usage: application root
    rest api url : http:/127.0.0.1:8000
    method type:get
    required fields:none
    access type:public
'''
@app.get('/read')
def product_page():
    return {"msg":"product details"}

app.include_router(router)