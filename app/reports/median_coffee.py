from __future__ import annotations

from collections import defaultdict
from statistics import median

from app.models import StudyRecord
from app.reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def build(self, records: list[StudyRecord]) -> tuple[list[str], list[list[str | int]]]:
        spend_by_student: dict[str, list[int]] = defaultdict(list)


        for record in records:
            spend_by_student[record.student].append(record.coffee_spent)


        rows = [
            [student, float(median(spendings))]
            for student, spendings in spend_by_student.items()
        ]
        rows.sort(key=lambda item: item[1], reverse=True)

        return ["student", "median_coffee"], rows