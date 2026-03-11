import pytest
from datetime import date
from app.models import StudyRecord



@pytest.fixture
def sample_row():
    return {
        "student": "Алексей Смирнов",
        "date": "2024-06-01",
        "coffee_spent": "450",
        "sleep_hours": "4.5",
        "study_hours": "12",
        "mood": "норм",
        "exam": "Математика"
    }

@pytest.fixture
def sample_records():
    return [
        StudyRecord(
            student="Алексей Смирнов",
            date=date(2024, 6, 1),
            coffee_spent=450,
            sleep_hours=4.5,
            study_hours=12.0,
            mood="норм",
            exam="Математика"
        ),
        StudyRecord(
            student="Алексей Смирнов",
            date=date(2024, 6, 2),
            coffee_spent=500,
            sleep_hours=4.0,
            study_hours=14.0,
            mood="устал",
            exam="Математика"
        ),
        StudyRecord(
            student="Дарья Петрова",
            date=date(2024, 6, 1),
            coffee_spent=200,
            sleep_hours=7.0,
            study_hours=6.0,
            mood="отл",
            exam="Математика"
        )
    ]
