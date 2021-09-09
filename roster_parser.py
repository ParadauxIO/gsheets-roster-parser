from datetime import datetime

removeables = ["(A)", "(Firstweek)"]
class_types = ["Daily", "Weekly", "Thunkable", "J2", "J", "F2", "F", "PC", "LCCS", "Senior"]


def roster_to_json(roster_location):
    f = open(roster_location, "r")
    lines = f.readlines()

    times = []
    temp = []
    titles = []
    date = lines[0][:-1]
    lines.pop(0)

    for s in lines:
        original = s
        if s.startswith("#"):
            continue

        for removeable in removeables:
            if removeable in s:
                s = s.replace(removeable, "")

        if s == "\n":
            continue

        # Get just the timeperiod
        t = s[:-1]
        # Summer 2021

        for class_type in class_types:
            if class_type in s:
                t = t[t.find(class_type) + len(class_type) + 1:]
                break

        original = original.replace(t, "") \
            .replace("\n", "") \
            .replace("\"", "").strip()
        titles.append(original)

        t = t.replace("\"", "").replace("\n", "")

        temp.append(t)
        if s.endswith("\"\n"):
            times.append(temp)
            temp = []
    times.append(temp)

    return {
        "date": datetime.strptime(date, "%d-%m-%Y"),
        "times": times,
        "titles": titles
    }