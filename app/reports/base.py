from abc import ABC, abstractmethod

from app.models import StudyRecord


class BaseReport(ABC):
    """
    Базовый класс для репортов, чтобы они имели одинаковый скелет
    """

    name: str

    @abstractmethod
    def build(self, records: list[StudyRecord]) -> tuple[list[str], list[list[object]]]:
        """
        Формирует данные отчёта.
        Возвращает заголовки таблицы и строки данных.
        """

