import tkinter

MILES_TO_KM_CONVERSION = 1.609


def convert():
    converted = int(input_box.get()) * MILES_TO_KM_CONVERSION
    conversion_label["text"] = format(converted, '.2f')


window = tkinter.Tk()

window.title("Miles to Km Converter")
window.minsize(width=290, height=120)
window.config(padx=20, pady=20)

input_box = tkinter.Entry(width=20, justify="right")
input_box.grid(column=1, row=0)
input_box.focus()


miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=5, pady=5)

conversion_label = tkinter.Label(text=0)
conversion_label.grid(column=1, row=1)
conversion_label.config(padx=5, pady=5)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)
conversion_label.config(padx=5, pady=5)

window.mainloop()
