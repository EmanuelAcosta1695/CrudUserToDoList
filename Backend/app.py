from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import sys
sys.path.append('./')

from routes.user import user
from routes.task import task



app = FastAPI(
    openapi_tags=[{
        "Title": "REST API with FastAPI",
        "description": "CRUD users and tasks",
        "version": "0.0.1",
        "name" : "CRUD",
    }]
)
#uvicorn app:app --reload


# Configuración de los orígenes permitidos (origins)
origins = ["*"]

    # "http://localhost",
    # "http://localhost:3000",
    # "http://example.com",
    # "https://example.com",


# Configuración del middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user)
app.include_router(task)



@app.get('/')
def home():
    return "Hello World!"



if __name__ == '__main__':
    uvicorn.run("app:app")