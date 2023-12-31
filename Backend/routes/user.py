from fastapi import APIRouter, HTTPException
from db.userdb import getUsers, create_user, deleteUser, get_userId, update_user
from schemas.user import createUser, responseUser, updateUser
import uuid

user = APIRouter()



@user.get("/user", response_model=list[responseUser], tags=["user"])
def get_users():
    return getUsers()



@user.get("/user/{id}", response_model=responseUser, tags=["user"])
def get_user_by_id(id: uuid.UUID):
    try:
        user = get_userId(id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")



@user.post("/user", tags=["user"])
def create_new_user(user: createUser):
    try:
        new_user = create_user(user)
        return new_user
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error: User creation failed")



@user.put("/user/{id}", response_model=responseUser, tags=["user"])
def update_user_by_id(id: uuid.UUID, updated_user: updateUser):
    try:
        user = update_user(id, updated_user)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    


@user.delete("/user/{id}", tags=["user"])
def delete_user(id: uuid.UUID):  # Asegúrate de que el parámetro id sea de tipo str
    
    try:
        deleted_user = deleteUser(id)

        if deleted_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return deleted_user
    
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
