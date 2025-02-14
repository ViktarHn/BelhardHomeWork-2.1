import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from logging import getLogger

logger = getLogger(__name__)

class Visualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        plt.style.use('seaborn-v0_8')  # Используем актуальный стиль

    def plot_histogram(self, column: str, bins: int = 15, **kwargs) -> None:
        """Улучшенная гистограмма."""
        if column not in self.data.columns:
            logger.error(f"Столбец {column} не найден!")
            return
        
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], bins=bins, kde=True, **kwargs)
        plt.title(f"Распределение: {column}", fontsize=14)
        plt.xlabel(column, fontsize=12)
        plt.ylabel("Частота", fontsize=12)
        plt.show()

    def plot_correlation_matrix(self) -> None:
        """Матрица корреляций."""
        numeric_data = self.data.select_dtypes(include='number')
        if numeric_data.empty:
            logger.error("Нет числовых данных для построения матрицы корреляции.")
            return
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Корреляционная матрица", fontsize=14)
        plt.show()
    def plot_line(self, x: str, y: str, **kwargs) -> None:
        """Линейный график."""
        if x not in self.data.columns or y not in self.data.columns:
            logger.error(f"Столбцы {x} или {y} не найдены!")
        return
    
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.data, x=x, y=y, **kwargs)
        plt.title(f"Линейный график: {x} vs {y}", fontsize=14)
        plt.xlabel(x, fontsize=12)
        plt.ylabel(y, fontsize=12)
        plt.show()
    def plot_scatter(self, x: str, y: str, **kwargs) -> None:
        """Диаграмма рассеяния."""
        if x not in self.data.columns or y not in self.data.columns:
            logger.error(f"Столбцы {x} или {y} не найдены!")
        return
    
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.data, x=x, y=y, **kwargs)
        plt.title(f"Диаграмма рассеяния: {x} vs {y}", fontsize=14)
        plt.xlabel(x, fontsize=12)
        plt.ylabel(y, fontsize=12)
        plt.show()