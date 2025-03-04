import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk  # For images
from datetime import datetime  # For date/time functionality

# Main Window
root = tk.Tk()
root.title("Fitness Application")
root.geometry("600x800")  # Adjust the window size to fit content

# Open image files (paths updated for your system)
image_path1 = 'C:/Users/dhipo/OneDrive/Software Dev/Myfitness/image1.jpg'
image_path2 = 'C:/Users/dhipo/OneDrive/Software Dev/Myfitness/image2.jpg'

# Load images using PIL
image1 = Image.open(image_path1)
image2 = Image.open(image_path2)

# Reduce image sizes by 50%
width1, height1 = image1.size
width2, height2 = image2.size

# Scale the images by 50%
new_width1 = int(width1 * 0.5)
new_height1 = int(height1 * 0.5)
new_width2 = int(width2 * 0.5)
new_height2 = int(height2 * 0.5)

# Resize images to 50% of the original size
image1_resized = image1.resize((new_width1, new_height1))
image2_resized = image2.resize((new_width2, new_height2))

# Convert the resized images for Tkinter
photo1 = ImageTk.PhotoImage(image1_resized)
photo2 = ImageTk.PhotoImage(image2_resized)

# Create a frame to hold the images
frame_images = tk.Frame(root)
frame_images.pack(pady=10)

# Display Image1
label_image1 = tk.Label(frame_images, image=photo1)
label_image1.grid(row=0, column=0, padx=10)

# Display Image2
label_image2 = tk.Label(frame_images, image=photo2)
label_image2.grid(row=0, column=1, padx=10)

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

# Title Label
label_title = tk.Label(root, text="Fitness Application", font=("Arial", 18))
label_title.pack(pady=10)

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

# Exercise Logging Section
frame_exercise = tk.Frame(root)
frame_exercise.pack(pady=10)

label_exercise = tk.Label(frame_exercise, text="Exercise:")
label_exercise.grid(row=0, column=0, padx=5, pady=5)
entry_exercise = tk.Entry(frame_exercise)
entry_exercise.grid(row=0, column=1, padx=5, pady=5)

label_duration = tk.Label(frame_exercise, text="Duration (min):")
label_duration.grid(row=1, column=0, padx=5, pady=5)
entry_duration = tk.Entry(frame_exercise)
entry_duration.grid(row=1, column=1, padx=5, pady=5)

button_log = tk.Button(root, text="Log Exercise", command=log_exercise)
button_log.pack(pady=10)

text_log = tk.Text(root, height=10, width=50)
text_log.pack(pady=10)

# Exit Button
button_exit = tk.Button(root, text="Exit", command=root.quit)
button_exit.pack(pady=10)

root.mainloop()
