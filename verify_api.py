import httpx
import time

URL = "http://127.0.0.1:8000"

def verify_api():
    try:
        # Create an item
        print("Creating item...")
        response = httpx.post(f"{URL}/items/", json={"name": "Test Item", "price": 10.5})
        assert response.status_code == 200
        print("Item created:", response.json())
        
        # Read items
        print("Reading all items...")
        response = httpx.get(f"{URL}/items/")
        assert response.status_code == 200
        items = response.json()
        assert len(items) > 0
        print("Items:", items)
        
        item_id = int(list(items.keys())[0])
        
        # Read specific item
        print(f"Reading item {item_id}...")
        response = httpx.get(f"{URL}/items/{item_id}")
        assert response.status_code == 200
        print("Item read:", response.json())
        
        # Update item
        print(f"Updating item {item_id}...")
        response = httpx.put(f"{URL}/items/{item_id}", json={"name": "Updated Item", "price": 20.0})
        assert response.status_code == 200
        print("Item updated:", response.json())
        
        # Read updated item
        print(f"Reading updated item {item_id}...")
        response = httpx.get(f"{URL}/items/{item_id}")
        assert response.json()["name"] == "Updated Item"
        print("Item verified updated.")

        # Delete item
        print(f"Deleting item {item_id}...")
        response = httpx.delete(f"{URL}/items/{item_id}")
        assert response.status_code == 200
        print("Item deleted.")
        
        # Verify deletion
        print(f"Verifying deletion of item {item_id}...")
        response = httpx.get(f"{URL}/items/{item_id}")
        assert response.status_code == 404
        print("Item verified deleted.")
        
        print("\nAll tests passed!")

    except Exception as e:
        print(f"\nTest failed: {e}")

if __name__ == "__main__":
    verify_api()
