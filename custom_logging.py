import logging

def setup_logging():
    """
    Настройка логирования для проекта.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Логи будут записываться в файл app.log
            logging.StreamHandler()          # Логи будут выводиться в консоль
        ]
    )