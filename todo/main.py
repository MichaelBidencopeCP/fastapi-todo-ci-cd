from fastapi import FastAPI
from todo.api.v1.todos.simple_todo import router as simple_todo
from todo.api.healthcheck import router as healthcheck
def create_app():
    app = FastAPI()
    app.include_router(simple_todo, prefix="/api/v1", tags=["todos"])
    app.include_router(healthcheck, prefix="/api", tags=["healthcheck"])
    return app

app = create_app()