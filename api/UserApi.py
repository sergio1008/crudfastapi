from fastapi import APIRouter, Depends
from service.UserService import UserService
from dto.UserDTO import UserDTO


service = UserService()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}, 200 : {"description": "success"}},
)

@router.get("/", tags=["get users"])
def getAll():
    return service.getAll()

@router.post("/", tags=["create users"])
def create(user: UserDTO):
    service.create(user)
    return  {"message" : "User created"}, 200
     
    