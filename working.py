from fastapi import FastAPI, Path, HTTPException, status 
from typing import Optional
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

@app.get("/")
def home():
    return {"Data": "Test"}

@app.get("/about")
def about():
    return {"Data":"about"}

@app.get("/item/{item_id}")
def get_item(item_id: int = Path(description="The id of the item")):
    return inventory[item_id]

@app.get("/get-by-name/{item_id}")
def get_item(item_id: int, name: Optional[str] = None):
    for item in inventory:
        if inventory[item].name == name:
            return inventory[item]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


inventory = {}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item_id already exists"}
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}    
    return inventory[item_id]  


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
     if item_id not in inventory:
         return {"Error": "Item ID does not exists"}
     inventory[item_id].update(item)
     
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id in inventory:
        del inventory[item_id]
    else:
        {"Error":"Item ID doesnt not exists"}