from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# simple get and post apis using fastAPI

items = ["apple", "mango", "oramge", "banana"]

@app.get("/")
def root():
    return {"Hello","World"}

@app.post("/items")
def create_items(item: str):
    if(item in items):
     return items
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_items(item_id: int):
    if(item_id < len(items)):
     return items[item_id];
    else:
      raise HTTPException( status_code=404, detail=f'item {item_id} not found') 
    

# simple get and post apis using fastAPI that takes json payload to create a simple todo list

todoList = []
class Item(BaseModel):
   text: str
   is_done: bool = False

@app.post("/set/todolist")
def create_items(item: Item):
    if(item in todoList):
     return todoList
    todoList.append(item)
    return todoList