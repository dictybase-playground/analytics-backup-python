import pandas as pd
from analytics.cmd import parse_cmdline
from analytics.service import initialize_analyticsreporting
from analytics.fetch import get_report
from analytics.parse import parse_response
from analytics.csv import get_csv_headers
from analytics.csv import save_response
from analytics.params import AnalyticsParams


def main():
    args = parse_cmdline()
    params = AnalyticsParams(
        viewId=args.viewId,
        startDate=args.startDate,
        endDate=args.endDate,
        outputFile=args.outputFile
    )

    analytics = initialize_analyticsreporting()
    response = get_report(analytics, params)
    data = parse_response(response)
    headers = get_csv_headers(response)
    pageToken = response['reports'][0].get('nextPageToken')

    while pageToken != None:
        print(
            f"fetching next batch of results starting with page token {pageToken}")
        analytics = initialize_analyticsreporting()
        response = get_report(analytics, params, str(int(pageToken)))
        pageToken = response['reports'][0].get('nextPageToken')
        newData = parse_response(response)
        data = pd.concat([data, newData], ignore_index=True)

    print("finished fetching results")
    save_response(data, headers, params.outputFile)
    print(f"successfully saved report to {params.outputFile}")


if __name__ == '__main__':
    main()
