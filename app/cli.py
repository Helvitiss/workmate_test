import argparse
from pathlib import Path

from tabulate import tabulate

from app.models import StudyRecord
from app.reports.registry import REPORTS
from app.reader import FileReader


def build_parser(report_registry: list[str]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Генерация отчетов по данным студентов")
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV-файлам с данными",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=report_registry,
        help="Название отчёта",
    )
    return parser



def run():
    parser = build_parser(list(REPORTS.keys()))
    args = parser.parse_args()

    records: list[StudyRecord] = []
    for file in args.files:
        path = Path(file)
        try:
            records.extend(FileReader(path).read_csv())
        except (FileNotFoundError, ValueError) as exc:
            parser.exit(status=1, message=f"{exc}\n")


    report = REPORTS[args.report]()
    headers, rows = report.build(records)
    print(tabulate(rows, headers=headers, tablefmt="grid"))

    return 0