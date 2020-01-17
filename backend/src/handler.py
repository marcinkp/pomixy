import json
from src.controller import Controller


def get(event, context):
  controller = Controller(event["pathParameters"]["table"])
  return controller.get(event["pathParameters"]["id"])


def add(event, context):
  controller = Controller(event["pathParameters"]["table"])
  return controller.add(json.loads(event["body"]))

