from tkinter import *
import csv
import os

def button_on_click():
    try:
        name = user_name.get().strip()
        if name == "":
            result.config(text="Please enter your name")
            return

        h = float(height.get())
        w = float(weight.get())

        if h <= 0 or w <= 0:
            result.config(text="Enter positive numbers only")
            return

        bmi = round(w / (h ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        filename = "data.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

            if not file_exists:
                writer.writerow(["Name", "Weight (kg)", "Height (m)", "BMI", "Category"])

            writer.writerow([name, w, h, bmi, category])

        result.config(text=f"Your BMI is {bmi}\nCategory: {category}")

    except ValueError:
        result.config(text="Please enter valid numbers")

# ---------------- GUI ----------------

window = Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=300)

Label(window, text="User Name").grid(row=0, column=0)
Label(window, text="Weight(kg)").grid(row=1, column=0)
Label(window, text="Height (m)").grid(row=2, column=0)
Label(window, text="Result").grid(row=3, column=0)

user_name = Entry(window)
weight = Entry(window)
height = Entry(window)

user_name.grid(row=0, column=1)
weight.grid(row=1, column=1)
height.grid(row=2, column=1)

Button(window, text="Calculate BMI", command=button_on_click).grid(row=4, column=1)

result = Label(window, text="")
result.grid(row=3, column=1)

window.mainloop()
