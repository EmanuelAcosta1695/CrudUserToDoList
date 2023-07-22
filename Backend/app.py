from fastapi import FastAPI
import uvicorn

import sys
sys.path.append('./')

from routes.user import user


app = FastAPI()
#uvicorn app:app --reload


app.include_router(user)


@app.get('/')
def home():
    return "Hello World!"



if __name__ == '__main__':
    uvicorn.run("app:app")