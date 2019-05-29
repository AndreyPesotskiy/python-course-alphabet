import logging
import unittest
from testfixtures import LogCapture


def say_hello(user):
    logging.info(f"{user} saying hello")


class TestSayHello(unittest.TestCase):

    def test_say_hello(self):
        expected_message = "Denis saying hello"
        expected_level = "INFO"
        expected_message_number = 1

        with LogCapture() as logs:
            say_hello("Denis")

            self.assertEqual(len(logs.records), expected_message_number)
            # Some interesting way to do that
            # Equal to record = logs.records[0]
            [record] = logs.records
            self.assertEqual(record.levelname, expected_level)
            self.assertEqual(record.msg, expected_message)


if __name__ == "__main__":
    unittest.main()
