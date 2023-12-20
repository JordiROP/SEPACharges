import os

import PySimpleGUI as sg
import pandas as pd
import os

data = pd.read_csv(os.path.abspath(os.path.join(os.getcwd(), 'app', 'assets', 'ejemplos.csv')))
columns = data.columns.values.tolist()
values = data.values.tolist()

tbl1 = sg.Table(values=values, headings=columns,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='center', key='-TABLE-',
                selected_row_colors='red on yellow',
                enable_events=True,
                expand_x=True,
                expand_y=True,
                enable_click_events=True)
