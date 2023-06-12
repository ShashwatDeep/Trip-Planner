from tkinter import *
import os
import webbrowser

countries=["India"]
my_dict={"India":["Delhi","Jaipur","Ahmedabad","Kullu","Bangalore","Kolkata","Chennai","Goa","Hyderabad","Amritsar"]}
my_IATA={"India":["DEL","JAI","AMD","KUU","BLR","CCU","MAA","GOI","HYD","ATQ"]}

def delete2():
  screen3.destroy()
  screen2.destroy()
  session()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def delete5():
  screen10.destroy()
  
def delete6():
  screen1.destroy()

def delete7():
  screen2.destroy()

def delete8():
  screen6.destroy()

def flight_go():
  index_info=index.get()
  url_mmtflight = "https://www.makemytrip.com/flight/search?itinerary=BOM-"+(my_IATA["India"][index_info-1])+"-13/12/2021&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng"
  webbrowser.open(url_mmtflight)

def flight_booking():
  index_info=index.get()
  if index_info<1 or index_info>10 :
    global screen10
    screen10 = Toplevel()
    screen10.configure(bg='red')

    app_width = 250
    app_height = 250
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen10.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    screen10.title("Error")
    Label(screen10, text = "Please enter a valid index (1-10)", bg='red', font = ("Times New Roman", 13)).pack()
    Button(screen10, text = "OK", bg='light green', command =delete5).pack()
  else:
    global screen9
    index_info=index.get()
    screen9 = Toplevel()
    screen9.configure(bg='orange')

    app_width = 500
    app_height = 500
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen9.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    screen9.title("Flight Bookings")
    Label(screen9, text = "The destination selected by you is : "+(my_dict["India"][index_info-1])+"\n", bg='orange').pack()
    Button(screen9, text = "Continue to website", bg='light green', width = 30, height = 1, command = flight_go).pack()
    Label(screen9, text = "", bg='orange').pack()
    Label(screen9, text = "Or else, you have one of the following options.\n", bg='orange').pack()
    Button(screen9, text = "Know More", bg='light green', width = 15, height = 1, command = know_more).pack()
    Button(screen9, text = "Hotel Bookings", bg='light green', width = 20, height = 1, command = hotel_booking).pack()
    Button(screen9, text = "Back", bg='light green', width = 10, height = 1, command = screen9.destroy).pack(side=LEFT, padx=15,pady=20)
    Button(screen9, text = "Quit", bg='light green', width = 10, height = 1, command = screen9.quit).pack(side=RIGHT, padx=15,pady=20)

def hotel_go():
  index_info=index.get()
  url_mmthotel = "https://www.makemytrip.com/hotels/hotel-listing/?checkin=12132021&city=CT"+(my_IATA["India"][index_info-1])+"&checkout=12142021&roomStayQualifier=2e0e&locusId=CT"+(my_IATA["India"][index_info-1])+"&country=IN&locusType=city&searchText="+(my_dict["India"][index_info-1])+"&visitorId=9ac049be-1f06-4321-b2b9-4a3bc71bdd19&regionNearByExp=3"
  webbrowser.open(url_mmthotel)

def hotel_booking():
  index_info=index.get()
  if index_info<1 or index_info>10 :
    global screen10
    screen10 = Toplevel()
    screen10.configure(bg='red')

    app_width = 250
    app_height = 250
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen10.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    screen10.title("Error")
    Label(screen10, text = "Please enter a valid index (1-10)", bg='red', font = ("Times New Roman", 13)).pack()
    Button(screen10, text = "OK", bg='light green', command =delete5).pack()
  else:
    global screen8
    index_info=index.get()
    screen8 = Toplevel()
    screen8.configure(bg='orange')

    app_width = 500
    app_height = 500
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen8.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    screen8.title("Hote Bookings")
    Label(screen8, text = "The destination selected by you is : "+(my_dict["India"][index_info-1])+"\n", bg='orange').pack()
    Button(screen8, text = "Continue to website", bg='light green', width = 30, height = 1, command = hotel_go).pack()
    Label(screen8, text = "", bg='orange').pack()
    Label(screen8, text = "Or else, you have one of the following options.\n", bg='orange').pack()
    Button(screen8, text = "Know More", bg='light green', width = 15, height = 1, command = know_more).pack()
    Button(screen8, text = "Flight Bookings", bg='light green', width = 20, height = 1, command = flight_booking).pack()
    Button(screen8, text = "Back", bg='light green', width = 10, height = 1, command = screen8.destroy).pack(side=LEFT, padx=15,pady=20)
    Button(screen8, text = "Quit", bg='light green', width = 10, height = 1, command = screen8.quit).pack(side=RIGHT, padx=15,pady=20)
  
