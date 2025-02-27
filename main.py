import tkinter as tk
from tkinter import messagebox
from datetime import datetime  # For date/time functionality

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get input values
        weight_lbs = float(entry_weight.get())
        feet = int(entry_feet.get())
        inches = int(entry_inches.get())
        
        # Validate inputs
        if weight_lbs <= 0 or feet < 0 or inches < 0:
            messagebox.showerror("Input Error", "Please enter valid weight, height in feet, and inches.")
            return
        
        # Convert weight from lbs to kg
        weight_kg = weight_lbs * 0.453592
        
        # Convert height from feet and inches to meters
        height_m = (feet * 12 + inches) * 0.0254
        
        # Calculate BMI
        bmi = weight_kg / (height_m * height_m)
        
        label_result.config(text=f"BMI: {bmi:.2f}")
        
        # Show BMI category
        if bmi < 18.5:
            label_category.config(text="Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            label_category.config(text="Category: Normal weight")
        elif 25 <= bmi < 29.9:
            label_category.config(text="Category: Overweight")
        else:
            label_category.config(text="Category: Obese")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        # Function to log exercise data
def log_exercise():
    exercise = entry_exercise.get()
    duration = entry_duration.get()
    
    if not exercise or not duration:
        messagebox.showerror("Input Error", "Please enter both exercise and duration.")
        return
    
    # Get current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Display logged exercise data with date and time
    text_log.insert(tk.END, f"{current_date} | Exercise: {exercise} | Duration: {duration} minutes\n")
    entry_exercise.delete(0, tk.END)
    entry_duration.delete(0, tk.END)

# Function to clear all fields
def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_feet.delete(0, tk.END)
    entry_inches.delete(0, tk.END)
    label_result.config(text="BMI: --")
    label_category.config(text="Category: --")
    entry_exercise.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    text_log.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Fitness Application")
root.geometry("400x600")

# Create and place widgets
label_title = tk.Label(root, text="Fitness Application", font=("Arial", 18))
label_title.pack(pady=10)

# Input fields for weight and height
frame_bmi = tk.Frame(root)
frame_bmi.pack(pady=10)

label_weight = tk.Label(frame_bmi, text="Enter Weight (lbs):")
label_weight.grid(row=0, column=0, padx=10, pady=5)

entry_weight = tk.Entry(frame_bmi)
entry_weight.grid(row=0, column=1, padx=10, pady=5)

label_height = tk.Label(frame_bmi, text="Enter Height (ft and inches):")
label_height.grid(row=1, column=0, padx=10, pady=5)

label_feet = tk.Label(frame_bmi, text="Feet:")
label_feet.grid(row=1, column=1, padx=10, pady=5)

entry_feet = tk.Entry(frame_bmi, width=5)
entry_feet.grid(row=1, column=2, padx=10, pady=5)

label_inches = tk.Label(frame_bmi, text="Inches:")
label_inches.grid(row=1, column=3, padx=10, pady=5)

entry_inches = tk.Entry(frame_bmi, width=5)
entry_inches.grid(row=1, column=4, padx=10, pady=5)

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=10)

label_result = tk.Label(root, text="BMI: --", font=("Arial", 14))
label_result.pack(pady=5)

label_category = tk.Label(root, text="Category: --", font=("Arial", 12))
label_category.pack(pady=5)

# Exercise logging section
frame_exercise = tk.Frame(root)
frame_exercise.pack(pady=10)

label_exercise = tk.Label(frame_exercise, text="Exercise:")
label_exercise.grid(row=0, column=0, padx=10, pady=5)

entry_exercise = tk.Entry(frame_exercise)
entry_exercise.grid(row=0, column=1, padx=10, pady=5)

label_duration = tk.Label(frame_exercise, text="Duration (min):")
label_duration.grid(row=1, column=0, padx=10, pady=5)

entry_duration = tk.Entry(frame_exercise)
entry_duration.grid(row=1, column=1, padx=10, pady=5)

button_log = tk.Button(root, text="Log Exercise", command=log_exercise)
button_log.pack(pady=10)

# Exercise log display area
text_log = tk.Text(root, height=10, width=40)
text_log.pack(pady=10)

# Clear Button
button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.pack(pady=10)

# Start the GUI loop
root.mainloop()