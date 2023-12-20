import PySimpleGUI as sg

from table import tbl1
from register_customer import CustomerRegistrationWindow
from detail_customer import DetailCustomerWindow
sg.theme('DefaultNoMoreNagging')  # Add a touch of color
# All the stuff inside your window.
button_register = sg.Button('Dar Alta', key="REGISTER")
button_sepa = sg.Button('Exportar SEPA', key="SEPA_EXPORT")
button_back_up = sg.Button('Exportar CSV', key="CSV_EXPORT")
button_load_db = sg.Button('Importar CSV', key="IMPORT")

layout = [[button_register, button_sepa, button_back_up, button_load_db],
          [tbl1]]

window = sg.Window('App', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif '+CLICKED+' in event:
        dcw = DetailCustomerWindow()
        dcw.show_window()
    elif 'REGISTER' in event:
        crw = CustomerRegistrationWindow()
        crw.show_window()
window.close()
