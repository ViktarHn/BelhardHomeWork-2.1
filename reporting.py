import pandas as pd  # Добавляем импорт pandas
from logging import getLogger

logger = getLogger(__name__)

class Reporter:
    @staticmethod
    def missing_values_report(missing_counts: pd.Series) -> None:
        """
        Отчет о пропущенных значениях.

        Параметры:
        - missing_counts: Серия с количеством пропущенных значений в каждом столбце.
        """
        logger.info("\n" + "="*40)
        logger.info("Отчет о пропущенных значениях:")
        logger.info("="*40)
        
        if missing_counts.sum() == 0:
            logger.info("Пропущенные значения отсутствуют.")
        else:
            for col, count in missing_counts.items():
                if count > 0:
                    logger.info(f"{col}: {count} пропусков ({count/len(missing_counts)*100:.2f}%)")