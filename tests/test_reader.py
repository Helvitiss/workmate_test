import pytest
from pathlib import Path
from app.reader import FileReader

def test_file_reader_validation_non_existent():
    reader = FileReader(Path("non_existent.csv"))
    with pytest.raises(FileNotFoundError, match="не существует"):
        reader.read_csv()

def test_file_reader_validation_wrong_extension(tmp_path):
    wrong_file = tmp_path / "test.txt"
    wrong_file.write_text("content")
    
    reader = FileReader(wrong_file)
    with pytest.raises(ValueError, match="Поддерживаются только: .csv"):
        reader.read_csv()

def test_file_reader_read_csv(tmp_path, sample_row):
    csv_file = tmp_path / "test.csv"
    header = ",".join(sample_row.keys())
    values = ",".join(sample_row.values())
    csv_file.write_text(f"{header}\n{values}", encoding="utf-8")
    
    reader = FileReader(csv_file)
    records = reader.read_csv()
    
    assert len(records) == 1
    assert records[0].student == sample_row["student"]
