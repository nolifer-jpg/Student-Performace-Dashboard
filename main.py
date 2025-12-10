import tkinter as tk

import numpy as np
import pandas as pd

df = pd.DataFrame(columns=["Name", "Marks"])


def add_student():
    name_value = name.get()
    marks_value = marks.get()
    df.loc[len(df)] = [name_value, marks_value]
    text.delete("1.0", tk.END)
    text.insert(tk.END, df.to_string())


def calculate_avg():
    df["Marks"] = pd.to_numeric(df["Marks"])
    avg = df["Marks"].mean()

    text.insert(tk.END, f"\n\nClass Average: {avg:.2f}")


def clear_text():
    text.delete("1.0", tk.END)


def refresh_screen():
    text.delete("1.0", tk.END)
    text.insert(tk.END, df.to_string(index=False))


def curve_grades():
    marks_array = np.array([df["marks"].to_numpy])
    new_marks = marks_array + 5
    df["Marks"] = new_marks
    refresh_screen()
    text.insert(tk.END, "\n\n[System] Grades Curved by +5!")


def detailed_stats():
    marks_array = np.array([df["Marks"].to_numpy()])
    median_score = np.median(marks_array)
    max_score = np.max(marks_array)
    min_score = np.min(marks_array)
    text.insert(
        tk.END,
        f"\n\nMedian Score: {median_score:.2f} | Max Score: {max_score} | Min Score: {min_score}",
    )


root = tk.Tk()
root.title("Student Dashboard")
root.geometry("400x400")

input_frame = tk.Frame(root, bg="lightgray")
input_frame.pack()

output_frame = tk.Frame(root)
output_frame.pack()

text = tk.Text(output_frame, height=10)
text.pack()

lbl1 = tk.Label(input_frame, text="Name")
name = tk.Entry(input_frame)

lbl2 = tk.Label(input_frame, text="Marks")
marks = tk.Entry(input_frame)

add_stud = tk.Button(input_frame, text="Add", command=add_student)
analyze_stud = tk.Button(input_frame, text="Analyze", command=calculate_avg)
clear_chat = tk.Button(input_frame, text="Clear Chat", command=clear_text)
curve_grade = tk.Button(input_frame, text="Curve(+5)", command=curve_grades)
detailed = tk.Button(input_frame, text="Detailed Stats", command=detailed_stats)


lbl1.grid(row=0, column=0)
name.grid(row=0, column=1)

lbl2.grid(row=1, column=0)
marks.grid(row=1, column=1)

add_stud.grid(row=2, column=0, columnspan=2)
analyze_stud.grid(row=3, column=0, columnspan=2)
curve_grade.grid(row=4, column=0)
detailed.grid(row=4, column=1)
clear_chat.grid(row=5, column=0, columnspan=2)
root.mainloop()
