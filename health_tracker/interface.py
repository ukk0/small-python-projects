import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox

BASE_URL = "http://127.0.0.1:8000"


class UserManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Tracker")

        self.create_input_widgets()
        self.create_action_buttons()

    def create_input_widgets(self):
        tk.Label(self.root, text="Username:").grid(row=0, column=0)
        self.entry_username = tk.Entry(self.root)
        self.entry_username.grid(row=0, column=1)

        tk.Label(self.root, text="Email:").grid(row=1, column=0)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=1, column=1)

        tk.Label(self.root, text="Age:").grid(row=2, column=0)
        self.entry_age = tk.Entry(self.root)
        self.entry_age.grid(row=2, column=1)

        tk.Label(self.root, text="Sex:").grid(row=3, column=0)
        self.combo_sex = ttk.Combobox(self.root, values=["Male", "Female"])
        self.combo_sex.grid(row=3, column=1)
        self.combo_sex.current(0)

        tk.Label(self.root, text="Weight (kg):").grid(row=4, column=0)
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.grid(row=4, column=1)

        tk.Label(self.root, text="Height (m):").grid(row=5, column=0)
        self.entry_height = tk.Entry(self.root)
        self.entry_height.grid(row=5, column=1)

    def create_action_buttons(self):
        tk.Button(self.root, text="Add User", command=self.add_user).grid(row=6, column=0)
        tk.Button(self.root, text="Update User", command=self.update_user).grid(row=6, column=1)
        tk.Button(self.root, text="Delete User", command=self.delete_user).grid(row=7, column=0)
        tk.Button(self.root, text="Show User Info", command=self.show_user_info).grid(row=7, column=1)
        tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi).grid(row=8, column=0, columnspan=2)

    def add_user(self):
        user_info = self.get_user_info_from_entries()
        response = requests.post(f"{BASE_URL}/user/", json=user_info)
        self.handle_response(response, "User added successfully")

    def update_user(self):
        user_info = self.get_user_info_from_entries()
        identifier = self.get_identifier()
        response = requests.patch(f"{BASE_URL}/user/{identifier}", json=user_info)
        self.handle_response(response, "User updated successfully")

    def delete_user(self):
        identifier = self.get_identifier()
        response = requests.delete(f"{BASE_URL}/user/{identifier}")
        self.handle_response(response, "User deleted successfully")

    def show_user_info(self):
        identifier = self.get_identifier()
        response = requests.get(f"{BASE_URL}/user/{identifier}")
        if response.status_code == 200:
            user = response.json()
            messagebox.showinfo("User Info", f"Username: {user['username']}\nEmail: {user['email']}\nAge: {user['age']}\nSex: {user['sex']}\nWeight: {user['weight']}\nHeight: {user['height']}")
        else:
            messagebox.showerror("Error", response.json()["detail"])

    def calculate_bmi(self):
        identifier = self.get_identifier()
        response = requests.get(f"{BASE_URL}/user/{identifier}/bmi")
        if response.status_code == 200:
            bmi = response.json()["bmi"]
            messagebox.showinfo("BMI", f"BMI: {bmi}")
        else:
            messagebox.showerror("Error", response.json()["detail"])

    def get_user_info_from_entries(self):
        return {
            "username": self.entry_username.get(),
            "email": self.entry_email.get(),
            "age": int(self.entry_age.get()),
            "sex": self.combo_sex.get(),
            "weight": float(self.entry_weight.get()),
            "height": float(self.entry_height.get())
        }

    def get_identifier(self):
        return self.entry_username.get() or self.entry_email.get()

    @staticmethod
    def handle_response(response, success_message):
        if response.status_code == 200:
            messagebox.showinfo("Success", success_message)
        else:
            messagebox.showerror("Error", response.json()["detail"])
