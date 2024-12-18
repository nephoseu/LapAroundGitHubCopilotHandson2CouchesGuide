from fastapi import FastAPI
from database.database import Database
from database.user import UserService
from database.snippet import SnippetService
from database.project import ProjectService
from database.comment import CommentService
from fastapi import HTTPException, Request
from fastapi import Body

app = FastAPI()

connection_string = "YOUR_CONNECTION_STRING"
# Initialize the Database object
db = Database(connection_string)

# Initialize the CRUD objects
user_crud = UserService(db)
snippet_crud = SnippetService(db)
project_crud = ProjectService(db)
comment_crud = CommentService(db)


@app.get("/users")
async def get_all_users():
    return user_crud.get_all_users()

@app.get("/user/{user_id}")
async def get_one_user(user_id: str):
    user = user_crud.get_one_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
async def create_user(user: dict = Body(...)):
    return user_crud.insert_user(user)

@app.put("/users/{user_id}")
async def update_user(user_id: str, user: dict = Body(...)):
    existing_user = user_crud.get_one_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user['id'] = user_id
    return user_crud.update_user(user)


@app.get("/snippets/{snippet_id}")
async def get_one_snippet(snippet_id: str):
    snippet = snippet_crud.get_one_snippet(snippet_id)
    if snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet

@app.get("/snippets")
async def search_snippets(owner_id: str = None, tags: str = None, language: str = None):
    if tags:
        tags = tags.split(',')
    return snippet_crud.search_snippet(owner_id, tags, language)

@app.post("/snippets")
async def create_snippet(snippet: dict = Body(...)):
    return snippet_crud.insert_snippet(snippet)

@app.put("/snippets/{snippet_id}")
async def update_snippet(snippet_id: str, snippet: dict = Body(...)):
    existing_snippet = snippet_crud.get_one_snippet(snippet_id)
    if existing_snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    snippet['id'] = snippet_id
    return snippet_crud.update_snippet(snippet)

@app.delete("/snippets/{snippet_id}")
async def delete_snippet(snippet_id: str):
    existing_snippet = snippet_crud.get_one_snippet(snippet_id)
    if existing_snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet_crud.delete_snippet(snippet_id)


@app.get("/comments/{snippet_id}")
async def get_all_comments(snippet_id: str):
    return comment_crud.get_all_comments(snippet_id)

@app.post("/comments/{snippet_id}")
async def create_comment(snippet_id: str, comment: dict = Body(...)):
    return comment_crud.insert_comment(snippet_id,comment)


@app.post("/projects")
async def create_project(project: dict = Body(...)):
    return project_crud.insert_one_project(project)

@app.get("/projects/{projectId}")
async def get_one_project(projectId: str):
    project = project_crud.get_one_project(projectId)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.put("/projects/{projectId}")
async def update_project(projectId: str, project: dict = Body(...)):
    existing_project = project_crud.get_one_project(projectId)
    if existing_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    project['id'] = projectId
    return project_crud.update_project(project)

@app.post("/projects/{projectId}/members")
async def add_user_to_project(projectId: str, user: dict = Body(...)):
    user_id = user.get("user_id")
    role = user.get("role")
    if user_id is None or role is None:
        raise HTTPException(status_code=400, detail="user_id and role are required")
    return project_crud.add_user_to_project(projectId, user_id, role)