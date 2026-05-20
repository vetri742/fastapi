from fastapi import APIRouter
from typing import Optional

router=APIRouter(prefix="/products")

# Dummy data

product=[
    {"id":1,"name":"bat","category":"sports","price":5000},
    {"id":2,"name":"ball","category":"sports","price":2000},
    {"id":3,"name":"book","category":"studies","price":10000},
    {"id":4,"name":"tv","category":"furniture","price":64000}
]

'''
usage:application product list
restapi url:http://127.0.0:8000/products/productdetails
method type:get
required fields:none
access type : public

'''

@router.get("/productdetails")
def product_details():
    return product


'''
usage:application product by id
restapi url:http://127.0.0:8000/products/productdetails/id
method type:get
required fields:none
access type : public

'''
@router.get("/{productid}")
def product_id(productid:int):
    for i in product:
        if i['id']==productid:
            return i
    return {"msg": "item does not exist"}


'''
usage:application product by filter
restapi url:http://127.0.0:8000/products/productdetails?category=sports
method type:get
required fields:none
access type : public

'''

@router.get('/')
def product_category(category:Optional[str]=None):
    filter_products=[]
    for i in product:
        if category==i['category']:
            filter_products.append(i)
    return filter_products