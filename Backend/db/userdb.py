from schemas.user import responseUser, createUser, updateUser
from models.user import users
import uuid
from db.db import SessionLocal

def create_user(user: createUser):
    try:
        db = SessionLocal()
        new_user = users(nombre=user.nombre, edad=user.edad, correo=user.correo)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close_all()



# Función para obtener todos los usuarios
def getUsers():
    db = SessionLocal()
    users_db = db.query(users).all()
    db.close()
    return users_db



def get_userId(id: uuid.UUID):
    try:
        db = SessionLocal()
        user = db.query(users).filter(users.id == id).first()
        db.close()

        return user
    except Exception as e:
        raise e
    


def update_user(id: uuid.UUID, updated_user: updateUser):
    try:
        db = SessionLocal()
        user = db.query(users).filter(users.id == id).first()

        if user:
            # Actualizar los campos del usuario con los valores proporcionados en updated_user
            user.nombre = updated_user.nombre
            user.edad = updated_user.edad
            user.correo = updated_user.correo

            db.commit()
            db.refresh(user)

            db.close()
            return user
        else:
            db.close()
            return None
    except Exception as e:
        db.rollback()
        raise e



# Función para eliminar un usuario por su ID
def deleteUser(id: uuid.UUID):
    db = SessionLocal()
    user = db.query(users).filter(users.id == id).first()  # Cambio aquí: users.id en lugar de users.c.id

    if user:
        db.delete(user)
        db.commit()

    db.close()

    return user
