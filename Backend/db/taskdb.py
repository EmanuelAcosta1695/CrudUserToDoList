from schemas.task import createTask, updateTask
from models.task import tasks
import uuid
from db.db import SessionLocal


def create_task(task: createTask):
    try:
        db = SessionLocal()
        new_task = tasks(usuario_id=task.usuario_id, tarea=task.tarea, id_estado=task.id_estado)
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

    # Aplicar filtro para obtener solo las tareas con id_estado igual a 1 o 2
    #tasks_db = db.query(tasks).filter(tasks.id_estado.in_([1, 2])).all()

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
            task.usuario_id = updated_task.usuario_id
            task.tarea = updated_task.tarea
            task.id_estado = updated_task.id_estado

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
def deleteTask(id: uuid.UUID):
    db = SessionLocal()
    task = db.query(tasks).filter(tasks.id == id).first()  # Cambio aquí: users.id en lugar de users.c.id

    if task:
        db.delete(task)
        db.commit()

    db.close()

    return task
