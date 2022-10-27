import tkinter as tk
import tkinter.ttk as ttk
import pyvisa as visa

root = tk.Tk()
root.title('Tektronix PWS4721 GUI')
rm = visa.ResourceManager('/usr/lib64/libvisa.so')

window_height = 800
window_width = 800

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

def center_screen():
    global screen_height, screen_width, x_coordinate, y_coordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (window_width/2))
    y_coordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width,
                  window_height, x_coordinate, y_coordinate))


center_screen()

style = ttk.Style(root)
root.tk.call('source', 'themes/azure/azure.tcl')
style.theme_use('azure')

page1 = tk.Frame(root)
page2 = tk.Frame(root)

def show_frame(frame):
    frame.tkraise()

for frame in (page1, page2):
    frame.grid(row=0, column=0, sticky='nsew')


show_frame(page1)

def select_power_supply(*args):
    selected = combobox_power_supply.get()
    try:
        # power_supply = rm.open_resource(selected)
        print('click')
        page2.tkraise()
    except visa.VisaIOError:
        ttk.Label(frame1, text='Erro!' +
                  '\nNão foi possível conectar a fonte de tensão selecionada.',
                  foreground='red').place(x=45, y=200)
    return selected


def list_resources():
    return rm.list_resources()


# Frame select power supply
frame1 = ttk.LabelFrame(page1,
    text='Selecione sua fonte de alimentação',
    width=350, height=250)
frame1.place(x=25, y=20)
combobox_power_supply = ttk.Combobox(page1, state='readonly', values=[
    'teste', str(list_resources())], width=40)
combobox_power_supply.current(0)
combobox_power_supply.place(x=45, y=50)
button = ttk.Button(page1, text='Button',
                    command=lambda: select_power_supply(
                        combobox_power_supply))
button.bind('<Button-1>', select_power_supply)
button.place(x=45, y=100)

# Frame use power supply

frame2 = ttk.LabelFrame(
    page2, text='Frame2',
    width=500, height=500)
frame2.place(x=25, y=20)




root.mainloop()
