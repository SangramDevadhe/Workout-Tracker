import tkinter as tk
from tkinter import ttk, messagebox

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        for workout in self.workouts:
            print(workout)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout_page(user, root):
    def add_workout():
        date = date_entry.get()
        exercise_type = exercise_type_entry.get()
        duration = int(duration_entry.get())
        calories_burned = int(calories_burned_entry.get())
        workout = Workout(date, exercise_type, duration, calories_burned)
        user.add_workout(workout)
        messagebox.showinfo("Success", "Workout added successfully!")
        show_services()

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Add Workout", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
    tk.Label(root, text="Date (YYYY-MM-DD):", bg="lightblue").pack()
    date_entry = tk.Entry(root)
    date_entry.pack()
    tk.Label(root, text="Exercise Type:", bg="lightblue").pack()
    exercise_type_entry = tk.Entry(root)
    exercise_type_entry.pack()
    tk.Label(root, text="Duration (minutes):", bg="lightblue").pack()
    duration_entry = tk.Entry(root)
    duration_entry.pack()
    tk.Label(root, text="Calories Burned:", bg="lightblue").pack()
    calories_burned_entry = tk.Entry(root)
    calories_burned_entry.pack()
    tk.Button(root, text="Add", command=add_workout).pack(pady=10)
    tk.Button(root, text="Back", command=show_services).pack(pady=10)

def view_workouts_page(user, root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="View Workouts", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
    tree = ttk.Treeview(root, columns=("Date", "Exercise Type", "Duration", "Calories Burned"), show='headings')
    tree.heading("Date", text="Date")
    tree.heading("Exercise Type", text="Exercise Type")
    tree.heading("Duration", text="Duration (minutes)")
    tree.heading("Calories Burned", text="Calories Burned")
    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    for workout in user.workouts:
        tree.insert("", tk.END, values=(workout.date, workout.exercise_type, workout.duration, workout.calories_burned))

    tk.Button(root, text="Back", command=show_services).pack(pady=10)

def save_data_page(user, root):
    def save_data():
        filename = filename_entry.get()
        user.save_data(filename)
        messagebox.showinfo("Success", "Data saved successfully!")
        show_services()

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Save Data", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
    tk.Label(root, text="Filename:", bg="lightblue").pack()
    filename_entry = tk.Entry(root)
    filename_entry.pack()
    tk.Button(root, text="Save", command=save_data).pack(pady=10)
    tk.Button(root, text="Back", command=show_services).pack(pady=10)

def load_data_page(user, root):
    def load_data():
        filename = filename_entry.get()
        user.load_data(filename)
        messagebox.showinfo("Success", "Data loaded successfully!")
        show_services()

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Load Data", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
    tk.Label(root, text="Filename:", bg="lightblue").pack()
    filename_entry = tk.Entry(root)
    filename_entry.pack()
    tk.Button(root, text="Load", command=load_data).pack(pady=10)
    tk.Button(root, text="Back", command=show_services).pack(pady=10)

def show_services():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Our Services", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
    tk.Button(root, text="Add Workout", command=lambda: add_workout_page(user, root)).pack(pady=5)
    tk.Button(root, text="View Workouts", command=lambda: view_workouts_page(user, root)).pack(pady=5)
    tk.Button(root, text="Save Data", command=lambda: save_data_page(user, root)).pack(pady=5)
    tk.Button(root, text="Load Data", command=lambda: load_data_page(user, root)).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

def start_program():
    name = name_entry.get()
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    global user
    user = User(name, age, weight)
    show_services()

root = tk.Tk()
root.title("Workout Tracker")
root.geometry("600x400")
root.configure(bg="lightblue")

tk.Label(root, text="Welcome to Workout Tracker", font=("Helvetica", 16), bg="lightblue").pack(pady=10)
tk.Label(root, text="Enter your details below:", bg="lightblue").pack(pady=5)

tk.Label(root, text="Name:", bg="lightblue").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:", bg="lightblue").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Weight:", bg="lightblue").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Button(root, text="Start", command=start_program).pack(pady=10)

root.mainloop()