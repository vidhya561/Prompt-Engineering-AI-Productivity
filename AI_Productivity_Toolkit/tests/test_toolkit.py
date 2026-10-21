import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from toolkit import build_prompt, parse_json_response, score_response


class ToolkitTests(unittest.TestCase):
    def test_build_prompt(self):
        prompt = build_prompt("Tutor", "Beginner", "Explain lists",
                              ["Use simple English"], "Bullets")
        self.assertIn("Role: Tutor", prompt)
        self.assertIn("Task: Explain lists", prompt)

    def test_parse_json(self):
        self.assertEqual(parse_json_response('{"status":"ok"}')["status"], "ok")

    def test_invalid_json(self):
        with self.assertRaises(ValueError):
            parse_json_response("{bad json}")

    def test_score_average(self):
        self.assertEqual(score_response({"accuracy": 4, "clarity": 5}), 4.5)


if __name__ == "__main__":
    unittest.main()
