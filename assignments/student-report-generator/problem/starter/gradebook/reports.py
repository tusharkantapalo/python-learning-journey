"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students
from .stats import average_per_student, subjects_offered, top_scorer, passing_students
from .data import RECORDS


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    
    report = ""

    report += f"Total number of records: {len(records)}\n"
    report += f"Subjects offered: {sorted(subjects_offered(records))}\n"
    report += f"Average scores: {average_per_student(records)}\n"
    report += f"Top scorer: {top_scorer(records)}\n"
    report += f"Passing students: {passing_students(records)}\n"

    return report
