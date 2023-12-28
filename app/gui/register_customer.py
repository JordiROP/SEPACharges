import PySimpleGUI as sg
from datetime import datetime
from back.model import Customer


class CustomerRegistrationWindow:
    def __init__(self):
        # LABELS
        self.label_name = sg.Text('Nombre')
        self.label_surname1 = sg.Text('Primer Apellido:')
        self.label_surname2 = sg.Text('Segundo Apellido:')
        self.label_dni = sg.Text('DNI:')
        self.label_birthdate = sg.Text('Fecha de Nacimiento:')
        self.label_phone = sg.Text('Teléfono:')
        self.label_mail = sg.Text('Email:')
        self.label_direction = sg.Text('Dirección:')
        self.label_cp = sg.Text('Código Postal:')
        self.label_city = sg.Text('Ciudad:')
        self.label_iban = sg.Text('IBAN:')
        self.label_register_date = sg.Text('Fecha de Alta:')
        self.label_register_cuota = sg.Text('Cuota:')
        self.label_active = sg.Text('Activo:')
        # INPUTS
        self.input_name = sg.Input(key="C_NOMBRE", size=(15, 1))
        self.input_surname1 = sg.Input(key="C_SURNAME1", size=(15, 1))
        self.input_surname2 = sg.Input(key="C_SURNAME2", size=(15, 1))
        self.input_dni = sg.Input(key="C_DNI", size=(13, 1))
        self.input_birthdate = sg.Input(key="C_BIRTH_DATE", size=(13, 1))
        self.input_birthdate_button = sg.CalendarButton(
            "Seleccionar Fecha", key='C_BIRTH_DATE_PICK', target='C_BIRTH_DATE',
            close_when_date_chosen=True, format='%d/%m/%Y', size=(10, 2))
        self.input_phone = sg.Input(key="C_PHONE", size=(13, 1))
        self.input_mail = sg.Input(key="C_MAIL", size=(13, 1))
        self.input_direction = sg.Input(key="C_DIRECTION", size=(20, 1))
        self.input_cp = sg.Input(key="C_CP", size=(10, 1))
        self.input_city = sg.Input(key="C_CITY", size=(10, 1))
        self.input_iban = sg.Input(key="C_IBAN", size=(20, 1))
        self.input_register_date = sg.Input(datetime.today().strftime('%d/%m/%Y'), key="C_REGISTER_DATE", size=(13, 1))
        self.input_register_button = sg.CalendarButton(
            "Seleccionar Fecha", key='C_REGISTER_DATE_PICK', target='C_REGISTER_DATE',
            close_when_date_chosen=True, format='%d/%m/%Y', size=(10, 2))
        self.input_register_cuota = sg.Input(key="C_CUOTA", size=(5, 1))
        self.input_active = sg.Checkbox('', key="C_ACTIVE", default=True)
        # BUTTONS
        self.button_save = sg.Button('Guardar', key="SAVE")

        self.layout = [[self.label_name, self.input_name, self.label_surname1, self.input_surname1,
                        self.label_surname2, self.input_surname2, self.label_dni, self.input_dni,
                        self.label_phone, self.input_phone],
                       [self.label_mail, self.input_mail, self.label_birthdate,
                        self.input_birthdate, self.input_birthdate_button, self.label_direction, self.input_direction,
                        self.label_city, self.input_city, self.label_cp, self.input_cp],
                       [self.label_iban, self.input_iban,
                        self.label_register_date, self.input_register_date, self.input_register_button,
                        self.label_register_cuota, self.input_register_cuota, self.label_active, self.input_active],
                       [self.button_save]]

    def show_window(self):
        register_window = sg.Window('Dar de Alta', self.layout)
        while True:
            event, values = register_window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "SAVE":
                dni = values['C_DNI']
                name = values['C_NOMBRE']
                surname1 = values['C_SURNAME1']
                surname2 = values['C_SURNAME2']
                birthdate = values['C_BIRTH_DATE']
                phone = values['C_PHONE']
                email = values['C_MAIL']
                direction = values['C_DIRECTION']
                pc = values['C_CP']
                city = values['C_CITY']
                iban = values['C_IBAN']
                register_date = values['C_REGISTER_DATE']
                quota = values['C_CUOTA']
                active = values['C_ACTIVE']

                customer = Customer(dni=dni, name=name, surname1=surname1, surname2=surname2, birthdate=birthdate,
                                    phone=phone, email=email, direction=direction, pc=pc, city=city, iban=iban,
                                    register_date=register_date, quota=quota, active=active)
        register_window.close()
