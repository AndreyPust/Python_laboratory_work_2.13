def get_station(stations):
    """
    Функция запроса данных о станции.
    """
    name = input("Название пункта: ")
    # Создать словарь.
    station = {'name': name}
    print("Добавить поезд? n/y")
    cucle = input()
    if cucle == 'n':
        station['train'] = 'Поездов нет'
        station['time'] = ' '
    else:
        train = input("Номер поезда: ")
        dep_time = input("Время отправления поезда: ")
        # Добавить в словарь поезд и время.
        station['train'] = train
        station['time'] = dep_time

    # Добавить словарь в список.
    stations.append(station)

    # Отсортировать список в случае необходимости по времени поезда.
    if len(stations) > 1:
        stations.sort(key=lambda item: item.get('time', ''))

    return stations
