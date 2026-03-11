import csv
from datetime import date
from pathlib import Path
from typing import Sequence

from app.models import StudyRecord


class FileReader:
    """
    Класс для чтения файлов с базовой валидацией пути.
    Сделан отдельным классом, чтобы при необходимости можно было
    легко расширить функциональность.
    """

    def __init__(self, path: Path):
        self.path = path

    def _validate(self, extensions: Sequence[str] | None = None) -> None:
        if not self.path.exists():
            raise FileNotFoundError(f'Файл {self.path} не существует')

        if not self.path.is_file():
            raise ValueError("Путь не ведет к файлу")

        if extensions and self.path.suffix.lower() not in {ext.lower() for ext in extensions}:
            raise ValueError(f"Поддерживаются только: {', '.join(extensions)}")

    def read_csv(self) -> list[StudyRecord]:
        self._validate([".csv"])

        records: list[StudyRecord] = []

        with open(self.path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                records.append(
                    StudyRecord(
                        student=row["student"],
                        date=date.fromisoformat(row["date"]),
                        coffee_spent=int(row["coffee_spent"]),
                        sleep_hours=float(row["sleep_hours"]),
                        study_hours=float(row["study_hours"]),
                        mood=row["mood"],
                        exam=row["exam"],
                    )
                )
        return records
