import pytest
from todo.crud.todo_items import create, get_all


async def test_create_todo(db_session):
    todo_data = {"title": "Test Todo", "description": "This is a test todo item."}
    db = db_session
    todo_item = await create(db, **todo_data)
    assert todo_item.id is not None
    assert todo_item.title == todo_data["title"]
    assert todo_item.description == todo_data["description"]
    assert todo_item.completed is False
    
async def test_get_all_todos(db_session):
    db = db_session
    todos = await get_all(db)
    assert isinstance(todos, list)
    for todo in todos:
        assert hasattr(todo, "id")
        assert hasattr(todo, "title")
        assert hasattr(todo, "description")
        assert hasattr(todo, "completed")

