import PySimpleGUI as sg


class DetailCustomerWindow:
    def __init__(self, customer):
        self.customer = customer
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
        self.label_register_drop = sg.Text('Fecha de Baja:')
        self.label_register_cuota = sg.Text('Cuota:')
        self.label_active = sg.Text('Activo:')
        # INPUTS
        self.input_name = sg.Input(customer['nombre'], key="NOMBRE", disabled=True)
        self.input_surname1 = sg.Input(customer['apellido1'], key="SURNAME1", disabled=True)
        self.input_surname2 = sg.Input(customer['apellido2'], key="SURNAME2", disabled=True)
        self.input_dni = sg.Input(customer['dni'], key="DNI", disabled=True)
        self.input_birthdate = sg.Input(customer['fecha_nacimiento'], key="BIRTH_DATE", disabled=True)
        self.input_phone = sg.Input(customer['telefono'], key="PHONE", disabled=True)
        self.input_mail = sg.Input(customer['email'], key="MAIL", disabled=True)
        self.input_direction = sg.Input(customer['direccion'], key="DIRECTION", disabled=True)
        self.input_cp = sg.Input(customer['CP'], key="CP", disabled=True)
        self.input_city = sg.Input(customer['ciudad'], key="CITY", disabled=True)
        self.input_iban = sg.Input(customer['IBAN'], key="IBAN", disabled=True)
        self.input_register_date = sg.Input(customer['alta'], key="REGISTER_DATE", disabled=True)
        self.input_register_drop = sg.Input(customer['baja'], key="DROP_DATE", disabled=True)
        self.input_register_cuota = sg.Input(customer['cuota'], key="CUOTA", disabled=True)
        self.input_active = sg.Input(customer['activo'], key="ACTIVE", disabled=True)
        # BUTTONS
        self.button_save = sg.Button('Guardar', key="SAVE")
        self.button_mod = sg.Button('Modificar', key="MODIFY")
        self.button_del = sg.Button('Borrar', key="DELETE")
        self.layout = [[self.label_name, self.input_name, self.label_surname1, self.input_surname1,
                        self.label_surname2, self.input_surname2],
                       [self.label_dni, self.input_dni, self.label_birthdate, self.input_birthdate,
                        self.label_phone, self.input_phone],
                       [self.label_mail, self.input_mail, self.label_direction, self.input_direction,
                        self.label_cp, self.input_cp],
                       [self.label_city, self.input_city, self.label_iban, self.input_iban,
                        self.label_register_date, self.input_register_date],
                       [self.label_register_drop, self.input_register_drop,
                        self.label_register_cuota, self.input_register_cuota, self.label_active, self.input_active],
                       [self.button_save, self.button_mod, self.button_del]]

    @classmethod
    def unlock_layout(cls, register_window):
        register_window['NOMBRE'].update(disabled=False)
        register_window['SURNAME1'].update(disabled=False)
        register_window['SURNAME2'].update(disabled=False)
        register_window['DNI'].update(disabled=False)
        register_window['BIRTH_DATE'].update(disabled=False)
        register_window['PHONE'].update(disabled=False)
        register_window['MAIL'].update(disabled=False)
        register_window['DIRECTION'].update(disabled=False)
        register_window['CP'].update(disabled=False)
        register_window['CITY'].update(disabled=False)
        register_window['IBAN'].update(disabled=False)
        register_window['REGISTER_DATE'].update(disabled=False)
        register_window['DROP_DATE'].update(disabled=False)
        register_window['CUOTA'].update(disabled=False)
        register_window['ACTIVE'].update(disabled=False)

    @classmethod
    def lock_layout(cls, register_window):
        register_window['NOMBRE'].update(disabled=True)
        register_window['SURNAME1'].update(disabled=True)
        register_window['SURNAME2'].update(disabled=True)
        register_window['DNI'].update(disabled=True)
        register_window['BIRTH_DATE'].update(disabled=True)
        register_window['PHONE'].update(disabled=True)
        register_window['MAIL'].update(disabled=True)
        register_window['DIRECTION'].update(disabled=True)
        register_window['CP'].update(disabled=True)
        register_window['CITY'].update(disabled=True)
        register_window['IBAN'].update(disabled=True)
        register_window['REGISTER_DATE'].update(disabled=True)
        register_window['DROP_DATE'].update(disabled=True)
        register_window['CUOTA'].update(disabled=True)
        register_window['ACTIVE'].update(disabled=True)

    def show_window(self):
        register_window = sg.Window('Detalles Cliente', self.layout)
        while True:
            event, values = register_window.read()
            if event == sg.WIN_CLOSED:
                break
            if "MODIFY" in event:
                self.unlock_layout(register_window)
        register_window.close()
