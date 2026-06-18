from fastapi import  FastAPI 

app = FastAPI()
contacts = {
    1: {
        "name": "Kiran",
        "phone": 9876543210
    },
    2: {
        "name": "Light",
        "phone": 8329328238
    }
}

@app.get("/home/{user}")
def home(user:str):
    return f"{"Hello":{user}}"

@app.get("/contacts")
def show_contacts():
    return contacts

@app.post("/contacts/{id}")
def add_contact(id: int, name: str, phone: str):

    contacts[id] = {
        "name": name,
        "phone": phone
    }

    return {
        "message": "Contact Added",
        "data": contacts[id]
    }

@app.put("/contacts/{id}")
def update_contact(id: int, name: str, phone: str):

    if id not in contacts:
        return {"error": "Contact not found"}

    contacts[id] = {
        "name": name,
        "phone": phone
    }

    return {
        "message": "Updated Successfully",
        "data": contacts[id]
    }


@app.delete("/contacts/{id}")
def delete_contact(id: int):

    if id not in contacts:
        return {"error": "Contact not found"}

    deleted = contacts.pop(id)

    return {
        "message": "Deleted Successfully",
        "deleted": deleted
    }

