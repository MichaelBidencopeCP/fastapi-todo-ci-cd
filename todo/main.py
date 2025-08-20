from fastapi import FastAPI
from todo.api.v1.todos.simple_todo import router as simple_todo
def create_app():
    app = FastAPI()
    app.include_router(simple_todo, prefix="/api/v1", tags=["todos"])
    return app

app = create_app()