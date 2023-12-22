import PySimpleGUI as sg

from .table import CustomersTable
from .register_customer import CustomerRegistrationWindow
from .detail_customer import DetailCustomerWindow

sg.theme('DefaultNoMoreNagging')  # Add a touch of color

class MainScreen:
    def __init__(self):
        self.button_register = sg.Button('Dar Alta', key="REGISTER")
        self.button_sepa = sg.Button('Exportar SEPA', key="SEPA_EXPORT")
        self.button_back_up = sg.Button('Exportar CSV', key="CSV_EXPORT")
        self.button_load_db = sg.Button('Importar CSV', key="IMPORT")
        self.layout = [[self.button_register, self.button_sepa, self.button_back_up, self.button_load_db],
                       [CustomersTable().create_window()]]

    def show_window(self):
        window = sg.Window('SEPA Management', self.layout)
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
