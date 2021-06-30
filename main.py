import cfg
import pandas as pd
from analytics.cmd import parse_cmdline
from analytics.service import initialize_analyticsreporting
from analytics.fetch import get_report
from analytics.parse import parse_response
from analytics.csv import get_csv_headers
from analytics.csv import save_response
from analytics.params import AnalyticsParams
from upload.params import MinioParams
from upload.client import upload_report


def save_analytics(args, viewId):
    """Queries the Analytics Reporting API V4 and saves to CSV.

    Args:
      args: Object with parsed arguments.
      viewId: str
    Returns:
      CSV filename: str
    """
    params = AnalyticsParams(
        viewId=viewId,
        startDate=args.startDate,
        endDate=args.endDate,
        dimensions=args.dimensions,
        metrics=args.metrics
    )

    cfg.logger.info(f"fetching google analytics data for view id {viewId}")
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

    cfg.logger.info(f"finished retrieving {len(data.index)} results")
    csv = save_response(data, headers, params.viewId)
    cfg.logger.info(f"successfully saved report to {csv}")
    return csv


def main():
    args = parse_cmdline()

    views = args.viewIds.split(",")
    for id in views:
        csv = save_analytics(args, id)
        # upload result to minio
        minioParams = MinioParams(
            endpoint=args.endpoint,
            accessKey=args.accessKey,
            secretKey=args.secretKey,
            bucket=args.bucket,
            filename=csv
        )
        upload_report(minioParams)


if __name__ == '__main__':
    main()
