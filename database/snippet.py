
from datetime import datetime
from database.database import Database


class SnippetService:
    def __init__(self,db : Database):
        self.db = db
        self.create_table()

    def create_table(self):
        self.db.execute("""
        CREATE TABLE IF NOT EXISTS snippets (
        id TEXT PRIMARY KEY,
        ownerId TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        code TEXT NOT NULL,
        language TEXT NOT NULL,
        tags TEXT,
        createdAt TIMESTAMP,
        updatedAt TIMESTAMP,
        FOREIGN KEY(ownerId) REFERENCES users(id)
        )
        """)

    
    def get_one_snippet(self, id):
        self.db.execute("SELECT * FROM snippets WHERE id=%s", (id,))
        row = self.db.fetchone()
        if row:
            snippet = {
                "id": row[0],
                "ownerId": row[1],
                "title": row[2],
                "description": row[3],
                "code": row[4],
                "language": row[5],
                "tags": row[6].split(",") if row[6] else [],
                "createdAt": row[7],
                "updatedAt": row[8]
            }
            return snippet
        else:
            return None

   
    def search_snippet(self, ownerId=None, tags=None, language=None):
        query = "SELECT * FROM snippets WHERE 1=1"
        params = []
        if ownerId:
            query += " AND ownerId=%s"
            params.append(ownerId)
        if tags:
            query += " AND (" + " OR ".join(["tags LIKE %s"] * len(tags)) + ")"
            params.extend([f"%{tag}%" for tag in tags])
        if language:
            query += " AND language=%s"
            params.append(language)
        print(query, params)
        self.db.execute(query, params)
        rows = self.db.fetchall()
        snippets = []
        for row in rows:
            snippet = {
                "id": row[0],
                "ownerId": row[1],
                "title": row[2],
                "description": row[3],
                "code": row[4],
                "language": row[5],
                "tags": row[6].split(",") if row[6] else [],
                "createdAt": row[7],
                "updatedAt": row[8]
            }
            snippets.append(snippet)
        return snippets

    def insert_snippet(self, snippet):
        tags = ",".join(snippet.get("tags", []))
        createdAt = datetime.now().isoformat()
        updatedAt = createdAt
        self.db.execute("""
            INSERT INTO snippets (id, ownerId, title, description, code, language, tags, createdAt, updatedAt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            snippet["id"],
            snippet["ownerId"],
            snippet["title"],
            snippet.get("description"),
            snippet["code"],
            snippet["language"],
            tags,
            createdAt,
            updatedAt
        ))
        return self.get_one_snippet(snippet["id"])

    def update_snippet(self, snippet):
        tags = ",".join(snippet.get("tags", []))
        updatedAt = datetime.now().isoformat()
        self.db.execute("""
            UPDATE snippets
            SET ownerId=%s, title=%s, description=%s, code=%s, language=%s, tags=%s, updatedAt=%s
            WHERE id=%s
        """, (
            snippet["ownerId"],
            snippet["title"],
            snippet.get("description"),
            snippet["code"],
            snippet["language"],
            tags,
            updatedAt,
            snippet["id"]
        ))
        return self.get_one_snippet(snippet["id"])

    def delete_snippet(self, id):
        snippet = self.get_one_snippet(id)
        if snippet:
            self.db.execute("DELETE FROM snippets WHERE id=%s", (id,))
        return snippet

    