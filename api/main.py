from fastapi import FastAPI
from api.users.router import router as user_router
from api.friends.router import router as friend_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user_router)
app.include_router(friend_router)


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # Cookie from front end
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"]
)
