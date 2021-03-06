from datetime import timedelta
import roster_calendar_api
import roster_parser


def main():
    roster = roster_parser.roster_to_json("roster.txt")
    date = roster["date"]

    event_count = 0
    print(roster["times"])

    for day in roster["times"]:

        if day == ['']:
            continue

        for time in day:
            roster_calendar_api.create_event(date, time, roster["titles"][event_count])
            event_count += 1
        date += timedelta(days=1)

    print(f"Created {event_count} events in your calendar.")


if __name__ == '__main__':
    main()
