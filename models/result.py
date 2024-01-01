from dataclasses import dataclass


class ResultStatus:
    OK = "OK"
    ERROR = "ERROR"


@dataclass
class Result:
    status: ResultStatus
    payload: dict = None
