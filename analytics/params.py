from dataclasses import dataclass


@dataclass
class AnalyticsParams:
    viewId: str
    startDate: str
    endDate: str
    outputFile: str
