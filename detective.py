# detective.py
import pandas as pd
import random

_previous_sum = None
_case_number = 0
_table_names = {}

def det_sum(table, column):
    """
    Детектив данных представляет...
    Parameters:
    table (pd.DataFrame): таблица с уликами
    column (str): столбец для наблюдения
    """
    import pandas as pd
    import random
    
    global _previous_sum, _case_number, _table_names
    _case_number += 1

    # Проверяем существование столбца
    if column not in table.columns:
        print(f"\n🔍 Сводка №{_case_number}: Андрюха! Пропал столбец '{column}'! Возможен криминал! По коням!")
        return

    # Считаем текущую сумму
    current_sum = table[column].sum()
    
    # Функция для зашифровки чисел
    def format_number(num):
        abs_num = abs(num)
        if abs_num >= 1_000_000_000:
            return f"{num/1_000_000_000:.1f} млрд"
        elif abs_num >= 1_000_000:
            return f"{num/1_000_000:.1f} млн"
        elif abs_num >= 1_000:
            return f"{num/1_000:.1f} тыс"
        else:
            return f"{num:.1f}"
    
    # Форматируем текущую сумму
    formatted_current = format_number(current_sum)
    
    # Получаем уникальный идентификатор таблицы (по id в памяти)
    table_id = id(table)
    
    # Если для этой таблицы еще нет кодового имени - создаем новое
    if table_id not in _table_names:
        animals = ["Антилопа", "Бобр", "Барсук", "Волк", "Выдра", "Гепард", "Горилла", "Дикобраз", "Дельфин",
                   "Енот", "Жираф", "Зебра", "Заяц", "Игуана", "Йеменский хамелеон", "Кот", "Кенгуру",
                   "Лев", "Лама", "Медведь", "Морж", "Носорог", "Олень", "Панда", "Пума",
                   "Рысь", "Слон", "Сурикат", "Тигр", "Тюлень", "Утконос", "Фламинго", "Хомяк",
                   "Цапля", "Черепаха", "Шимпанзе", "Щука", "Эму", "Юрок", "Як"]
        
        _table_names[table_id] = random.choice(animals)
    
    # Получаем кодовое имя для этой таблицы
    table_animal = _table_names[table_id]
    
    # Серия принтов
    print(f"\n🕵️ Сводка АН №{_case_number}: Наблюдение за объектом '{table_animal}' по столбцу '{column}'")
    print("=" * 50)
    
    # Если это первое появление таблицы
    if _previous_sum is None:
        print(f"🔎 Объект '{table_animal}' был принят под наблюдение! Сумма: {formatted_current}")
        print("📋 Фиксируем в сводке...")
    else:
        # Выводим текущую сумму
        print(f"💼 Текущая сумма: {formatted_current}")
        
        # Вычисляем разницу
        difference = current_sum - _previous_sum
        
        if difference != 0:
            # Форматируем разницу
            formatted_diff = f"{abs(difference):,.0f}".replace(',', ' ')
            
            if difference > 0:
                print(f"⬆️ Хм... Сумма выросла на {formatted_diff}")
                print("🕵️ Похоже, мы пропустили новые связи! Отправляем экипаж для проверки!")
            else:
                print(f"⬇️ Ого! Сумма уменьшилась на {formatted_diff}")
                print("🔍 Кто-то пытается замести следы! Нужна проверка по камерам!")
        else:
            print("🤔 Сумма не изменилась...")
            print("📝 Заносим в сводку: Объект не выходил, встреч не зафиксировано")
    
    print("=" * 50)
    # Сохраняем сумму
    _previous_sum = current_sum