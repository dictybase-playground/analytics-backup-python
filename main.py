from analytics.service import initialize_analyticsreporting
from analytics.fetch import get_report
from analytics.csv import save_response


def main():
    analytics = initialize_analyticsreporting()
    response = get_report(analytics)
    save_response(response)


if __name__ == '__main__':
    main()
