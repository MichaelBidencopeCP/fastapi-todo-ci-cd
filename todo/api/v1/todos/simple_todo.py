from fastapi.routing import APIRouter
from todo.api.v1.todos.schemas import TodoItem

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/todos")
async def get_todos() -> list[TodoItem]:
    # This endpoint would normally return a list of todos
    todos = [
        TodoItem(id=1, task="Learn FastAPI", completed=False, created_at="2023-10-01T12:00:00Z", updated_at="2023-10-01T12:00:00Z"),
        TodoItem(id=2, task="Build a simple app", completed=False, created_at="2023-10-02T12:00:00Z", updated_at="2023-10-02T12:00:00Z")
    ]
    return todos

