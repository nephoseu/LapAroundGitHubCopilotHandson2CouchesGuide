import json

class User:
  def __init__(self, id, username, name=None, bio=None, skills=None, githubProfileUrl=None, gitlabProfileUrl=None, profileImageUrl=None, createdAt=None, updatedAt=None):
    self.id = id
    self.username = username
    self.name = name
    self.bio = bio
    self.skills = skills
    self.githubProfileUrl = githubProfileUrl
    self.gitlabProfileUrl = gitlabProfileUrl
    self.profileImageUrl = profileImageUrl
    self.createdAt = createdAt
    self.updatedAt = updatedAt

  def serialize(self):
    return json.dumps({
      "id": self.id,
      "username": self.username,
      "name": self.name,
      "bio": self.bio,
      "skills": self.skills,
      "githubProfileUrl": self.githubProfileUrl,
      "gitlabProfileUrl": self.gitlabProfileUrl,
      "profileImageUrl": self.profileImageUrl,
      "createdAt": self.createdAt,
      "updatedAt": self.updatedAt
    })
  
class Snippet:
  def __init__(self, id, ownerId, title, code, language, description=None, tags=None, createdAt=None, updatedAt=None):
    self.id = id
    self.ownerId = ownerId
    self.title = title
    self.description = description
    self.code = code
    self.language = language
    self.tags = tags
    self.createdAt = createdAt
    self.updatedAt = updatedAt

  def serialize(self):
    return json.dumps({
      "id": self.id,
      "ownerId": self.ownerId,
      "title": self.title,
      "description": self.description,
      "code": self.code,
      "language": self.language,
      "tags": self.tags,
      "createdAt": self.createdAt,
      "updatedAt": self.updatedAt
    })

class Comment:
  def __init__(self, id, snippetId, authorId, content, createdAt=None, updatedAt=None):
    self.id = id
    self.snippetId = snippetId
    self.authorId = authorId
    self.content = content
    self.createdAt = createdAt
    self.updatedAt = updatedAt

  def serialize(self):
    return json.dumps({
      "id": self.id,
      "snippetId": self.snippetId,
      "authorId": self.authorId,
      "content": self.content,
      "createdAt": self.createdAt,
      "updatedAt": self.updatedAt
    })

class Project:
  def __init__(self, id, ownerId, name, description=None, repoUrl=None, createdAt=None, updatedAt=None):
    self.id = id
    self.ownerId = ownerId
    self.name = name
    self.description = description
    self.repoUrl = repoUrl
    self.createdAt = createdAt
    self.updatedAt = updatedAt

  def serialize(self):
    return json.dumps({
      "id": self.id,
      "ownerId": self.ownerId,
      "name": self.name,
      "description": self.description,
      "repoUrl": self.repoUrl,
      "createdAt": self.createdAt,
      "updatedAt": self.updatedAt
    })

class ProjectMembership:
  def __init__(self, id, projectId, userId, role=None, createdAt=None, updatedAt=None):
    self.id = id
    self.projectId = projectId
    self.userId = userId
    self.role = role
    self.createdAt = createdAt
    self.updatedAt = updatedAt

  def serialize(self):
    return json.dumps({
      "id": self.id,
      "projectId": self.projectId,
      "userId": self.userId,
      "role": self.role,
      "createdAt": self.createdAt,
      "updatedAt": self.updatedAt
    })
