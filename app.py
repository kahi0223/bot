from flask import Flask
from flask import request

from use_case import send_message
from use_case import hot_news
from models import Result
from models.result import ResultStatus

app = Flask(__name__)


@app.route("/", methods=["POST"])
def bot() -> tuple[dict[str, str], int]:
    """Bot endpoint.
    payload: {"message": "<text>"}
    """
    message = request.form.get("message", None)
    if message is None:
        return {"message": "No message"}, 400
    result: Result = send_message(message=message)
    if result.status == ResultStatus.OK:
        return result.payload, 200
    return result.payload, 500


@app.route("/news")
def hot_news() -> tuple[dict[str, str], int]:
    result: Result = hot_news()
    if result.status == ResultStatus.OK:
        return result.payload, 200
    return result.payload, 500
