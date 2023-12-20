import PySimpleGUI as sg


class DetailCustomerWindow:
    def __init__(self):
        self.input_name = sg.Input('Nombre', key="NOMBRE")
        self.input_surname1 = sg.Input('Primer Apellido', key="SURNAME1")
        self.input_surname2 = sg.Input('Segundo Apellido', key="SURNAME2")
        self.input_dni = sg.Input('DNI', key="DNI")
        self.input_birthdate = sg.Input('Fecha de Nacimiento', key="BIRTH_DATE")
        self.input_phone = sg.Input('Teléfono', key="PHONE")
        self.input_mail = sg.Input('Correo Electrónico', key="MAIL")
        self.input_direction = sg.Input('Dirección', key="DIRECTION")
        self.input_cp = sg.Input('Código Postal', key="CP")
        self.input_city = sg.Input('Ciudad', key="CITY")
        self.input_iban = sg.Input('IBAN', key="IBAN")
        self.input_register_date = sg.Input('Fecha Alta', key="REGISTER_DATE")
        self.input_register_drop = sg.Input('Fecha Baja', key="NOMBRE")
        self.input_active = sg.Input('Activo', key="ACTIVE")
        self.button_save = sg.Button('Guardar', key="SAVE")
        self.button_mod = sg.Button('Modificar', key="Modify")
        self.layout = [[self.input_name, self.input_surname1, self.input_surname2, self.input_dni],
                       [self.input_birthdate, self.input_phone, self.input_mail],
                       [self.input_direction, self.input_cp, self.input_city],
                       [self.input_iban, self.input_register_date, self.input_active],
                       [self.button_save, self.button_mod]]

    def show_window(self):
        register_window = sg.Window('Detalles Cliente', self.layout)
        while True:
            event, values = register_window.read()
            if event == sg.WIN_CLOSED:
                break
        register_window.close()
