import PySimpleGUI as sg
from model.generator import generate_image

# Определение макета GUI
layout = [
    [sg.Text("Введите prompt:"), sg.InputText(key='prompt')],
    [sg.Text("Введите negative prompt:"), sg.InputText(key='negative_prompt')],
    [sg.Button('Сгенерировать изображение'), sg.Button('Выход')],
    [sg.Image(key='image')]
]

# Создание окна
window = sg.Window('Генератор изображений Stable Diffusion', layout)

# Обработка событий в окне
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    if event == 'Сгенерировать изображение':
        # Генерация изображения
        image_path = generate_image(values['prompt'], values['negative_prompt'])
        window['image'].update(filename=image_path)

window.close()
