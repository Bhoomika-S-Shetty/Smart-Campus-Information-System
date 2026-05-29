import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from datetime import datetime

students=[]

# ---------------- Register Student ----------------

def register():

    win=tk.Toplevel(root)
    win.title("Student Registration")
    win.geometry("300x400")

    tk.Label(win,text="Name").pack()
    name=tk.Entry(win)
    name.pack()

    tk.Label(win,text="Student ID").pack()
    sid=tk.Entry(win)
    sid.pack()

    tk.Label(win,text="Department").pack()
    dept=tk.Entry(win)
    dept.pack()

    tk.Label(win,text="Marks").pack()
    marks=tk.Entry(win)
    marks.pack()

    tk.Label(win,text="Attendance (%)").pack()
    attend=tk.Entry(win)
    attend.pack()

    def save():

        try:

            data={
                "Name":name.get(),
                "ID":sid.get(),
                "Dept":dept.get(),
                "Marks":int(marks.get()),
                "Attendance":float(attend.get())
            }

            students.append(data)

            with open("students.txt","a") as f:
                f.write(str(data)+"\n")

            messagebox.showinfo(
                "Success",
                "Student Registered"
            )

            win.destroy()

        except:
            messagebox.showerror(
                "Error",
                "Enter valid values"
            )

    tk.Button(
        win,
        text="Save",
        bg="green",
        fg="white",
        command=save
    ).pack(pady=15)

# ---------------- Records ----------------

def records():

    win=tk.Toplevel(root)
    win.title("Student Records")
    win.geometry("500x400")

    text=tk.Text(win)

    text.pack(fill="both",expand=True)

    for s in students:

        text.insert(
            tk.END,
            f"Name:{s['Name']}\n"
            f"ID:{s['ID']}\n"
            f"Dept:{s['Dept']}\n"
            f"Marks:{s['Marks']}\n"
            f"Attendance:{s['Attendance']}%\n"
            "----------------------\n"
        )

# ---------------- Search ----------------

def search():

    win=tk.Toplevel(root)

    win.title("Search Student")

    tk.Label(
        win,
        text="Enter Student ID"
    ).pack()

    sid=tk.Entry(win)
    sid.pack()

    def find():

        for s in students:

            if s["ID"]==sid.get():

                messagebox.showinfo(
                    "Found",
                    str(s)
                )
                return

        messagebox.showerror(
            "Not Found",
            "Student not found"
        )

    tk.Button(
        win,
        text="Search",
        command=find
    ).pack()

# ---------------- Delete ----------------

def delete():

    win=tk.Toplevel(root)

    tk.Label(
        win,
        text="Enter ID"
    ).pack()

    sid=tk.Entry(win)
    sid.pack()

    def remove():

        global students

        students=[
            x for x in students
            if x["ID"]!=sid.get()
        ]

        messagebox.showinfo(
            "Deleted",
            "Record removed"
        )

    tk.Button(
        win,
        text="Delete",
        command=remove
    ).pack()

# ---------------- Fees ----------------

def fees():

    win=tk.Toplevel(root)

    win.title("Fee Calculator")

    tk.Label(win,text="Tuition Fee").pack()

    t=tk.Entry(win)
    t.pack()

    tk.Label(win,text="Exam Fee").pack()

    e=tk.Entry(win)
    e.pack()

    tk.Label(win,text="Library Fee").pack()

    l=tk.Entry(win)
    l.pack()

    def calculate():

        total=(
            int(t.get())+
            int(e.get())+
            int(l.get())
        )

        messagebox.showinfo(
            "Total Fee",
            total
        )

    tk.Button(
        win,
        text="Calculate",
        command=calculate
    ).pack()

# ---------------- Grades ----------------

def grades():

    win=tk.Toplevel(root)

    tk.Label(
        win,
        text="Enter Marks"
    ).pack()

    m=tk.Entry(win)
    m.pack()

    def grade():

        marks=int(m.get())

        if marks>=90:
            g="A"

        elif marks>=75:
            g="B"

        elif marks>=50:
            g="C"

        else:
            g="Fail"

        messagebox.showinfo(
            "Grade",
            g
        )

    tk.Button(
        win,
        text="Generate Grade",
        command=grade
    ).pack()

# ---------------- Performance Graph ----------------

def performance():

    if len(students)==0:

        messagebox.showerror(
            "Error",
            "No data"
        )
        return

    names=[]
    marks=[]

    for s in students:

        names.append(
            s["Name"]
        )

        marks.append(
            s["Marks"]
        )

    plt.bar(
        names,
        marks
    )

    plt.xlabel(
        "Students"
    )

    plt.ylabel(
        "Marks"
    )

    plt.title(
        "Performance Analysis"
    )

    plt.show()

# ---------------- Main Window ----------------

root=tk.Tk()
root.geometry("1920x1080")
bg_image = Image.open("campus_bg.png")   # your campus image
bg_image = bg_image.resize((1920, 1080))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title_frame = tk.Frame(root, bg="white")
title_frame.place(
    relx=0.5,
    y=90,
    anchor="center"
)
tk.Label(
    title_frame,
    text="🎓 SMART CAMPUS INFORMATION SYSTEM",
    font=("Segoe UI", 34, "bold"),
    bg="white",
    fg="#0B2E83"
).pack()

tk.Label(
    title_frame,
    text="Empowering Education. Inspiring Futures.",
    font=("Segoe UI", 14),
    bg="white",
    fg="gray"
).pack()

cards = [
("📋 Registration", register, "#4F46E5", 350, 220),
("📑 Records", records, "#10B981", 600, 220),
("🔍 Search", search, "#8B5CF6", 850, 220),

("🗑 Delete", delete, "#EF4444", 350, 430),
("💰 Fees", fees, "#F59E0B", 600, 430),
("🎓 Grades", grades, "#EC4899", 850, 430),

("📊 Performance", performance, "#06B6D4", 600, 620)
]

row = 0
col = 0
def enter(e):
    e.widget.config(bg="#2563EB")

def leave(e, color):
    e.widget.config(bg=color)
for text, cmd, color,x,y in cards:

    btn = tk.Button(
        root,
    text=text,
    command=cmd,
    bg=color,
    fg="white",
    font=("Segoe UI",16,"bold"),
    relief="flat",
    width=14,
    height=4,
    bd=0
)
    btn.config(
    activebackground=color,
    activeforeground="white"
)
    btn.place(x=x, y=y)

    btn.bind("<Enter>", enter)
    btn.bind("<Leave>",
         lambda e, c=color: leave(e, c))

    col += 1

    if col > 2:
        col = 0
        row += 1

root.mainloop()