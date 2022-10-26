import tkinter as tk
import tkinter.ttk as ttk
import pyvisa as visa

root = tk.Tk()
root.title('Tektronix PWS4721 GUI')
rm = visa.ResourceManager('/usr/lib64/libvisa.so')

window_height = 300
window_width = 400


def center_screen():
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width,
                  window_height, x_cordinate, y_cordinate))


center_screen()

style = ttk.Style(root)
root.tk.call('source', 'themes/azure/azure.tcl')
style.theme_use('azure')


def select_power_supply(*args):
    selected = combobox_power_supply.get()
    try:
        power_supply = rm.open_resource(selected)
        print(power_supply)
    except visa.VisaIOError:
        ttk.Label(root, text='Erro!' +
                  '\nNão foi possível conectar a fonte de tensão selecionada.',
                  foreground='red').place(x=45, y=200)
    return selected


def list_resources():
    return rm.list_resources()


frame1 = ttk.LabelFrame(
    root, text='Selecione sua fonte de alimentação',
    width=350, height=250)
frame1.place(x=25, y=20)
combobox_power_supply = ttk.Combobox(root, state='readonly', values=[
    'teste', str(list_resources())], width=40)
print(rm.list_resources())
combobox_power_supply.current(0)
combobox_power_supply.place(x=45, y=50)
button = ttk.Button(root, text='Button',
                    command=lambda: select_power_supply(
                        combobox_power_supply))
button.bind('<Button-1>', select_power_supply)
button.place(x=45, y=100)
root.mainloop()
