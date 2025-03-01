import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk  # For images
from datetime import datetime  # For date/time functionality

# Function to validate numeric input
def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Function to calculate BMI
def calculate_bmi():
    weight = entry_weight.get()
    feet = entry_feet.get()
    inches = entry_inches.get()
    
    if not (weight and feet and inches):
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    
    if not (is_valid_number(weight) and feet.isdigit() and inches.isdigit()):
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return
    
    weight_kg = float(weight) * 0.453592
    height_m = (int(feet) * 12 + int(inches)) * 0.0254
    bmi = weight_kg / (height_m ** 2)
    label_result.config(text=f"BMI: {bmi:.2f}")
    
    if bmi < 18.5:
        label_category.config(text="Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        label_category.config(text="Category: Normal weight")
    elif 25 <= bmi < 29.9:
        label_category.config(text="Category: Overweight")
    else:
        label_category.config(text="Category: Obese")

# Function to log exercise
def log_exercise():
    exercise = entry_exercise.get()
    duration = entry_duration.get()
    
    if not (exercise and duration):
        messagebox.showerror("Input Error", "Please enter both exercise and duration.")
        return
    
    if not is_valid_number(duration):
        messagebox.showerror("Input Error", "Duration must be a numeric value.")
        return
    
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text_log.insert(tk.END, f"{current_date} | Exercise: {exercise} | Duration: {duration} minutes\n")
    entry_exercise.delete(0, tk.END)
    entry_duration.delete(0, tk.END)

# Function to clear fields
def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_feet.delete(0, tk.END)
    entry_inches.delete(0, tk.END)
    label_result.config(text="BMI: --")
    label_category.config(text="Category: --")
    entry_exercise.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    text_log.delete(1.0, tk.END)

# Function to open fitness tips window
def open_fitness_tips():
    top = Toplevel(root)
    top.title("Fitness Tips")
    top.geometry("400x400")
    
    label_tips = tk.Label(top, text="Fitness Tips", font=("Arial", 18))
    label_tips.pack(pady=10)
    
    tips_text = "1. Stay hydrated.\n2. Exercise regularly.\n3. Eat a balanced diet."
    label_tip_content = tk.Label(top, text=tips_text, justify="left")
    label_tip_content.pack(pady=10)
    
    button_close = tk.Button(top, text="Close", command=top.destroy)
    button_close.pack(pady=10)

# Main Window
root = tk.Tk()
root.title("Fitness Application")
root.geometry("500x700")

label_title = tk.Label(root, text="Fitness Application", font=("Arial", 18))
label_title.pack(pady=10)

# Load and display images
try:
    img1 = Image.open("image1.jpg").resize((100, 100))
    photo1 = ImageTk.PhotoImage(img1)
    label_img1 = tk.Label(root, image=photo1, text="Fitness Image 1", compound="top")
    label_img1.pack()
except Exception as e:
    label_img1 = tk.Label(root, text="Image 1 not found", compound="top")
    label_img1.pack()

try:
    img2 = Image.open("image2.jpg").resize((100, 100))
    photo2 = ImageTk.PhotoImage(img2)
    label_img2 = tk.Label(root, image=photo2, text="Fitness Image 2", compound="top")
    label_img2.pack()
except Exception as e:
    label_img2 = tk.Label(root, text="Image 2 not found", compound="top")
    label_img2.pack()

# BMI Calculation Section
frame_bmi = tk.Frame(root)
frame_bmi.pack(pady=10)

label_weight = tk.Label(frame_bmi, text="Weight (lbs):")
label_weight.grid(row=0, column=0, padx=5, pady=5)
entry_weight = tk.Entry(frame_bmi)
entry_weight.grid(row=0, column=1, padx=5, pady=5)

label_feet = tk.Label(frame_bmi, text="Height (ft):")
label_feet.grid(row=1, column=0, padx=5, pady=5)
entry_feet = tk.Entry(frame_bmi, width=5)
entry_feet.grid(row=1, column=1, padx=5, pady=5)

label_inches = tk.Label(frame_bmi, text="Inches:")
label_inches.grid(row=1, column=2, padx=5, pady=5)
entry_inches = tk.Entry(frame_bmi, width=5)
entry_inches.grid(row=1, column=3, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="BMI: --", font=("Arial", 14))
label_result.pack(pady=5)
label_category = tk.Label(root, text="Category: --", font=("Arial", 12))
label_category.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=root.quit)
button_exit.pack(pady=10)

root.mainloop()
