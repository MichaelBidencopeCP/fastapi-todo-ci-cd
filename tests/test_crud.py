import pytest
from todo.crud import todo_crud
from todo.api.v1.todos.schemas import TodoItemCreate, TodoItemUpdate, TodoItemResponse

async def test_create_todo(db_session):
    todo_data : TodoItemCreate = TodoItemCreate(title="Test Todo", description="This is a test todo item.")
    db = db_session
    todo_item = await todo_crud.create(db, todo_data)
    assert todo_item.id is not None
    assert todo_item.title == todo_data.title
    assert todo_item.description == todo_data.description
    assert todo_item.completed is False
    
async def test_get_all_todos(db_session):
    db = db_session
    todos = await todo_crud.get_all(db)
    assert isinstance(todos, list)
    for todo in todos:
        assert hasattr(todo, "id")
        assert hasattr(todo, "title")
        assert hasattr(todo, "description")
        assert hasattr(todo, "completed")

async def test_update_todo(db_session):
    db = db_session
    todo_data = TodoItemCreate(title="Initial Title", description="Initial Description")
    todo_item = await todo_crud.create(db, todo_data)

    update_data = TodoItemUpdate(title="Updated Title", completed=True)
    updated_todo = await todo_crud.update(db, todo_item.id, update_data)

    assert updated_todo.id == todo_item.id
    assert updated_todo.title == update_data.title
    assert updated_todo.description == todo_data.description
    assert updated_todo.completed is True
    
async def test_delete_todo(db_session):
    db = db_session
    todo_data = TodoItemCreate(title="To be deleted", description="This todo will be deleted.")
    todo_item = await todo_crud.create(db, todo_data)
    deleted_todo = await todo_crud.delete(db, todo_item.id)
    assert deleted_todo.id == todo_item.id
    assert await todo_crud.get(db, todo_item.id) is None

async def test_get_todo_not_found(db_session):
    db = db_session
    todo = await todo_crud.get(db, 9999)
    assert todo is None
    
async def test_update_todo_not_found(db_session):
    db = db_session
    update_data = TodoItemCreate(title="Non-existent", description="This todo does not exist.")
    updated_todo = await todo_crud.update(db, 9999, update_data)
    assert updated_todo is None


