#generate Snippet class defined below

Description: Represents a code snippet shared by a user.

Suggested Fields:

id (string | UUID): Unique identifier for the snippet.
ownerId (string | UUID, required): The ID of the user who created the snippet.
title (string, required): A short title for the snippet.
description (string, optional): Detailed description of what the snippet does.
code (string, required): The actual code content.
language (string, required): Programming language (e.g. "JavaScript", "Python", "Go").
tags (array of strings, optional): Tags for categorization (e.g. ["frontend", "authentication"]).
createdAt (datetime): Timestamp of creation.
updatedAt (datetime): Timestamp of last update.
Indices:

Primary: id
Index: ownerId, tags, language
Relationships:

A Snippet belongs to a User (owner).
A Snippet has many Comments.

#implement serialize method to return json representation of Snippet

database.py 
-----------
Create a python database class for managing SQLite in memory database operations.
Class should have method which are wrapper around cursor methods

---------
user.py users

"Create a Python Database class for managing SQLite in memory database operations.
User table should have these properties: id (string | UUID): Unique identifier for the user.
username (string, required, unique): Chosen username.
name (string, optional): The user’s real name.
bio (string, optional): A short bio describing the user.
skills (array of strings, optional): List of programming skills, e.g. ["JavaScript", "Python"].
githubProfileUrl (string, optional): Link to GitHub profile.
gitlabProfileUrl (string, optional): Link to GitLab profile.
profileImageUrl (string, optional): URL to the user’s profile picture.
createdAt (datetime): Timestamp when the user was created.
updatedAt (datetime): Timestamp when the user was last updated.

Implement these methods:
connect() - connect to the database, ensure check_same_thread is set to False
create() - create a user table using properties from the User model in models.py
get_all_users() - retrieve all users
get_one_user(id) - retrieve a single user by ID
insert_user(user) - insert a new user
update_user(user) - update an existing user
delete_user(id) - delete a user by ID
Ensure to use obj['prop'] syntax to get property
Ensure that every method returns response in user model
Ensure commit transactions where necessary."

-------
snippet.py snippets

Implement Snippet class to manage code snippets. 
Snippet table should have these properties:
•	id (string | UUID): Unique identifier for the snippet.
•	ownerId (string | UUID, required): The ID of the user who created the snippet.
•	title (string, required): A short title for the snippet.
•	description (string, optional): Detailed description of what the snippet does.
•	code (string, required): The actual code content.
•	language (string, required): Programming language (e.g. "JavaScript", "Python", "Go").
•	tags (array of strings, optional): Tags for categorization (e.g. ["frontend", "authentication"]).
•	createdAt (datetime): Timestamp of creation.
•	updatedAt (datetime): Timestamp of last update.

Implement method create_table which will create snippet table

Implement these method for managing snippets:

get_one_snippet(id) - retrive one code snippet
search_snippet(ownerId,tags,language) - Search and filter code snippets by user, tag, language.
insert_snippet(snippet) - inser a new snippet
update_snippet(snippet) - update a snippet
delete_snippet(snippetId) - delete snippet

For implementation use the self.db which is wrapper around sqlite3 connection

----------------------

comment.py comments

Implement Comments class to manage comments for the code snippets
Comment table should have these properties:

•	id (string | UUID): Unique identifier for the comment.
•	snippetId (string | UUID, required): The ID of the snippet the comment is on.
•	authorId (string | UUID, required): The ID of the user who posted the comment.
•	content (string, required): The comment text.
•	createdAt (datetime): Timestamp of creation.
•	updatedAt (datetime): Timestamp of last update.

Implement method create_table which will create comment table

Also implement method for managing comments, here is definition of those:

insert_comment(snippetId,comment) - Add a comment to a code snippet.
get_all_comments(snippedId)  - Retrive comments for a code snippet.

For method implementation use the self.db which is wrapper around sqlite3 connection


----------------------

project.py  projects

Implement Project class to manage projects.
Represents a collaborative project that users can join and share code repositories.
Project table should have these properties:

•	id (string | UUID): Unique identifier for the project.
•	ownerId (string | UUID, required): The ID of the user who created the project.
•	name (string, required): Project name.
•	description (string, optional): Brief description of the project.
•	repoUrl (string, optional): URL to the main code repository (e.g. GitHub link).
•	createdAt (datetime): Timestamp of creation.
•	updatedAt (datetime): Timestamp of last update

