from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import user, auth, image
from app.models import User, Profile
from .database import engine


app = FastAPI()

# origins = [
#     settings.CLIENT_ORIGIN,
# ]

User.metadata.create_all(engine)
Profile.metadata.create_all(engine)


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/user')
app.include_router(image.router, tags=['Profile'], prefix='/api/image')


@app.get('/api/healthchecker')
def root():
    return {'message': 'Hello World'}

