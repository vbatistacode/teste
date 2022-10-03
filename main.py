import time
from fastapi import FastAPI, Request

from api import users, courses, sections
from db.db_setup import engine
from db.models import user, course

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mesh Bank API",
    description="Mesh Bank app backend",
    version="0.0.1",
    contact={
        "name": "Mesh Works",
        "email": "vbatista@meshworks.com.br",
    },
    license_info={
        "name": "MIT",
    },
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)