import PySimpleGUI as sg

from back.queries import get_customer_by_dni
from gui.constants import WINDOW_EVENT_VALUE, VALUE_ROW, POS_DNI
from gui.detail_customer import DetailCustomerWindow
from gui.register_customer import CustomerRegistrationWindow
from gui.table import CustomersTable

sg.theme('DefaultNoMoreNagging')  # Add a touch of color


class MainScreen:
    def __init__(self):
        self.button_register = sg.Button('Dar Alta', key="REGISTER")
        self.button_sepa = sg.Button('Exportar SEPA', key="SEPA_EXPORT")
        self.button_back_up = sg.Button('Exportar CSV', key="CSV_EXPORT")
        self.button_load_db = sg.Button('Importar CSV', key="IMPORT")
        self.data_table = CustomersTable()
        self.layout = [[self.button_register, self.button_sepa, self.button_back_up, self.button_load_db],
                       [self.data_table.create_window()]]

    def show_window(self):
        window = sg.Window('SEPA Management', self.layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            if '+CLICKED+' in event:
                row = event[WINDOW_EVENT_VALUE][VALUE_ROW]
                print(row)
                if row is not None:
                    dni = self.data_table.values[row][POS_DNI]
                    customer = get_customer_by_dni(dni)
                    if customer:
                        dcw = DetailCustomerWindow(customer)
                        dcw.show_window()

            if event == 'REGISTER':
                crw = CustomerRegistrationWindow()
                crw.show_window()

            if event == 'DETAIL_UNLOCK':
                print("done")
        window.close()
