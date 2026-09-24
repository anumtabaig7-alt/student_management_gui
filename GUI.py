import tkinter as tk
from tkinter import messagebox
students = [(100,"alice"),(101,"anum"),(102,"james"),(103,"alex"),(104,"sarah"),(105,"teresa")]
students.append((106,"tom"))
info_stud = {"alice": {"age": 20, "major":"cs"}, "anum": {"age":20, "major" : "cs"}, "james":{"age":21 ,"major":"python"},"alex":{"age":22, "major": "python"},"sarah": {"age":20 ,"major":"cs"}}
info_stud["teresa"] = {"age": 22 , "major": "python"}

root = tk.Tk()
root.configure(bg="#2B1B2A")
frame_welcome = tk.Frame(root, bg="#2B1B2A")
frame_add_stu = tk.Frame(root, bg="#4D2A3A")
frame_search = tk.Frame(root, bg="#4D2A3A")
frame_searchage = tk.Frame(root, bg="#4D2A3A")
frame_searchmajor = tk.Frame(root, bg="#4D2A3A")

def search_student() :
    cleansearch = entry_name1.get().strip().lower()
    if cleansearch in info_stud:
        profile = info_stud[cleansearch]
        messagebox.showinfo(
            "student found",
            f"\n ✅ FOUND : {cleansearch.capitalize()}\n Major : {profile['major']}\n Age : {profile['age']}"
        )
    else:
        messagebox.showwarning(
            "no student found",
            f"\n ❌ COULDN'T FIND : {cleansearch.capitalize()}"
        )
    entry_name1.delete(0, tk.END)


def search_by_major() :
    grouped_major: dict[str, list[str]] = {}
    for name, profile in info_stud.items() :
        major = profile["major"]
        if major not in grouped_major :
            grouped_major[major] = []
        grouped_major[major].append(name.capitalize())

    inmajor = entry_major1.get().strip().lower()
    if not inmajor:
        messagebox.showwarning("INPUT ERROR", "ENTER MAJOR FIRST")
        return
    if inmajor in grouped_major:
        messagebox.showinfo("found", f"{inmajor} students: {grouped_major[inmajor]}")
    else:
        messagebox.showinfo("not found", f"NO STUDENTS IN {inmajor}")
    entry_major1.delete(0, tk.END)


def search_by_age():
    groupedage: dict[int, list[str]] = {}
    for name, profile in info_stud.items():
        age = profile["age"]
        if age not in groupedage:
            groupedage[age] = []
        groupedage[age].append(name.capitalize())

    strage = entry_age1.get().strip()
    try:
        intage = int(strage)
    except ValueError:
        messagebox.showerror("INPUT ERROR", "ENTER VALID AGE")
        entry_age1.delete(0, tk.END)
        return

    if intage in groupedage:
        num = len(groupedage[intage])
        messagebox.showinfo("found", f"{num} students found of age {intage}\n{intage} age students: {groupedage[intage]}")
    else:
        messagebox.showinfo("NO STUDENTS FOUND", f"NO STUDENTS FOUND OF AGE {intage}")
    entry_age1.delete(0, tk.END)


def add_stu() :
    name = entry_name.get().strip().lower()
    agestr = entry_age.get().strip()
    major = entry_major.get().strip().lower()
    try:
        intage = int(agestr)
    except ValueError:
        messagebox.showwarning("INPUT ERROR", "PLEASE ENTER A VALID AGE")
        return

    if not name or not major:
        messagebox.showwarning("INPUT ERROR", "FILL ALL FIELDS FIRST")
        return
    else:
        if name not in info_stud:
            info_stud[name] = {"age": intage, "major": major}
            messagebox.showinfo("STUDENT HAS BEEN ADDED SUCCESSFULLY")
        else:
            messagebox.showwarning("STUDENT ALREADY IN RECORD")
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_major.delete(0, tk.END)
def add_stu_page ():
   frame_welcome.pack_forget()
   frame_add_stu.pack(fill = "both" ,expand = True)
def show_welcome_page () :
   frame_add_stu.pack_forget()
   frame_welcome.pack(fill = "both",expand = True)
def show_searchpage ():
   frame_welcome.pack_forget()
   frame_search.pack(fill = "both", expand = True)
def show_searchagepage ():
   frame_welcome.pack_forget()
   frame_searchage.pack(fill = "both", expand = True) 
def show_searchmajorpage ():
   frame_welcome.pack_forget()
   frame_searchmajor.pack(fill = "both", expand = True)
def clear_screen():
   for frame in [frame_welcome,frame_add_stu,frame_search,frame_searchage,frame_searchmajor] :
      frame.pack_forget()
def go_home():
   clear_screen()
   frame_welcome.pack(fill = "both",expand = True )      




root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("550x500")

show_welcome_page()

label_welcome = tk.Label(frame_welcome, text="Main Menu", font=("Arial", 16, "bold"), bg="#2B1B2A", fg="#F9DCE6")
label_welcome.pack(pady=40)

