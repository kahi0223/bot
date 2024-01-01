from flask import Flask

from main import main
from models import Result
from models.result import ResultStatus

app = Flask(__name__)


@app.route("/news")
def hot_news() -> tuple[dict[str, str], int]:
    result: Result = main()
    if result.status == ResultStatus.OK:
        return result.payload, 200
    return result.payload, 500
