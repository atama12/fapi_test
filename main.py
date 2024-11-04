from fastapi import FastAPI

app = FastAPI()

@app.get("/items/me")
def items_me():
    return {"message":"current user"}

@app.get("/items/{item_id}")
def items_item_id(item_id:int):
    return {"message":item_id}