ProjectMembership table should have these properties:
•	id (string | UUID): Unique identifier.
•	projectId (string | UUID, required): The ID of the project.
•	userId (string | UUID, required): The ID of the user who is a member.
•	role (string, optional): Role in the project, e.g. ["maintainer", "contributor"].
•	createdAt (datetime)
•	updatedAt (datetime)

Implement method create_table which will create project  and project membership table 
Create_Table method invoke in constructor

Also implement method for managing projects here is definition of those:

For method implementation use the self.db which is wrapper around sqlite3 connection

get_one_project(id) - Retrive project details
insert_one_project(project) - Create a new Project
update_project(project) - update project
add_user_to_project(projectId,userId, role) - add use to the project (use ProjectMembership)

---------------------------------------------------
app.py 

Create a FastAPI application. 
Initialize a fastapi app 
Setup the Database object which will be used for other entities for managing crud operations
Import Database object from the database.database module
Create User,Snippet,Project,Comment objects those require in constructor db object which will use for crud operations.
Import them from database.NAME_OF_OBJECT module, so for 1 class 1 import

---------------------------------------------------

app.py  user endpoints

Implement the following routes for CRUD operations on user:

GET '/users': Retrieve all users from the database 
GET '/user/:userId': Retrieve a single user by its ID 
POST 'users: Create a new user account.
PUT '/users/:userId': Update an existing user in the database 

For crud implementation use user_crud which has these methods:

    get_all_users() - retrieve all users
    get_one_user(id) - retrieve a single user by ID
    insert_user(user) - insert a new user
    update_user(user) - update an existing user
    delete_user(id) - delete a user by ID

When implementing routes, do not use response model or any validation. Just get data from the requst.body
Ensure JSON serialization/deserialization for data exchange between the fastapi routes and the database.

---------------------------------------------------

app.py  snippets endpoint

Implement the following routes for CRUD operations on snippets:

GET '/snippets/:snippetId': Retrieve a snippet by its ID 
GET '/snippets' : search and filter code snippets by user.tag,languages - does variable will endpoint get from query params
POST '/snippets: Create a new snippet.
PUT '/snippets/:snippetId': Update an existing snippet in the database 
DELETE '/snippets/:snippetId' : Delete an existing snippet by ID

For crud implementation use snippet_crud which has these methods:

    get_one_snippet(id) - retrive one code snippet
    search_snippet(ownerId,tags,language) - Search and filter code snippets by user, tag, language.
    insert_snippet(snippet) - inser a new snippet
    update_snippet(snippet) - update a snippet
    delete_snippet(snippetId) - delete snippet

When implementing routes, do not use response model or any validation. Just get data from the requst.body
Ensure JSON serialization/deserialization for data exchange between the fastapi routes and the database.

-----------------------------------------------

app.py comments endpoint


Implement the following routes for CRUD operations on comments:

GET '/comments/:snippetId': Retrieve all comments for snippet.
POST '/comments/:snippetId: Creates new comment for snippet.

For crud implementation use comment_crud which has these methods:

    insert_comment(snippetId,comment) - Add a comment to a code snippet.
    get_all_comments(snippedId)  - Retrive comments for a code snippet.

When implementing routes, do not use response model or any validation. Just get data from the requst.body
Ensure JSON serialization/deserialization for data exchange between the fastapi routes and the database.


----------------------------------------------------

app.py project endpoints

Implement the following routes for CRUD operations on project:

POST '/projects' - Create a new project.
GET '/projects/{projectId}' - Retrieve project details.
PUT '/projects/{projectId}' - Update project information.
POST '/projects/{projectId}/members' - Add a user to a project.

For crud implementation use project_crud which has these methods:

    get_one_project(id) - Retrive project details
    insert_one_project(project) - Create a new Project
    update_project(project) - update project
    add_user_to_project(projectId,userId, role) - add use to the project (use ProjectMembership)

When implementing routes, do not use response model or any validation. Just get data from the requst.body
Ensure JSON serialization/deserialization for data exchange between the fastapi routes and the database.





