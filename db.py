import sqlite3
from datetime import datetime

class Database:
  def __init__(self):
    self.conn = None
    self.cursor = None

  def connect(self):
    self.conn = sqlite3.connect(":memory:", check_same_thread=False)
    self.cursor = self.conn.cursor()

  def create(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        name TEXT,
        bio TEXT,
        skills TEXT,
        githubProfileUrl TEXT,
        gitlabProfileUrl TEXT,
        profileImageUrl TEXT,
        createdAt TEXT,
        updatedAt TEXT
      )
    """)

  def get_all_users(self):
    self.cursor.execute("SELECT * FROM users")
    rows = self.cursor.fetchall()
    users = []
    for row in rows:
      user = {
        "id": row[0],
        "username": row[1],
        "name": row[2],
        "bio": row[3],
        "skills": row[4].split(",") if row[4] else [],
        "githubProfileUrl": row[5],
        "gitlabProfileUrl": row[6],
        "profileImageUrl": row[7],
        "createdAt": datetime.fromisoformat(row[8]),
        "updatedAt": datetime.fromisoformat(row[9])
      }
      users.append(user)
    return users

  def get_one_user(self, id):
    self.cursor.execute("SELECT * FROM users WHERE id=?", (id,))
    row = self.cursor.fetchone()
    if row:
      user = {
        "id": row[0],
        "username": row[1],
        "name": row[2],
        "bio": row[3],
        "skills": row[4].split(",") if row[4] else [],
        "githubProfileUrl": row[5],
        "gitlabProfileUrl": row[6],
        "profileImageUrl": row[7],
        "createdAt": datetime.fromisoformat(row[8]),
        "updatedAt": datetime.fromisoformat(row[9])
      }
      return user
    else:
      return None

  def insert_user(self, user):
    skills = ",".join(user.get("skills", []))
    createdAt = datetime.now().isoformat()
    updatedAt = createdAt
    self.cursor.execute("""
      INSERT INTO users (id, username, name, bio, skills, githubProfileUrl, gitlabProfileUrl, profileImageUrl, createdAt, updatedAt)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
      user["id"],
      user["username"],
      user.get("name"),
      user.get("bio"),
      skills,
      user.get("githubProfileUrl"),
      user.get("gitlabProfileUrl"),
      user.get("profileImageUrl"),
      createdAt,
      updatedAt
    ))
    self.conn.commit()
    return self.get_one_user(user["id"])

  def update_user(self, user):
    skills = ",".join(user.get("skills", []))
    updatedAt = datetime.now().isoformat()
    self.cursor.execute("""
      UPDATE users
      SET username=?, name=?, bio=?, skills=?, githubProfileUrl=?, gitlabProfileUrl=?, profileImageUrl=?, updatedAt=?
      WHERE id=?
    """, (
      user["username"],
      user.get("name"),
      user.get("bio"),
      skills,
      user.get("githubProfileUrl"),
      user.get("gitlabProfileUrl"),
      user.get("profileImageUrl"),
      updatedAt,
      user["id"]
    ))
    self.conn.commit()
    return self.get_one_user(user["id"])

  def delete_user(self, id):
    user = self.get_one_user(id)
    if user:
      self.cursor.execute("DELETE FROM users WHERE id=?", (id,))
      self.conn.commit()
    return user
  
  