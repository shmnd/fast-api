from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float | None = None

# Simulate a database
fake_items_db: Dict[int, Item] = {}
current_id = 0

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    global current_id
    current_id += 1
    fake_items_db[current_id] = item
    return item

@app.get("/items/", response_model=Dict[int, Item])
async def read_items():
    return fake_items_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemUpdate):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    stored_item_data = fake_items_db[item_id].model_dump()
    update_data = item.model_dump(exclude_unset=True)
    updated_item = fake_items_db[item_id].model_copy(update=update_data)
    fake_items_db[item_id] = updated_item
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del fake_items_db[item_id]
    return {"detail": "Item deleted"}
