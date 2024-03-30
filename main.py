import pandas as pd  # Импорт библиотеки

path = 'resources/visits.csv'  # Путь к файлу

df = pd.read_csv(path, sep=';')  # Чтение файла в DF
df.columns = df.columns.str.lower()  # Приведение названий солбцов к нижнему регистру
# При проверке через print(df.duplicated().sum()) были выявлены дубликаты, поэтому ниже мы их удаляем
df = df.drop_duplicates()  # Удаление дубликатов из DF

df = df.dropna() # Удаляем строки, где пропущено хотя бы одно значение, то есть имеется значение nan(None)
print(df['region'].unique())  # В результате был получен массив: ['United States' 'USA']

# Задали корректное значение, на которое будем заменять
name = 'United States'
# Список дубликатов
duplicates = ['USA']
# Исключаем дубликаты
df['region'] = df['region'].replace(duplicates, name)

print(df['device'].unique())  # В результате был получен массив ['iPhone' 'Mac' 'Android' 'PC' 'MAC' 'IPHONE']
df['device'] = df['device'].str.lower()  # Чтобы исключить дубли приводим все значения к нижнему регистру

df = df.reset_index()  # Обновление индексации

# Группировка по столбцам device и channel и подсчет уникальных значений в столбце user_id
print(df.groupby(['device', 'channel'])['user_id'].count())





