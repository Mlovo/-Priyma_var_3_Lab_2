def solve_linguistics():
    students_data = {}
    
    number_of_students = 3

    print(f"--- Введення даних для {number_of_students} учнів ---")
    
    # 1. Збір даних
    for i in range(number_of_students):
        print(f"\nУчень №{i + 1}")
        name = input("Введіть ім'я учня: ").strip()
        
        # Перевірка на пусте ім'я
        while not name:
            print("Ім'я не може бути порожнім!")
            name = input("Введіть ім'я учня: ").strip()

        languages_input = input(f"Які мови знає {name}? (через пропуск): ")
        languages_set = set(languages_input.split())
        
        students_data[name] = languages_set

    # 2. Виведення мов для кожного учня
    print("\n" + "="*30)
    print("СПИСОК МОВ ПО УЧНЯХ:")
    print("="*30)
    
    for name, languages in students_data.items():
        # .join() об'єднує елементи множини в рядок для гарного виводу
        langs_str = ", ".join(languages) if languages else "Не знає іноземних мов"
        print(f"Учень: {name:10} | Мови: {langs_str}")

    # 3. Пошук учня (або учнів), що знає найбільше мов
    max_count = -1
    best_students = []

    for name, languages in students_data.items():
        count = len(languages)
        
        if count > max_count:
            max_count = count
            best_students = [name] # Новий лідер
        elif count == max_count:
            best_students.append(name) # Додаємо до лідерів (нічия)

    # 4. Виведення переможця
    print("\n" + "="*30)
    print("РЕЗУЛЬТАТ:")
    print("="*30)
    
    if max_count > 0:
        students_str = ", ".join(best_students)
        print(f"Найбільше мов ({max_count}) знає: {students_str}")
    else:
        print("Ніхто не знає жодної мови :(")

if __name__ == "__main__":
    solve_linguistics()
