import pandas as pd  # Импорт библиотеки

path = 'resources/visits.csv'  # Путь к файлу
df = pd.read_csv(path, sep=';')  # Чтение файла в DF
# Выводим первые 20 строк файла
print(df.head(n=20))

# Выводим информацию по DF
print(df.info())

df.columns = df.columns.str.lower()  # Приведение названий солбцов к нижнему регистру

# В результате вывода df.info() было выявлено несоответствие типов значений в столбцах session_start, session_end.
# Выполняем преобразования:
df['session_start'] = pd.to_datetime(df['session_start'])
df['session_end'] = pd.to_datetime(df['session_end'])

print(df.dtypes)

print(df['region'].unique())  # В результате был получен массив: ['United States' 'USA' nan]
df = df.dropna()  # Удаляем строки, где пропущено хотя бы одно значение, то есть имеется значение nan(None)
print(df['region'].unique())  # В результате был получен массив: ['United States' 'USA']

# Задали корректное значение, на которое будем заменять
name = 'United States'
# Список дубликатов
duplicates = ['USA']
# Исключаем дубликаты
df['region'] = df['region'].replace(duplicates, name)

print(df['device'].unique())  # В результате был получен массив ['iPhone' 'Mac' 'Android' 'PC' 'MAC' 'IPHONE']
df['device'] = df['device'].str.lower()  # Чтобы исключить дубли приводим все значения к нижнему регистру

print('Количество дублей в файле', df.duplicated().sum())
# При проверке через print(df.duplicated().sum()) были выявлены дубликаты, поэтому ниже мы их удаляем
df = df.drop_duplicates()  # Удаление дубликатов из DF
df = df.reset_index()  # Обновление индексации

# Группировка по столбцам device и channel и подсчет уникальных значений в столбце user_id
print(df.groupby(['device', 'channel'])['user_id'].count())

# Группировка - device и количество рекламных источников каждого типа (channel). Создать датафрейм.
# Переименовать столбец с количеством в «сount». Отсортировать по убыванию столбца «count»
print(df.groupby(['device', 'channel'])['user_id'].count().sort_values(ascending=False).reset_index(name='count'))

# Сводная таблица (pivot_table) - уникальное количество пользователей для каждого устройства (device).
# Отсортировать по убыванию количества.
print(df.pivot_table(index=['device'], values='user_id', aggfunc=lambda x: len(x.unique()), sort=False)
      .rename(columns={"user_id": "count"}))

# Сводная таблица (pivot_table) - количество пользователей для каждого устройства (device) - строки и канала - столбцы.
# Отсортировать по возрастанию столбца device.
print(df.pivot_table(index=['device'], columns=['channel'], values='user_id', aggfunc=lambda x: len(x.unique()))
      .sort_values("device", ascending=True))
