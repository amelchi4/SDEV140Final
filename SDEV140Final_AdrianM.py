"""
Author:Adrian Melchi
Assignment: SDEV140 Final Project
Description: The purpose of this assignment is to create a GUI application
Program Name: User Log In Simulation
"""
from customtkinter import * #Importing customtkinter for improved customization

class main_setup: # Class creating for modularization
    def __init__(self): #Running the init manually
        self.login_window()
    def login_window(self): # Module creating the login window
        set_appearance_mode("dark") # Using CTk, making the windows "dark" mode 
        self.loginWindow = CTk() # Initializing the window
        self.loginWindow.geometry("600x800") # Fixed window size
        self.loginWindow.resizable(height = "false", width = "false") # Fixing window size to be static
        self.loginWindow.title("User Log In Page") # Titling loginWindow page
        self.lbl_greeting = CTkLabel(master = self.loginWindow, text="Welcome!", font = ("Helvetica", 25)) #Greeting label for window
        self.lbl_user = CTkLabel(master = self.loginWindow, text="Username:", font = ("Helvetica", 25))#Username label marking which box is for input
        self.ent_user = CTkEntry(master = self.loginWindow, border_color = "#7c1c1c") # Entry box for username
        self.lbl_pass = CTkLabel(master = self.loginWindow, text="Password:", font = ("Helvetica", 25))# Password label for password entry box
        self.ent_pass = CTkEntry(master = self.loginWindow, border_color = "#7c1c1c")# Password entry box for user input 
        self.btn_login = CTkButton(master = self.loginWindow, text = "Login", command = self.user_signIn, fg_color = "#7c1c1c", font = ("Helvetica", 15)) #Creating button for user log in
        self.btn_forgot = CTkButton(master = self.loginWindow, text="Forgot Username/Password", command = self.user_forgot, fg_color = "#7c1c1c", font = ("Helvetica", 15)) # Button if user "forgets" username or password
        self.btn_exit = CTkButton(master = self.loginWindow, text="Exit", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.exitWindows) # Exit button to close out the program

        self.widget_grid() # running the grid placements

    def user_signIn(self): #Module for the main window. 'Meat' of the program
        username = self.ent_user.get() #Getting user input from the Username entry box
        password = self.ent_pass.get() #Getting user input from the Password entry box
        userInfo = {"SDEV140": "Python140", "IvyTech": "ITCC2024", "RandomJohn": "109813"} #Dictionary for usernames and passwords. Key = Username, Value = Password
        if username in userInfo and userInfo[username] == password: #If loop to check for correct/incorrect user and pass
            self.successWindow = CTkToplevel() #New window for successful login
            self.successWindow.resizable(height = "false", width = "false")#Fixing window size to static
            self.successWindow.title("Successful Sign On") #Titling window
            self.successWindow.geometry("600x800") #Fixing window dimensions
            lbl_success = CTkLabel(master = self.successWindow, text = "Congratulations, you've made it.", font = ("Helvetica", 25)) # Label for window content
            btn_return = CTkButton(master = self.successWindow, text="Return to Login", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.returnLogin) #Return button for back to log in screen
            btn_exit=CTkButton(master = self.successWindow, text="Exit", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.exitWindows) #Exit button for closing program entirely
            #Packing Label and Buttons
            lbl_success.pack()
            btn_return.pack()
            btn_exit.pack()
            self.successWindow.mainloop() #Running the window if successful
        else:
            self.failureWindow = CTkToplevel() # New window for failed login
            self.failureWindow.resizable(height = "false", width = "false") #Fixing window size to static
            self.failureWindow.title("Failed Sign-On") # Titling new failure window
            self.failureWindow.geometry("600x800") # Fixing window size
            lbl_failure = CTkLabel(master = self.failureWindow, text= "Invalid Username or Password", font = ("Helvetica", 25)) # Label for window content
            btn_exit=CTkButton(master = self.failureWindow, text="Exit", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.exitWindows) # Button for exiting program entirely
            btn_return = CTkButton(master = self.failureWindow, text="Return to Login", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.returnLogin) # Button for returning to log in 
            #Packing label and buttons for use on screen
            btn_return.pack()
            btn_exit.pack()
            lbl_failure.pack()
            self.failureWindow.mainloop() # Running the window if log in failed
    
    def returnLogin(self): #Function for returning back to log in screen
        #Closes all windows but the main window log in
        self.forgotWindow.destroy()
        self.successWindow.destroy()
        self.failureWindow.destroy()

    def exitWindows(self): #Function for exiting program entirely
        #Closes all windows, exiting the program completely
        self.loginWindow.destroy()
        self.forgotWindow.destroy()
        self.successWindow.destroy()
        self.failureWindow.destroy()

    def user_forgot(self): #Function for when the user forgets a username/password
        self.forgotWindow = CTkToplevel() #New window if user clicks forgot button
        self.forgotWindow.resizable(height = "false", width = "false") #Fixing window to be static
        self.forgotWindow.title("Forgot Username/Password") #Titling the window
        self.forgotWindow.geometry("600x800")#Fixing window size
        lbl_forgot = CTkLabel(master = self.forgotWindow, text = "Please refer to user manual for list of usernames and passwords.", font = ("Helvetica", 15)) # Label directing user to manual if username or password has been forgotten
        btn_return = CTkButton(master = self.forgotWindow, text="Return to Login", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.returnLogin)#Button for returning to log in screen
        btn_exit=CTkButton(master = self.forgotWindow, text="Exit", fg_color = "#7c1c1c", font = ("Helvetica", 15), command=self.exitWindows)#Button for exiting program entirely
        #Packing label and buttons for window
        btn_exit.pack()
        btn_return.pack()
        lbl_forgot.pack()
        self.forgotWindow.mainloop()#Runs the new window if user has forgotten


    def widget_grid(self): #Function for grid placement of login window widgets
        self.lbl_greeting.grid(row=0, column=0, columnspan=2, sticky="W")
        self.lbl_user.grid(row=1, column=0, sticky="W")
        self.ent_user.grid(row=1, column=1, sticky="W")
        self.lbl_pass.grid(row=2, column=0, sticky="W",pady=5)
        self.ent_pass.grid(row=2, column=1, sticky="W", pady=5)
        self.btn_login.grid(row=3, column=0,sticky="W", pady=5) 
        self.btn_forgot.grid(row=4, column=0, sticky="W",pady=5)  
        self.btn_exit.grid(row=5, column=0, sticky="W",pady=5)



#Creating a class call
x=main_setup()
#Calling class and running the program.
x.loginWindow.mainloop()
