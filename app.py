import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from datetime import datetime,timezone

CREATE_BLOG_TABLE = (
    "CREATE TABLE IF NOT EXISTS blog(id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_CONTENT_TABLE ="""
CREATE TABLE IF NOT EXISTS contents(blod_id INTEGER, content text, date TIMESTAMP, FOREIGN KEY(blog_id)
 REFERENCES blogs(id) ON DELETE CASCADE);"""

INSERT_BLOG_RETURN_ID = "INSERT INTO blogs(name) VALUES (%s) RETURNING id;"
INSERT_BLOG = ("INSERT INTO contents(blog_id, content, date) VALUES (%s %s %s);")

GLOBAL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISINCT DATE(date)) AS days FROM contents;"""
)



load_dotenv()

app = Flask(__name__)
url = os.getenv ("DATABASE_URL")
connection = psycopg2.connect(url)

@app.post("/api/blog")
def create_room():
    data = request.get_json
    name = data['name']
    with connection:
        with connection.cursor() as crusor:
            crusor.execute(CREATE_BLOG_TABLE)
            crusor.execute(INSERT_BLOG_RETURN_ID,(name,))
            blog_id = crusor.fetchone()[0]
    
    return {"id":blog_id,"message":f"Blog{name} created."},201

@app.post("/api/content")
def add_content():
    data = requst.get_json()
    content = data["content"]
    blog_id = data["blog"]
    try:
        date = datetime.striptime(data["date"], "%m-%d-%Y %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_CONTENT_TABLE)
            cursor.execute(INSERT_BLOG, (blog_id,content,date))
    
    return {"message": "Content addded."},201