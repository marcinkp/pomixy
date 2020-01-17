import json


class Controller:
  def __init__(self, table):
    self.table = table

  def add(self, body):
    try:
      return _to_response(200, body)
    except:
      return general_error_handling()

  def get(self, id):
    try:
      record = {"id": id, "table": self.table}
      return _to_response(200, record)
    except:
      return general_error_handling()


def general_error_handling():
  return _to_response(500, _build_error_body("Unexpected error"))


def _to_response(status_code, body):
  return {
    "statusCode": status_code,
    "body": json.dumps(body)
  }


def _build_error_body(message):
  return {
    "message": message
  }
