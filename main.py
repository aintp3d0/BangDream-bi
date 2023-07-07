import uvicorn
from fastapi import FastAPI

from routers import auth
# from endpoint import (
#     Auth, User,
#     Music
# )


app = FastAPI()


app.include_router(auth)

# app.register_blueprint(User)
#
# app.register_blueprint(Music)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
