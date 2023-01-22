from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


app = FastAPI() #create API object

inventory = {
    1: {
        "name":"Milk",
        "price":3.99,
        "brand": "Regular"
    },
    2: {
        "name":"Butter",
        "price":2.22
    }
}


@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int = Path(None,description="The ID of the item you would like to view")): #PATH adds additional information to documentation at /docs
    return inventory[item_id]

#QUERY PARAMETERS
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int): #name: str = None - means it's optional parameter but it's better to use Optional packet from library
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error":"Item ID already exists."}
    
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]