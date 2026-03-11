from datetime import date
import pytest
from app.models import StudyRecord

def test_study_record_from_dict(sample_row):
    record = StudyRecord.from_dict(sample_row)
    
    assert record.student == "Алексей Смирнов"
    assert record.date == date(2024, 6, 1)
    assert record.coffee_spent == 450
    assert record.sleep_hours == 4.5
    assert record.study_hours == 12.0
    assert record.mood == "норм"
    assert record.exam == "Математика"

def test_study_record_invalid_types(sample_row):
    invalid_row = sample_row.copy()
    invalid_row["coffee_spent"] = "not an int"
    
    with pytest.raises(ValueError):
        StudyRecord.from_dict(invalid_row)

def test_study_record_invalid_date(sample_row):
    invalid_row = sample_row.copy()
    invalid_row["date"] = "2024-13-45"
    
    with pytest.raises(ValueError):
        StudyRecord.from_dict(invalid_row)
