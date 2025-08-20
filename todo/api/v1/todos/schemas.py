from pydantic import BaseModel, Field

class TodoItem(BaseModel):
    id: int = Field(..., description="The unique identifier for the todo item")
    task: str = Field(..., description="The task description of the todo item")
    completed: bool = Field(default=False, description="Indicates if the todo item is completed")
    created_at: str = Field(..., description="The timestamp when the todo item was created")
    updated_at: str = Field(..., description="The timestamp when the todo item was last updated")