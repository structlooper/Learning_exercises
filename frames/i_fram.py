import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('i_frame')

label_frame = ttk.LabelFrame(win, text = "Enter your details below")
label_frame.grid(row=0,column=0,sticky=tk.W,padx = 100)

name_lable = ttk.Label(label_frame,text = 'Enter your name : ')
name_lable.grid(row=0, column=0,sticky=tk.W)

email_lable = ttk.Label(label_frame, text = 'Enter your email : ')
email_lable.grid(row=1,column=0,sticky=tk.W)

age_lable =  ttk.Label(label_frame,text = 'Enter your age : ')
age_lable.grid(row=2,column=0,sticky =tk.W)

gender_lable =  ttk.Label(label_frame,text = 'Select your gender : ')
gender_lable.grid(row=4,column=0,sticky =tk.W)

# values assied_variables...
name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.IntVar()
gender_var = tk.StringVar()
usertype = tk.StringVar()
check_btn_var = tk.StringVar()

# inputs....
name_entrybox = ttk.Entry(label_frame, width=16, textvariable = name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_entrybox = ttk.Entry(label_frame, width=16, textvariable = email_var)
email_entrybox.grid(row=1,column=1)

age_entrybox = ttk.Entry(label_frame, width=16, textvariable = age_var)
age_entrybox.grid(row=2,column=1)

#combobox...
gender = ttk.Combobox(label_frame, width=13, textvariable = gender_var ,state = 'readonly' )
gender['values'] = ('male','female','other') 
gender.current(0)
gender.grid(row=4, column= 1)

# function.....
def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    gender_value = gender_var.get()
    user_type = usertype.get()
    if check_btn_var.get() == 1:
        subsscribed = 'Suscribed'
    else:
        subsscribed = 'not Suscribed'

    # write in txt file.........
    # with open('file_output.txt','a') as f:
    #     f.write(f'hello {user_name} and you are {gender_value}\n Your email is {user_email} and age is {user_age}\n You are {user_type} and {subsscribed} to this channal\n \n')
    
    print(f"hello {user_name},{user_age},{user_email},{gender_value},{user_type},{subsscribed}")

    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_lable.configure(foreground = 'Blue') #hexa value color can passed with '#'
    email_lable.configure(foreground = 'Blue') #hexa value color can passed with '#'
    age_lable.configure(foreground = 'Blue') #hexa value color can passed with '#'

# radio button...
radio_btn1 = ttk.Radiobutton(label_frame,text ='Student', value='student', variable= usertype)
radio_btn1.grid(row=5 ,column = 0)
radio_btn2 = ttk.Radiobutton(label_frame,text ='Teacher', value='teacher', variable= usertype)
radio_btn2.grid(row=5 ,column = 1)

# check button............
check_btn = ttk.Checkbutton(label_frame,text='check to suscribe', variable = check_btn_var)
check_btn.grid(row=6,columnspan=2,sticky=tk.W)


# button....
submit_button = ttk.Button(label_frame,text = 'submit', command=action)
submit_button.grid(row=10,column=1,sticky=tk.E)

# for acces items inside label_frame
for child in label_frame.winfo_children():
    child.grid_configure(padx = 5,pady=5)

win.mainloop()