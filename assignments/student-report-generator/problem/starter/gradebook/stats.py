"""gradebook.stats — aggregate statistics over grade records."""

from .data import RECORDS


def average_per_student(RECORDS: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement

    total_list = {}
    count = {}
    avg_dict = {}

    for i in RECORDS:
        name = i['name']
        if name in total_list:
            total_list[name] += i['score']
            count[name] += 1
        else:
            total_list[name] = i['score']
            count[name] = 1

    for name in total_list:
        avg_dict[name] = round(total_list[name] / count[name], 2)

    return avg_dict


def subjects_offered(RECORDS: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    unq_sub = set()
    for i in RECORDS:
        unq_sub.add(i['subject'])

    return unq_sub


def top_scorer(RECORDS: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement

    avg_list = average_per_student(RECORDS)

    highest = 0
    for name in avg_list:
        if avg_list[name] > highest:
            highest = avg_list[name]
            name1 = name

    top = (name1, highest)

    return top


def passing_students(RECORDS: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement

    avg_list = average_per_student(RECORDS)

    passed =[]
    for name in avg_list:
        if avg_list[name] >= threshold:
            passed.append(name)
    
    passed.sort()

    return passed
