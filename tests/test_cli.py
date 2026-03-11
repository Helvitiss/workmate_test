import sys

from app.cli import run


def test_cli_success(tmp_path, monkeypatch, capsys):
    file = tmp_path / "data.csv"
    file.write_text(
        "student,date,coffee_spent,sleep_hours,study_hours,mood,exam\n"
        "Alex,2024-01-01,3,7,5,happy,math\n"
    )

    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "--files", str(file), "--report", "median-coffee"],
    )

    run()

    captured = capsys.readouterr()
    assert "median" in captured.out.lower()