addstu_btn = tk.Button(frame_welcome , text = "Add a new student" , command = add_stu_page , bg ="#FFB6C1" , fg ="white" , font = ("Arial" , 11 , "bold") , height = 2 , relief="flat",bd=0,highlightthickness=0)
addstu_btn.pack(pady= 15)
search_stubtn = tk.Button(frame_welcome , text = "Search student by name " , command = show_searchpage , bg ="#FFB6C1" , fg ="white" , font = ("Arial" , 11 , "bold" ), height = 2 ,  relief="flat",bd=0,highlightthickness=0)
search_stubtn.pack(pady = 15)
search_by_agebtn = tk.Button(frame_welcome , text = "Search student by age" , command = show_searchagepage , bg ="#FFB6C1" , fg ="white" , font = ("Arial" , 11 , "bold"),height = 2 ,  relief="flat",bd=0,highlightthickness=0 )
search_by_agebtn.pack(pady = 15)
search_by_majorbtn = tk.Button(frame_welcome , text = "Search student by major" , command = show_searchmajorpage , bg ="#FFB6C1" , fg ="white" , font = ("Arial" , 11 , "bold"),height = 2 , relief="flat",bd=0,highlightthickness=0 )
search_by_majorbtn.pack(pady = 15)


label_title1 = tk.Label(frame_add_stu, text="Add new student", font=("Times New Roman", 16, "bold"), bg="#4D2A3A", fg="#F9DCE6")
label_title1.pack(pady=15, anchor="w", padx=30)

tk.Label(frame_add_stu,text = "Enter Name", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_name = tk.Entry(frame_add_stu, width=35)
entry_name.pack(pady=5)

tk.Label(frame_add_stu,text = "Enter Age", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_age = tk.Entry(frame_add_stu, width=35)
entry_age.pack(pady=5)

tk.Label(frame_add_stu,text = "Enter Major", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_major = tk.Entry(frame_add_stu, width=35)
entry_major.pack(pady=5)

btn_submit = tk.Button(frame_add_stu, text="Save Student", command=add_stu,bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 ,  relief="flat",bd=0,highlightthickness=0) 
btn_submit.pack(pady=15)

btn_back = tk.Button(frame_add_stu, text = "back to home page", command = go_home ,bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 , relief="flat",bd=0,highlightthickness=0) 
btn_back.pack(pady=15)



label_title2 = tk.Label(frame_search, text="Search student", font=("Arial", 16, "bold"), bg="#4D2A3A", fg="#F9DCE6")
label_title2.pack(pady=15, anchor="w", padx=30)

tk.Label(frame_search,text = "Enter Name", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_name1 = tk.Entry(frame_search, width=35)
entry_name1.pack(pady=5)

btn_submit1 = tk.Button(frame_search, text="Search", command=search_student, bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 ,  relief="flat",bd=0,highlightthickness=0)
btn_submit1.pack(pady=15)

btn_back1 = tk.Button(frame_search, text = "back to home page", command = go_home ,bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 ,  relief="flat",bd=0,highlightthickness=0) 
btn_back1.pack(pady=16)


label_title3 = tk.Label(frame_searchage, text="Find students by age", font=("Arial", 16, "bold"), bg="#4D2A3A", fg="#F9DCE6")
label_title3.pack(pady=15, anchor="w", padx=30)

tk.Label(frame_searchage,text = "Enter Age", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_age1 = tk.Entry(frame_searchage, width=35)
entry_age1.pack(pady=5)

btn_submit2 = tk.Button(frame_searchage, text="Search", command=search_by_age, bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 ,  relief="flat",bd=0,highlightthickness=0)
btn_submit2.pack(pady=15)

btn_back2 = tk.Button(frame_searchage, text = "back to home page", command = go_home ,bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 ,  relief="flat",bd=0,highlightthickness=0) 
btn_back2.pack(pady=16)

label_title4 = tk.Label(frame_searchmajor, text="Find students by major", font=("Arial", 16, "bold"), bg="#4D2A3A", fg="#F9DCE6")
label_title4.pack(pady=15, anchor="w", padx=30)

tk.Label(frame_searchmajor,text = "Enter Major", font =("Arial",16 ,"bold")).pack(anchor ="w", padx = 30)
entry_major1 = tk.Entry(frame_searchmajor, width=35)
entry_major1.pack(pady=5)

btn_submit3 = tk.Button(frame_searchmajor, text="Search", command=search_by_major, bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15 , height = 2 , relief="flat",bd=0,highlightthickness=0)
btn_submit3.pack(pady=15)

btn_back3 = tk.Button(frame_searchmajor, text = "back to home page", command = go_home,bg="#AF4C89", fg="white", font=("Arial", 10, "bold"), width=15, height = 2 , relief="flat",bd=0,highlightthickness=0) 
btn_back3.pack(pady = 16)

root.mainloop()
















                       
    

     
   
     

