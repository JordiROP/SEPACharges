import PySimpleGUI as sg

from back.queries import get_all_customers


class CustomersTable:
    def __init__(self):
        data = get_all_customers()
        self.columns = data.columns.values.tolist()
        self.values = data.values.tolist()

    def create_window(self):
        return sg.Table(values=self.values, headings=self.columns,
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='center', key='-TABLE-',
                        selected_row_colors='red on yellow',
                        enable_events=True,
                        expand_x=True,
                        expand_y=True,
                        enable_click_events=True)
