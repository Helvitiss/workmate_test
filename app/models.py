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

    @classmethod
    def from_dict(cls, data: dict) -> "StudyRecord":
        return cls(
            student=data["student"],
            date=date.fromisoformat(data["date"]),
            coffee_spent=int(data["coffee_spent"]),
            sleep_hours=float(data["sleep_hours"]),
            study_hours=float(data["study_hours"]),
            mood=data["mood"],
            exam=data["exam"],
        )