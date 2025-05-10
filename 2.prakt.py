# Импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv("C:/Users/Pavel/Desktop/2.Praktiskais darbs/dermatology_database_1.csv")

# Обработка признака 'age'
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # заменяем '?' на NaN и преобразуем к числу

# Проверка пропущенных значений
print("Пропущенные значения:\n", df.isnull().sum())

# Краткая информация
print("\nРазмерность данных:", df.shape)
print("\nУникальные классы:\n", df['class'].value_counts())

# Описательная статистика
print("\nСтатистика по числовым признакам:\n", df.describe())

# Гистограмма по возрасту
plt.hist(df['age'].dropna(), bins=20, color='orange')
plt.title('Распределение возраста')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.grid(True)
plt.savefig("vecuma_histogramma.png")  # <<<<<< SAGLABĀ
plt.show()

# Матрица корреляции
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(numeric_only=True), cmap='coolwarm', annot=False)
plt.title("Корреляционная матрица между признаками")
plt.savefig("korelacijas_matrica.png")  # <<<<<< SAGLABĀ
plt.show()

# Izkliedes diagramma: age vs erythema (piemērs)
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="age", y="erythema", hue="class", palette="Set2")
plt.title("Vecums pret ādas apsārtumu (erythema) pa klasēm")
plt.savefig("scatter_age_erythema.png")  # <<<<<< SAGLABĀ
plt.show()
