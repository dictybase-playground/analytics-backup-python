from analytics.cmd import parse_cmdline
from analytics.service import initialize_analyticsreporting
from analytics.fetch import get_report
from analytics.csv import save_response
from analytics.params import AnalyticsParams


def main():
    args = parse_cmdline()
    params = AnalyticsParams(
        viewId=args.viewId,
        startDate=args.startDate,
        endDate=args.endDate
    )

    analytics = initialize_analyticsreporting()
    response = get_report(analytics, params)
    save_response(response)


if __name__ == '__main__':
    main()
