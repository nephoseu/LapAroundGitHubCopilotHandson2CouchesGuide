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

---------
db.py

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

