from app import db

with db.engine.connect() as connection:
    connection.execute("ALTER TABLE friend RENAME COLUMN decription TO description;")