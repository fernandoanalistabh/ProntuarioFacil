from PySimpleGUI import PySimpleGUI as sg

# Layout teste commit
sg.theme('Reddit')
layout = [
    [sg.Text('Número do SUS'),sg.Input(key='numerodosus')],
    [sg.Text('OU')],
    [sg.Text('Nome do Paciente'),sg.Input(key='nomedopaciente')],
    [sg.Button('Localizar')]
]
# Janela
janela = sg.Window('Tela de Consulta', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Localizar':
        if valores['numerodosus'] == '54321' or valores['nomedopaciente'] == 'Joissi Fernandes':
            print('Aqui vermos as informaçõess do banco de dados!')