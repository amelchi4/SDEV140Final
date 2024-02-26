import tkinter as tk

windowOne = tk.Tk()
windowOne.title("Weather Forecast")
frame = tk.Frame(bg="black")
frame.pack()
greeting = tk.Label(master=frame, text="Welcome to this very adept weather forecasting application. Enjoy!", background = "black", foreground="white")
greeting.pack()

user_city = tk.Entry()
city_search = tk.Button(text="Find your city's weather")
city_search.pack()
user_city.pack()

userCity = user_city.get()



























windowOne.mainloop()