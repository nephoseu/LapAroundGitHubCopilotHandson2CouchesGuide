from datetime import datetime
from database.database import Database


class CommentService:
    def __init__(self, db: Database):
        self.db = db
        self.create_table()

    def create_table(self):
        self.db.execute("""
          CREATE TABLE IF NOT EXISTS comments (
          id TEXT PRIMARY KEY,
          snippetId TEXT NOT NULL,
          authorId TEXT NOT NULL,
          content TEXT NOT NULL,
          createdAt TIMESTAMP,
          updatedAt TIMESTAMP,
          FOREIGN KEY(snippetId) REFERENCES snippets(id),
          FOREIGN KEY(authorId) REFERENCES users(id)
          )
        """)

    def insert_comment(self, snippetId,comment):
        createdAt = datetime.now().isoformat()
        updatedAt = createdAt
        self.db.execute("""
          INSERT INTO comments (id, snippetId, authorId, content, createdAt, updatedAt)
          VALUES (%s, %s, %s, %s, %s, %s)
        """, (
          comment["id"],
          snippetId,
          comment["authorId"],
          comment["content"],
          createdAt,
          updatedAt
        ))
        return {
            "id": comment["id"],
            "snippetId": snippetId,
            "authorId": comment["authorId"],
            "content": comment["content"],
            "createdAt": createdAt,
            "updatedAt": updatedAt
        }

    def get_all_comments(self, snippetId):
        self.db.execute("SELECT * FROM comments WHERE snippetId=%s", (snippetId,))
        rows = self.db.fetchall()
        comments = []
        for row in rows:
            comment = {
                "id": row[0],
                "snippetId": row[1],
                "authorId": row[2],
                "content": row[3],
                "createdAt": row[4],
                "updatedAt": row[5]
            }
            comments.append(comment)
        return comments
