import os
import pandas as pd
from analyzer import SalesAnalyzer
from algorithms import bubble_sort, linear_search  # твои алгоритмы
import numpy as np
import timeit

# Пути к файлам и папкам
RAW_DATA = "data/sales_data.csv"
CLEAN_DATA = "data/sales_clean.csv"
FIGURES_DIR = "figures"
OUTPUT_DIR = "output"

# Создаём папки, если их нет
os.makedirs(FIGURES_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Инициализация анализатора и загрузка данных
analyzer = SalesAnalyzer(RAW_DATA)
df = analyzer.load_data()
df_clean = analyzer.clean_data()
analyzer.export_clean_data(CLEAN_DATA)
print(f"Data cleaned and saved to {CLEAN_DATA}")

# -------------------------------
# Основные метрики
# -------------------------------
total_rev = analyzer.total_revenue()
avg_order = analyzer.average_order_value()
cust_count = analyzer.customer_count()
repeat_rate = analyzer.repeat_customer_rate()
cancel_rate = analyzer.cancellation_rate()

print("\n Key Metrics:")
print(f"Total revenue: ${total_rev:.2f}")
print(f"Average order value: ${avg_order:.2f}")
print(f"Number of customers: {cust_count}")
print(f"Repeat customer rate: {repeat_rate:.2f}%")
print(f"Cancellation rate: {cancel_rate:.2f}%\n")

# Топ-10 клиентов
top_customers = analyzer.top_customers()
print("Top 10 customers by order amount:")
print(top_customers)

# Средний чек по категориям
avg_by_cat = analyzer.average_order_by_category()
print("\nAverage order value by product category:")
print(avg_by_cat)

# -------------------------------
# Сохраняем отчёты в output/
# -------------------------------
top_customers.to_csv(os.path.join(OUTPUT_DIR, "top_customers.csv"))
avg_by_cat.to_csv(os.path.join(OUTPUT_DIR, "average_order_by_category.csv"))

# Создаём текстовый отчёт
summary_file = os.path.join(OUTPUT_DIR, "summary_report.txt")
with open(summary_file, "w", encoding="utf-8") as f:
    f.write("Key Metrics:\n")
    f.write(f"Total revenue: ${total_rev:.2f}\n")
    f.write(f"Average order value: ${avg_order:.2f}\n")
    f.write(f"Number of customers: {cust_count}\n")
    f.write(f"Repeat customer rate: {repeat_rate:.2f}%\n")
    f.write(f"Cancellation rate: {cancel_rate:.2f}%\n\n")

    f.write("Top 10 customers by order amount:\n")
    f.write(str(top_customers) + "\n\n")

    f.write("Average order value by product category:\n")
    f.write(str(avg_by_cat) + "\n")

# -------------------------------
# Визуализация
# -------------------------------
analyzer.plot_revenue_by_category(save_path=os.path.join(FIGURES_DIR, "revenue_by_category.png"))
analyzer.plot_monthly_revenue(save_path=os.path.join(FIGURES_DIR, "monthly_revenue_trend.png"))
analyzer.plot_order_distribution(save_path=os.path.join(FIGURES_DIR, "order_value_distribution.png"))
print(f"Charts saved to {FIGURES_DIR}/")

# -------------------------------
# Сравнение скорости сортировки и поиска
# -------------------------------
order_amounts = df_clean['order_amount'].tolist()
order_array = np.array(order_amounts)
target_value = order_amounts[0]

# Сортировка
t_custom_sort = timeit.timeit(lambda: bubble_sort(order_amounts.copy()), number=1)
t_builtin_sort = timeit.timeit(lambda: sorted(order_amounts.copy()), number=1)
t_numpy_sort = timeit.timeit(lambda: np.sort(order_array.copy()), number=1)

# Поиск
t_custom_search = timeit.timeit(lambda: linear_search(order_amounts, target_value), number=1000)
t_builtin_search = timeit.timeit(lambda: target_value in order_amounts, number=1000)

print("\n Sorting performance:")
print(f"Custom bubble sort: {t_custom_sort:.6f} sec")
print(f"Python built-in sorted(): {t_builtin_sort:.6f} sec")
print(f"NumPy sort: {t_numpy_sort:.6f} sec")

print("\n Search performance (1000 runs):")
print(f"Custom linear search: {t_custom_search:.6f} sec")
print(f"Python 'in': {t_builtin_search:.6f} sec")

# -------------------------------
# Добавляем результаты в summary_report.txt
# -------------------------------
with open(summary_file, "a", encoding="utf-8") as f:
    f.write("\n Sorting performance (seconds):\n")
    f.write(f"Custom bubble sort: {t_custom_sort:.6f}\n")
    f.write(f"Python built-in sorted(): {t_builtin_sort:.6f}\n")
    f.write(f"NumPy sort: {t_numpy_sort:.6f}\n")

    f.write("\n Search performance (seconds, 1000 runs):\n")
    f.write(f"Custom linear search: {t_custom_search:.6f}\n")
    f.write(f"Python 'in': {t_builtin_search:.6f}\n")
