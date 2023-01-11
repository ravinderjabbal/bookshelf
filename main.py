import pull_data
from flask import Flask, Response

app = Flask(__name__)


# noinspection PyRedundantParentheses
@app.route("/get_data", methods=["GET"])
def get_data():
    processed_data = pull_data.get_processed_data()
    data = pull_data.get_json_data()
    return (Response(response=data))


@app.route("/save_data", methods=["PUT"])
def save_data():
    pass


if __name__ == '__main__':
    app.run()
