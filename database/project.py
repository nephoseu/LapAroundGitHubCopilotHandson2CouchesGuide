from datetime import datetime
import uuid

from database.database import Database

class ProjectService:
    def __init__(self, db: Database):
        self.db = db
        self.create_table()

    def create_table(self):
        with self.db:
            self.db.execute('''
                CREATE TABLE IF NOT EXISTS Project (
                    id TEXT PRIMARY KEY,
                    ownerId TEXT NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    repoUrl TEXT,
                    createdAt TEXT NOT NULL,
                    updatedAt TEXT NOT NULL
                )
            ''')
            self.db.execute('''
                CREATE TABLE IF NOT EXISTS ProjectMembership (
                    id TEXT PRIMARY KEY,
                    projectId TEXT NOT NULL,
                    userId TEXT NOT NULL,
                    role TEXT,
                    createdAt TIMESTAMP,
                    updatedAt TIMESTAMP,
                    FOREIGN KEY(projectId) REFERENCES Project(id)
                )
            ''')

    def get_one_project(self, id):
        self.db.execute('SELECT * FROM Project WHERE id = %s', (id,))
        return self.db.fetchone()

    def insert_one_project(self, project):
        with self.db:
            self.db.execute('''
                INSERT INTO Project (id, ownerId, name, description, repoUrl, createdAt, updatedAt)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (
                project['id'], 
                project['ownerId'], 
                project['name'], 
                project.get('description'), 
                project.get('repoUrl'), 
                datetime.now().isoformat(), 
                datetime.now().isoformat()
            ))

    def update_project(self, project):
        with self.db:
            self.db.execute('''
                UPDATE Project
                SET ownerId = %s, name = %s, description = %s, repoUrl = %s, updatedAt = %s
                WHERE id = %s
            ''', (
                project['ownerId'], 
                project['name'], 
                project.get('description'), 
                project.get('repoUrl'), 
                datetime.now().isoformat(), 
                project['id']
            ))

    def add_user_to_project(self, projectId, userId, role):
        with self.db:
            self.db.execute('''
                INSERT INTO ProjectMembership (id, projectId, userId, role, createdAt, updatedAt)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (
                str(uuid.uuid4()),
                projectId, 
                userId, 
                role, 
                datetime.now().isoformat(), 
                datetime.now().isoformat()
            ))