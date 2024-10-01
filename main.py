from fastapi import FastAPI, Security, Depends, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import PlainTextResponse
from models.user import UserModel
import uvicorn
from utils.token import create_access_token, check_permission, Permission
from typing import Annotated

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.post("/token")
async def login():
    access_token = create_access_token(data={'scopes': ['read-only']})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/")
async def process_items(user_model: UserModel,
                        permission: dict = Security(check_permission, scopes=["read-only"])):
    return user_model.dict()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
