from tkinter import * 

window = Tk()

window.title("test") 

window.geometry("600x450+70+120")

entry = Entry(
    window,

    width = 20,
    font = (

        "arial",

        20,

        "bold"
    )
    
)

entry.grid(row = 3, column = 2)

text = Label(
    window,

    text = " enter age: ",
    font = (

        "arial",

        20,

        "bold"
    )

) 
text.grid(row = 2, column = 2)

def print_age():

    text = Label(
        window,

        text = f"your age is: {entry.get()}",
    
        font = (

            "arial",

            20,

            "bold"
        )

    ) 
    text.grid(row = 4, column = 2)


My_button = Button(
    window, 
    text = "print_age", 
    width = 15,
    command = print_age,
    font = (

        "arial",

        20,

        "bold"


          
    )
  
)
My_button.grid(row = 3, column = 3)


window.mainloop()