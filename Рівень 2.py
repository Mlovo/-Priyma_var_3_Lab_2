import math

def solve():
    print("Введіть цілі числа через пропуск (має утворитися квадратна матриця):")
    raw_input = input("> ")

    # 1. Валідація введення чисел
    try:
        if not raw_input.strip():
            print("Помилка: Ви нічого не ввели.")
            return
        numbers = [int(x) for x in raw_input.split()]
    except ValueError:
        print("Помилка: Введені дані містять нечислові символи.")
        return

    # 2. Валідація розмірності (чи можна створити квадратну матрицю n*n)
    count = len(numbers)
    n = int(math.isqrt(count))

    if n * n != count:
        print(f"Помилка: Введено {count} чисел. Це число не є повним квадратом, "
              f"тому неможливо створити квадратну матрицю [n][n].")
        return

    # 3. Трансформація у двовимірний список
    matrix = []
    for i in range(n):
        start_index = i * n
        end_index = start_index + n
        row = numbers[start_index:end_index]
        matrix.append(row)

    # Вивід отриманої матриці для наочності
    print(f"\nСформована матриця {n}x{n}:")
    for row in matrix:
        print(row)

    # 4. Перевірка на симетричність відносно головної діагоналі
    # Матриця симетрична, якщо matrix[i][j] == matrix[j][i]
    is_symmetric = True
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                is_symmetric = False
                break
        if not is_symmetric:
            break

    # 5. Результат
    print("\nРезультат перевірки:")
    if is_symmetric:
        print("Матриця симетрична відносно головної діагоналі.")
    else:
        print("Матриця НЕ симетрична.")

if __name__ == "__main__":
    solve()