def know_more_go():
  index_info=index.get()
  url_knowmore = "https://en.wikipedia.org/wiki/"+(my_dict["India"][index_info-1])
  webbrowser.open(url_knowmore)

def know_more():
  index_info=index.get()
  if index_info<1 or index_info>10 :
    global screen10
    screen10 = Toplevel()
    screen10.configure(bg='red')

    app_width = 250
    app_height = 250
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen10.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    screen10.title("Error")
    Label(screen10, text = "Please enter a valid index (1-10)", bg='red', font = ("Times New Roman", 13)).pack()
    Button(screen10, text = "OK", bg='light green', command =delete5).pack()
  else:
    global screen7
    screen7 = Toplevel()
    screen7.configure(bg='orange')

    app_width = 500
    app_height = 500
  
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    screen7.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    screen7.title("Know More")
    Label(screen7, text = "To know more about the city click the button below.\n", bg='orange').pack()
    Button(screen7, text = "Go", bg='light green', width = 10, height = 1, command = know_more_go).pack()
    Label(screen7, text = "", bg='orange').pack()
    Label(screen7, text = "Or else, you have one of the following options.\n", bg='orange').pack()
    Button(screen7, text = "Hotel Bookings", bg='light green', width = 15, height = 1, command = hotel_booking).pack()
    Button(screen7, text = "Flight Bookings", bg='light green', width = 20, height = 1, command = flight_booking).pack()
    Button(screen7, text = "Back", bg='light green', width = 10, height = 1, command = screen7.destroy).pack(side=LEFT, padx=15,pady=20)
    Button(screen7, text = "Quit", bg='light green', width = 10, height = 1, command = screen7.quit).pack(side=RIGHT, padx=15,pady=20)

def session():
  global screen6
  global index
  global city_index
  index=IntVar()
  screen6 = Toplevel()
  screen6.configure(bg='orange')

  app_width = 500
  app_height = 500
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen6.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

  screen6.title("Home")
  Label(screen6, text = "Hello, welcome to your very own trip planner!\nOur services will extend to various countries. Right now, we can offer you a quality time in India.\nIn India we offer a tour in one of the following cities:", bg = "black", fg='white', width = "300", font = ("Times New Roman", 9)).pack()
  i=1
  for v in my_dict["India"]:
    Label(screen6, anchor = "w", text = str(i)+". "+str(v), bg='orange', width=600, font=('Calibri',10,'bold')).pack()
    i+=1
  Label(screen6, anchor = "w", text = "\nSo tell us! Which city do you plan do go to? Enter its index number: ", bg='orange', width=600, font=('Calibri',10,'bold')).pack()
  city_index = Entry(screen6, textvariable = index)
  city_index.pack()
  
  Button(screen6, text = "Know More", bg='light green', width = 10, height = 1, command = know_more).pack()
  Button(screen6, text = "Hotel Bookings", bg='light green', width = 15, height = 1, command = hotel_booking).pack()
  Button(screen6, text = "Flight Bookings", bg='light green', width = 20, height = 1, command = flight_booking).pack()
  Label(screen6, text = "", bg='orange').pack()
  Button(screen6, text = "Exit", bg='light green', width = 10, height = 1, command = delete8).pack()
  
def login_sucess():
  global screen3
  screen3 = Toplevel()
  screen3.configure(bg='light green')

  app_width = 250
  app_height = 250
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen3.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

  screen3.title("Success")
  Label(screen3, text = "Login Sucess",bg='light green', font = ("Times New Roman", 13)).pack()
  Button(screen3, text = "OK", bg='orange', command =delete2).pack()
  
