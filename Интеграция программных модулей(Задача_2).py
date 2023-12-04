def main():
    # Замените этот блок кода на ваш способ ввода данных
    N = int(input("Введите количество городов: "))
    M = int(input("Введите количество автобусных маршрутов: "))

    passengers = []  # Список для хранения количества пассажиров по каждому маршруту в каждом городе

    # Получаем информацию о пассажирах для каждого маршрута в каждом городе
    for i in range(N):
        city_passengers = []
        print(f"Для города {i + 1}:")
        for j in range(M):
            passengers_count = int(input(f"Введите количество пассажиров для маршрута {j + 1}: "))
            city_passengers.append(passengers_count)
        passengers.append(city_passengers)

    # Находим маршрут с наибольшим и наименьшим количеством пассажиров для каждого города
    for i, city in enumerate(passengers):
        max_passengers_route = city.index(max(city)) + 1
        min_passengers_route = city.index(min(city)) + 1
        print(f"Для города {i + 1}:")
        print(f"Маршрут с наибольшим количеством пассажиров: {max_passengers_route}")
        print(f"Маршрут с наименьшим количеством пассажиров: {min_passengers_route}")


if __name__ == "__main__":
    main()
