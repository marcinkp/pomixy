import unittest
import json
from src.controller import Controller


class ControllerTest(unittest.TestCase):

  def test_order(self):
    # given
    id = ""
    controller = Controller("order")

    # when
    response = controller.get(id)
    body = json.loads(response["body"])

    # then
    self.assertEqual(response["statusCode"], 200)


if __name__ == '__main__':
  unittest.main()
