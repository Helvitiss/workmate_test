import pytest
from app.reports.median_coffee import MedianCoffeeReport
from app.reports.registry import REPORTS

def test_registry():
    assert REPORTS[MedianCoffeeReport.name] is MedianCoffeeReport


def test_median_coffee_report_basic(sample_records):
    report = MedianCoffeeReport()
    headers, rows = report.build(sample_records)

    assert headers == ["student", "median_coffee"]
    assert len(rows) == 2
    # Алексей Смирнов: [450, 500] -> 475.0
    # Дарья Петрова: [200] -> 200.0
    assert rows[0] == ["Алексей Смирнов", 475.0]
    assert rows[1] == ["Дарья Петрова", 200.0]

def test_median_coffee_report_outliers(sample_records):
    from app.models import StudyRecord
    from datetime import date

    sample_records.append(
        StudyRecord(
            student="Алексей Смирнов",
            date=date(2024, 6, 3),
            coffee_spent=9999999,
            sleep_hours=3.0,
            study_hours=16.0,
            mood="зомби",
            exam="Математика"
        )
    )

    # [450, 500, 9999999] -> медиана 500.0
    report = MedianCoffeeReport()
    _, rows = report.build(sample_records)

    alexey_row = next(r for r in rows if r[0] == "Алексей Смирнов")
    assert alexey_row[1] == 500
