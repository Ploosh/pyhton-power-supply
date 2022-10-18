import tkinter as tk
import tkinter.ttk as ttk 
import pyvisa as visa

# from backend.list_resources import list_resources

root = tk.Tk()

root.geometry('900x700')
root.title('Tektronix PWS4721 GUI')
style = ttk.Style(root)
root.tk.call('source', 'themes/azure/azure.tcl')
style.theme_use('azure')

rm = visa.ResourceManager()


def select_power_supply(selection):
  rm.open_resource(selection)


def list_resources():
  return rm.list_resources('?*')


choices = list_resources()


options = tk.StringVar()
menu = tk.OptionMenu(root, options, str(choices))
menu.pack()
options.set('Selecione a fonte de alimentação')


root.mainloop()
