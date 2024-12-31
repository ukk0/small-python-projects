from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class User(BaseModel):
    username: str
    email: str
    age: int
    sex: str
    weight: float
    height: float


class UserUpdate(BaseModel):
    age: int = None
    weight: float = None
    height: float = None


def db_connect():
    return sqlite3.connect("users.db")


@app.post("/user/")
def add_user(user: User):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO users (username, email, age, sex, weight, height)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user.username, user.email, user.age, user.sex, user.weight, user.height))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    finally:
        conn.close()
    return {"message": "User added successfully"}


@app.patch("/user/{identifier}")
def update_user(identifier: str, user_update: UserUpdate):
    conn = db_connect()
    cursor = conn.cursor()
    try:
        cursor.execute(f'''
            UPDATE users SET age=?, weight=?, height=? WHERE username=? OR email=?
        ''', (user_update.age, user_update.weight, user_update.height, identifier, identifier))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        conn.close()
    return {"message": "User updated successfully"}


@app.delete("/user/{identifier}")
def delete_user(identifier: str):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM users WHERE username=? OR email=?
    ''', (identifier, identifier))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="User not found")
    conn.close()
    return {"message": "User deleted successfully"}


@app.get("/user/{identifier}")
def get_user(identifier: str):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, email, age, sex, weight, height FROM users WHERE username=? OR email=?
    ''', (identifier, identifier))
    user = cursor.fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "username": user[0],
        "email": user[1],
        "age": user[2],
        "sex": user[3],
        "weight": user[4],
        "height": user[5]
    }


@app.get("/user/{identifier}/bmi")
def calculate_bmi(identifier: str):
    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT weight, height FROM users WHERE username=? OR email=?
    ''', (identifier, identifier))
    user = cursor.fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    weight, height = user
    if height <= 0:
        raise HTTPException(status_code=400, detail="Invalid height value")
    bmi = weight / (height * height)
    return {"bmi": round(bmi, 2)}
