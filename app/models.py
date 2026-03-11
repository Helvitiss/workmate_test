from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class StudyRecord:
    student: str
    date: date
    coffee_spent: int
    sleep_hours: float
    study_hours: float
    mood: str
    exam: str