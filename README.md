# 🎓 Student Performance Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Math-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

> **A powerful desktop application to manage student grades, perform statistical analysis, and automate grading curves using Python.**

---

## 🚀 Overview

The **Student Performance Dashboard** is a GUI-based data analysis tool designed for teachers and administrators. It allows for real-time entry of student marks and leverages the power of **NumPy** and **Pandas** to perform instant calculations—including class averages, detailed statistical breakdowns, and automated grade curving via vectorization.

## ✨ Key Features

* **📝 Data Entry System:** Intuitive interface to add student names and marks dynamically.
* **📊 Real-Time Analytics:** Instantly calculate Class Average using **Pandas**.
* **🧠 Deep Stats (NumPy):** View advanced metrics like **Median**, **Max**, and **Min** scores with a single click.
* **⚡ Grade Curving (Broadcasting):** Uses NumPy's powerful *broadcasting* feature to add bonus points (+5) to the entire class instantly, without using loops.
* **🧹 Data Management:** Clear input fields or reset the entire dataset easily.
* **🖥️ Live Display:** View the updated class roster and statistics in a scrollable text area.

---

## 🛠️ Tech Stack

| Component | Library | Purpose |
| :--- | :--- | :--- |
| **GUI** | `tkinter` | Building the window, frames, buttons, and layout. |
| **Data** | `pandas` | Storing records in a structured DataFrame. |
| **Math** | `numpy` | High-performance array operations (Broadcasting & Stats). |

---

## 💻 How to Run

1.  **Clone the Repository**
    ```bash
    git clone git@github.com:nolifer-jpg/Student-Performace-Dashboard.git
    cd Student-Performace-Dashboard
    ```

2.  **Install Dependencies**
    You need `pandas` and `numpy` installed.
    ```bash
    pip install pandas numpy
    ```

3.  **Run the Application**
    ```bash
    python main.py
    ```

---

## 🧠 Code Highlight: NumPy Broadcasting

One of the coolest features of this app is how it handles grade curving. Instead of a slow `for` loop, we use **NumPy Broadcasting** to update thousands of records instantly:

```python
def curve_grades():
    # Convert Pandas column to high-speed NumPy array
    marks_array = df["Marks"].to_numpy()
    
    # Broadcast: Add 5 to every single item simultaneously
    new_marks = marks_array + 5
    
    # Update DataFrame
    df["Marks"] = new_marks
    
🚀 Future Roadmap
[ ] Add Save/Load functionality (CSV/Excel support).

[ ] Visualize data with Matplotlib charts (Histograms/Bar charts).

[ ] Add grade letter assignment (A, B, C) based on score ranges.

```
Just me exploring Data Science & GUI Development.
