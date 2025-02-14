from data_loader import DataLoader
from data_processing import DataProcessor
from visualization import Visualizer
from reporting import Reporter
from custom_logging import setup_logging
from logging import getLogger

# Настройка логирования
setup_logging()

# Создаем логгер
logger = getLogger(__name__)

# Загрузка данных
loader = DataLoader()
loader.load_from_csv("season-2324.csv")

# Предобработка данных
processor = DataProcessor(loader.data)

# Подсчет пропущенных значений
missing_values = processor.count_missing()
logger.info(f"Пропущенные значения:\n{missing_values}")

# Заполнение пропущенных значений (только для числовых столбцов)
processor.fill_missing(strategy='mean')

# Удаление выбросов (пример для числового столбца)
processor.remove_outliers(column="FTHG", threshold=3)

# Отчет о пропущенных значениях
reporter = Reporter()
reporter.missing_values_report(missing_values)

# Визуализация
viz = Visualizer(processor.data)
viz.plot_histogram("FTHG", bins=20, color='skyblue')
viz.plot_correlation_matrix()