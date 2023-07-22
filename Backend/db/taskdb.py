from schemas.task import createTask, updateTask
from models.task import tasks
import uuid
from db.db import SessionLocal



def create_task(task: createTask):
    try:
        db = SessionLocal()
        new_task = tasks(userId=task.userId, tarea=task.tarea, idState=task.idState)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close_all()



# Función para obtener todos los usuarios
def getTasks():
    db = SessionLocal()
    tasks_db = db.query(tasks).all()
    db.close()
    return tasks_db



def get_taskId(id: uuid.UUID):
    try:
        db = SessionLocal()
        task = db.query(tasks).filter(tasks.id == id).first()
        db.close()

        return task
    except Exception as e:
        raise e
    


def update_task(id: uuid.UUID, updated_task: updateTask):
    try:
        db = SessionLocal()
        task = db.query(tasks).filter(tasks.id == id).first()

        if task:
            # Actualizar los campos del usuario con los valores proporcionados en updated_user
            task.userId = updated_task.userId
            task.tarea = updated_task.tarea
            task.idState = updated_task.idState

            db.commit()
            db.refresh(task)

            db.close()
            return task
        else:
            db.close()
            return None
    except Exception as e:
        db.rollback()
        raise e



# Función para eliminar un usuario por su ID
def deleteUser(id: uuid.UUID):
    db = SessionLocal()
    task = db.query(tasks).filter(tasks.id == id).first()  # Cambio aquí: users.id en lugar de users.c.id

    if task:
        db.delete(task)
        db.commit()

    db.close()

    return task
