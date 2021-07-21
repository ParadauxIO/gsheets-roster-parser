from datetime import datetime


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

        # Get just the timeperiod
        t = s[:-1]
        if "Daily" in s:
            t = t[t.find("Daily") + 6:]

        if "Weekly" in s:
            t = t[t.find("Weekly") + 7:]

        if "Thunkable" in s:
            t = t[t.find("Thunkable") + 10:]

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