import tkinter

window = tkinter.Tk()
window.title("My first GUI project")
window.minsize(width = 500 , height = 300)
window.config(padx=100,pady=200)

my_label = tkinter.Label(text = "Miles to KM converter",font = ("Arial",14,"italic"))
#my_label.grid(column = 0, row = 0)

miles = tkinter.Label(text = "Miles", font = ("Times New Roman",10,"bold"))
miles.grid(column = 3,row = 0)

#is equla to label
equal = tkinter.Label(text = "is equal to", font = ("Times New Roman",10,"bold"))
equal.grid(column = 1, row = 1)

#ans
ans = tkinter.Label(text = "ans",font = ("Times New Roman",10,"bold"))
ans.grid(column = 2, row = 1)

# in KM
km = tkinter.Label(text = "in KM",font = ("Times New Roman",10,"bold"))
km.grid(column = 3, row = 1)
def button_clicked():
    new_text = int(input.get()) * 1.609
    ans.config(text = new_text)




my_button = tkinter.Button(text = "Calculate",command = button_clicked)
my_button.grid(column = 2, row = 2)

input = tkinter.Entry(highlightbackground = "red")
input.grid(column = 2, row = 0)















window.mainloop()