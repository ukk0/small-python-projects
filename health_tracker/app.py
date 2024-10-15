import threading
import uvicorn
from interface import UserManagerApp
from database import create_database
import tkinter as tk
from api import app as fastapi_app


def init_db():
    create_database()
    print("Database initialized.")


def start_fastapi():
    # Running server in a separate thread
    print("Starting FastAPI server...")
    uvicorn.run(fastapi_app, host="127.0.0.1", port=8000, log_level="info")


def start_tkinter():
    print("Starting Tkinter GUI...")
    root = tk.Tk()
    app = UserManagerApp(root)
    root.mainloop()


def run_app():
    init_db()
    api_thread = threading.Thread(target=start_fastapi, daemon=True)
    api_thread.start()
    start_tkinter()  # Main thread


if __name__ == "__main__":
    run_app()
