from datetime import timedelta
import roster_calendar_api
import roster_parser


def main():
    roster = roster_parser.roster_to_json("roster.txt")
    date = roster["date"]

    eventCount = 0

    for day in roster["times"]:
        for time in day:
            roster_calendar_api.createEvent(date, time, roster["titles"][eventCount])
            eventCount += 1
        date += timedelta(days=1)

    print(f"Created {eventCount} events in your calendar.")


if __name__ == '__main__':
    main()
