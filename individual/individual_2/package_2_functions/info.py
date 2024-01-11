def info(stations, name_station):
    """
    Функция вывода информации о введенной станции, о поездах и их времени (если они есть).
    Функция ничего не возвращает.
    """
    count = 0
    for station in stations:
        if station.get('name') == name_station:
            count += 1
            print("Номер поезда пункта: ", station.get('train'),
                  "Время отправления: ", station.get('time'))

    # Если счетчик равен 0, то станции не найдены.
    if count == 0:
        print("Станции не найдены.")

    return None
