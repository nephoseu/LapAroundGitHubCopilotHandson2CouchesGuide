from datetime import datetime

from database.database import Database


class UserService:
    def __init__(self,db : Database):
        self.db = db
        self.create_table()

    def create_table(self):
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            name TEXT,
            bio TEXT,
            skills TEXT,
            githubProfileUrl TEXT,
            gitlabProfileUrl TEXT,
            profileImageUrl TEXT,
            createdAt TIMESTAMP,
            updatedAt TIMESTAMP
            )
        """)
    
    def get_all_users(self):
        self.db.execute("SELECT * FROM users")
        rows = self.db.fetchall()
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
                "createdAt": row[8],
                "updatedAt": row[9]
            }
            users.append(user)
        return users

    def get_one_user(self, id):
        self.db.execute("SELECT * FROM users WHERE id=%s", (id,))
        row = self.db.fetchone()
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
                "createdAt": row[8],
                "updatedAt": row[9]
            }
            return user
        else:
            return None

    def insert_user(self, user):
        skills = ",".join(user.get("skills", []))
        createdAt = datetime.now().isoformat()
        updatedAt = createdAt
        self.db.execute("""
            INSERT INTO users (id,username, name, bio, skills, githubProfileUrl, gitlabProfileUrl, profileImageUrl, createdAt, updatedAt)
            VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            user['id'],
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
    
        return self.get_one_user(user["id"])

    def update_user(self, user):
        skills = ",".join(user.get("skills", []))
        updatedAt = datetime.now().isoformat()
        self.db.execute("""
            UPDATE users
            SET username=%s, name=%s, bio=%s, skills=%s, githubProfileUrl=%s, gitlabProfileUrl=%s, profileImageUrl=%s, updatedAt=%s
            WHERE id=%s
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
        return self.get_one_user(user["id"])

    def delete_user(self, id):
        user = self.get_one_user(id)
        if user:
            self.db.execute("DELETE FROM users WHERE id=%s", (id,))
        return user