from fastapi import APIRouter

todolist_router = APIRouter(prefix="/api", tags=["Todo"])

@todolist_router.get("/")
def all_todos():
    return "Not implemented yet"

@todolist_router.post("/")
def post_todo():
    return "Not implemented yet"

@todolist_router.put("/{key}")
def update_todo(key: int):
    return "Not implemented yet"

@todolist_router.delete("/{key}")
def delete_todo(key: int):
    return "Not implemented yet"