from dotenv import load_dotenv

# loading dotenv
load_dotenv()

from fastapi import FastAPI
import uvicorn
from src.routes import router

from src.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