def password_not_recognised():
  global screen4
  screen4 = Toplevel()
  screen4.configure(bg='red')

  app_width = 250
  app_height = 250
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen4.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

  screen4.title("Error")
  Label(screen4, text = "Password Error", bg='red', font = ("Times New Roman", 13)).pack()
  Button(screen4, text = "OK", bg='light green', command =delete3).pack()

def user_not_found():
  global screen5
  screen5 = Toplevel()
  screen5.configure(bg='red')
  
  app_width = 250
  app_height = 250
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen5.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  
  screen5.title("Error")
  Label(screen5, text = "User Not Found", bg='red', font = ("Times New Roman", 13)).pack()
  Button(screen5, text = "OK", bg='light green', command =delete4).pack()

def register_user():
  print("working")
  
  fname_info = fname.get()
  lname_info = lname.get()
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info+"\n")
  file.write(fname_info+"\n")
  file.write(lname_info+"\n")
  file.close()

  fname_entry.delete(0, END)
  lname_entry.delete(0, END)
  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", bg='orange' , fg = "green" ,font = ("calibri", 11, 'bold')).pack()
  
def login_verify():
  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()

  else:
        user_not_found()
  
def register():
  global screen1
  screen1 = Toplevel()
  screen1.configure(bg='orange')

  app_width = 500
  app_height = 500
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen1.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
  
  screen1.title("Register")
  
  
  global fname
  global lname
  global username
  global password
  global fname_entry
  global lname_entry
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  fname = StringVar()
  lname = StringVar()

  Label(screen1, text = "Please enter details below to register", bg = "black", fg='white', width = "300", height = "2", font = ("Times New Roman", 13)).pack()
  Label(screen1, text = "", bg='orange').pack()
  Label(screen1, text = "First Name * ", bg='light green').pack()
  fname_entry = Entry(screen1, textvariable = fname)
  fname_entry.pack()
  Label(screen1, text = "Last Name * ", bg='light green').pack()
  lname_entry = Entry(screen1, textvariable = lname)
  lname_entry.pack()
  Label(screen1, text = "Username * ", bg='light green').pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ", bg='light green').pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "", bg='orange').pack()
  Button(screen1, text = "Register", bg='light green', width = 10, height = 1, command = register_user).pack()
  Label(screen1, text = "", bg='orange').pack()
  Button(screen1, text = "Exit", bg='light green',height = "1", width = "10", command = delete6).pack()

def login():
  global screen2
  screen2 = Toplevel()
  screen2.configure(bg='orange')

  app_width = 500
  app_height = 500
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

  screen2.title("Login")
  Label(screen2, text = "Please enter details below to login", bg = "black", fg='white', width = "300", height = "2", font = ("Times New Roman", 13)).pack()
  Label(screen2, text = "", bg='orange').pack()

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username *", bg='light green').pack()
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.pack()
  Label(screen2, text = "", bg='orange').pack()
  Label(screen2, text = "Password *", bg='light green').pack()
  password_entry1 = Entry(screen2, textvariable = password_verify)
  password_entry1.pack()
  Label(screen2, text = "", bg='orange').pack()
  Button(screen2, text = "Login", bg='light green', width = 10, height = 1, command = login_verify).pack()
  Label(screen2, text = "", bg='orange').pack()
  Button(screen2, text = "Exit", bg='light green',height = "1", width = "10", command = delete7).pack()
  
def main_screen():
  global screen
  screen = Tk()
  screen.configure(bg='orange')
  
  app_width = 500
  app_height = 500
  
  screen_width = screen.winfo_screenwidth()
  screen_height = screen.winfo_screenheight()

  x = (screen_width / 2) - (app_width / 2)
  y = (screen_height / 2) - (app_height / 2)

  screen.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

  screen.title("Login/Register")
  Label(text = "Welcome to Trip Planner", bg = "black", fg='white', width = "300", height = "2", font = ("Times New Roman", 13)).pack()
  Label(text = "", bg='orange').pack()
  Button(text = "Login", bg='light green', height = "2", width = "30", command = login).pack()
  Label(text = "", bg='orange').pack()
  Button(text = "Register", bg='light green',height = "2", width = "30", command = register).pack()
  Label(text = "", bg='orange').pack()
  Button(text = "Exit", bg='light green', height = "2", width = "30", command = screen.quit).pack()

  screen.mainloop()

main_screen()

