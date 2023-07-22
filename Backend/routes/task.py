from fastapi import APIRouter, HTTPException
from db.taskdb import getTasks, create_task, deleteTask, get_taskId, update_task
from schemas.task import createTask, updateTask, responseTask
import uuid

task = APIRouter()


@task.get("/task", response_model=list[responseTask], tags=["task"])
def get_tasks():
    return getTasks()



@task.get("/task/{id}", response_model=responseTask, tags=["task"])
def get_task_by_id(id: uuid.UUID):
    try:
        task = get_taskId(id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")



@task.post("/task", tags=["task"])
def create_new_task(task: createTask):
    try:
        new_task = create_task(task)
        return new_task
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error: Task creation failed")



@task.put("/task/{id}", response_model=responseTask, tags=["task"])
def update_task_by_id(id: uuid.UUID, updated_task: updateTask):
    try:
        task = update_task(id, updated_task)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")
    


@task.delete("/task/{id}", tags=["task"])
def delete_task(id: str):  # Asegúrate de que el parámetro id sea de tipo str
    
    try:
        # Convertir el id de str a uuid.UUID
        task_id = uuid.UUID(id)

        deleted_task = deleteTask(task_id)

        if deleted_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return deleted_task
    
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

