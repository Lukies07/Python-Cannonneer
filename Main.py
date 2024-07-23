import tkinter as tk

root = tk.Tk()

# Get the screen width and height of the user
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width) + 'x' + str(screen_height)) #sets the window = the user's sxreen width/height
root.title("Cannonneer") #name of window

#Main menu title
label = tk.Label(root, text="Hello, world!", font=("Helvetica", 24))
label.place(relx=0.5, rely=0.5, anchor='center')

# Run the main loop
root.mainloop()

