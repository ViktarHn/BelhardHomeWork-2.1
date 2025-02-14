import pandas as pd
import requests
from logging import getLogger  # Импортируем getLogger из стандартного модуля logging

logger = getLogger(__name__)

class DataLoader:
    def __init__(self):
        self.data = None

    def load_from_csv(self, file_path: str) -> None:
        """Загрузка данных из CSV."""
        try:
            self.data = pd.read_csv(file_path)
            logger.info(f"Данные загружены из CSV: {file_path}")
        except Exception as e:
            logger.error(f"Ошибка загрузки CSV: {e}")
            raise
    def load_from_json(self, file_path: str) -> None:
        """Загрузка данных из JSON."""
        try:
            self.data = pd.read_json(file_path)
            logger.info(f"Данные загружены из JSON: {file_path}")
        except Exception as e:
            logger.error(f"Ошибка загрузки JSON: {e}")
            raise

    def load_from_api(self, url: str) -> None:
        """Загрузка данных через API."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            self.data = pd.DataFrame(response.json())
            logger.info(f"Данные загружены из API: {url}")
        except Exception as e:
            logger.error(f"Ошибка загрузки данных через API: {e}")
        raise