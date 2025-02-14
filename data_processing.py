import pandas as pd
from logging import getLogger

logger = getLogger(__name__)

class DataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def count_missing(self) -> pd.Series:
        """Подсчет пропущенных значений."""
        return self.data.isna().sum()

    def fill_missing(self, strategy='mean', columns=None) -> None:
        """
        Заполнение пропущенных значений.

        Параметры:
        - strategy: Стратегия заполнения ('mean', 'median', 'mode' или конкретное значение).
        - columns: Список столбцов для обработки (по умолчанию все числовые столбцы).
        """
        if columns is None:
            # Выбираем только числовые столбцы
            columns = self.data.select_dtypes(include='number').columns

        for col in columns:
            if strategy == 'mean':
                fill_value = self.data[col].mean()
            elif strategy == 'median':
                fill_value = self.data[col].median()
            elif strategy == 'mode':
                fill_value = self.data[col].mode()[0]
            else:
                fill_value = strategy  # Конкретное значение

            self.data[col].fillna(fill_value, inplace=True)
            logger.info(f"Пропуски в столбце '{col}' заполнены с использованием стратегии '{strategy}'.")

    def remove_outliers(self, column: str, threshold: float = 3) -> None:
        """
        Удаление выбросов с использованием метода Z-оценки.

        Параметры:
        - column: Столбец для обработки.
        - threshold: Пороговое значение Z-оценки (по умолчанию 3).
        """
        if column not in self.data.columns:
            logger.error(f"Столбец '{column}' не найден!")
            return

        # Вычисляем Z-оценки
        z_scores = (self.data[column] - self.data[column].mean()) / self.data[column].std()
        
        # Удаляем выбросы
        self.data = self.data[abs(z_scores) <= threshold]
        logger.info(f"Выбросы в столбце '{column}' удалены с порогом Z-оценки {threshold}.")