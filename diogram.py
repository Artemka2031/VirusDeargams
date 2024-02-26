from graphviz import Digraph


def create_virus_workflow_final_adjusted():
    dot = Digraph(comment='Финальная взаимодействие вируса с корректировкой')

    # Определение блоков
    dot.node('START', 'Запуск вирусного ПО')
    dot.node('RAM', 'Загрузка в ОЗУ')
    dot.node('CPU', 'CPU: Выполнение вируса')
    dot.node('ALU', 'АЛУ: Попытка загрузки')
    dot.node('PSW', 'PSW: Попытка изменения на режим ожидания')

    # Условные блоки (ромбы)
    dot.node('CHK_ALU', 'Проверка загрузки АЛУ', shape='diamond')
    dot.node('CHK_PSW', 'Проверка изменения PSW', shape='diamond')
    dot.node('PM', 'Изменение памяти программ', shape='diamond')
    dot.node('EM', 'Изменение памяти ошибок', shape='diamond')

    dot.node('LOOP', 'Возврат к началу программы')
    dot.node('HANG', 'Система зависает', shape='parallelogram')

    # Определение связей между блоками
    dot.edge('START', 'RAM', label='Запуск -> ОЗУ')
    dot.edge('RAM', 'CPU', label='ОЗУ -> CPU')
    dot.edge('CPU', 'ALU', label='CPU -> АЛУ')
    dot.edge('ALU', 'CHK_ALU', label='Проверка АЛУ')
    dot.edge('CHK_ALU', 'HANG', label='Успешно')
    dot.edge('CHK_ALU', 'PSW', label='Не успешно')
    dot.edge('PSW', 'CHK_PSW', label='Проверка PSW')
    dot.edge('CHK_PSW', 'PM', label='Не успешно')
    dot.edge('PM', 'EM', label='Не успешно')
    dot.edge('EM', 'LOOP', label='Не успешно')
    dot.edge('LOOP', 'START', label='Повтор')
    dot.edge('CHK_PSW', 'HANG', label='Успешно')
    dot.edge('PM', 'HANG', label='Успешно', constraint='false')
    dot.edge('EM', 'HANG', label='Успешно', constraint='false')

    # Указание пути сохранения файла (адаптируйте путь к вашей среде)
    output_path = 'Вирус резидентный'
    dot.render(output_path, format='png', view=True)


def create_non_resident_virus_workflow():
    dot = Digraph(comment='Взаимодействие нерезидентного вируса')

    # Определение блоков
    dot.node('TRIGGER', 'Триггер запуска', shape='ellipse')
    dot.node('START', 'Запуск вирусного ПО')
    dot.node('CHK_AV', 'Проверка наличия антивируса', shape='diamond')
    dot.node('REPEAT', 'Повтор', shape='parallelogram')
    dot.node('VIRUS_WORK', 'Работа вирусного ПО', shape='parallelogram')
    dot.node('END', 'Завершение работы вируса', shape='ellipse')

    # Определение связей между блоками
    dot.edge('TRIGGER', 'START', label='Активация')
    dot.edge('START', 'CHK_AV', label='Запуск')
    dot.edge('CHK_AV', 'REPEAT', label='Антивирус обнаруживает')
    dot.edge('REPEAT', 'START', label='Возврат к началу')
    dot.edge('CHK_AV', 'VIRUS_WORK', label='Антивирус не обнаруживает')
    dot.edge('VIRUS_WORK', 'END', label='Выполнено')

    # Указание пути сохранения файла
    output_path = 'Вирус нерезидентный'
    dot.render(output_path, format='png', view=True)


# Вызов функции для создания и сохранения блок-схемы
create_non_resident_virus_workflow()

# При вызове этой функции будет создана и сохранена блок-схема
create_virus_workflow_final_adjusted()
