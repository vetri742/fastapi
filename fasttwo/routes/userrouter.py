from fastapi import APIRouter

# create a mini route manager
router=APIRouter(prefix='/users')
'''
usage:Applicaton all users
Rest api url:http://127.0.0.1:8000/users/read
method type:GET
required fields:None
access type: public
'''

@router.get('/read')
def user_route_read():
    return {'msg':'fetched all user details'}

