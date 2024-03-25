from typing import List
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dependency_injector.wiring import Provide, inject
import qrcode
from imgix import UrlBuilder

from src.dto.user import BaseUser, CreateUser, User
from src.container import Container
from src.services.user import UserService
from src.db.db import Database

app = FastAPI()


@app.get("/")
def home(user_service: UserService = Depends(UserService)) -> list[User]:
    users = user_service.get_all_users()
    return users
    # return [
    #     {"id": 1, "name": "John Doe", "type": "doctor", "scud_id": 12},
    #     {"id": 2, "name": "John Doe", "type": "doctor", "scud_id": 10},
    #     {"id": 3, "name": "John Doe", "type": "doctor", "scud_id": 12},
    #     {"id": 4, "name": "John Doe", "type": "doctor", "scud_id": 12},
    #     {"id": 5, "name": "John Doe", "type": "doctor", "scud_id": 12},
    #     {"id": 6, "name": "Wane Doe", "type": "patient", "scud_id": 12},
    #     {"id": 7, "name": "John Smith", "type": "doctor", "scud_id": 14},
    # ]


@app.get("/user/{user_id}")
@inject
def get_user(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    user = user_service.get_user(user_id)
    img = qrcode.make(user.__dict__)
    img.save("qr_code.png")
    return user
    # return {"id": 1, "name": "John Doe", "type": "doctor", "scud_id": 12}


@app.post("/create_user", response_model=User)
@inject
def create_user(
    request: Request,
    user: CreateUser,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user(user)
    # return {"id": 1, "name": "John Doe", "type": "doctor", "scud_id": 12}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    # container = Container()
    # container.wire(
    #     modules=[
    #         __name__,
    #         "src.services.user",
    #     ]
    # )
    Database().init_db()
    # db.init_db()
    uvicorn.run(app, host="localhost", port=8000)
