from typing import Annotated

from fastapi import Depends, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials


auth = APIRouter(prefix='/auth')
security = HTTPBasic()


@auth.post('/register')
def register():
    pass


@auth.post('/login')
def login(
        credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    print('>>', credentials)


@auth.post('/logout')
def logout():
    pass
