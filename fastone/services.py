from fastapi import FastAPI
app=FastAPI()

@app.post("/")
def createuser():
    return {"message":"new user created"}

@app.put("/update")
def updateuser():
    return {"message":"new user updated"}

@app.get("/getuser")
def getuser():
    return {"message":"user data retrived"}

@app.delete("/delete")
def deleteuser():
    return{"message":"user deleted"}