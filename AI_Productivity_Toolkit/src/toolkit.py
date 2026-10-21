"""Reusable helpers for the AI Productivity Toolkit.
This code does not call an external AI model.
"""
import json
from typing import Any, Dict, List


def build_prompt(role: str, context: str, task: str,
                 constraints: List[str], output_format: str) -> str:
    """Build a structured prompt."""
    constraint_text = "\\n".join(f"- {item}" for item in constraints) or "- None specified"
    return (
        f"Role: {role}\\nContext: {context}\\nTask: {task}\\n"
        f"Constraints:\\n{constraint_text}\\nOutput format: {output_format}"
    )


def parse_json_response(response_text: str) -> Dict[str, Any]:
    """Parse a JSON object copied from a model."""
    try:
        result = json.loads(response_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Response is not valid JSON: {exc}") from exc
    if not isinstance(result, dict):
        raise ValueError("Expected a JSON object.")
    return result


def score_response(scores: Dict[str, int]) -> float:
    """Average integer scores from 1 through 5."""
    if not scores:
        raise ValueError("Provide at least one score.")
    for criterion, score in scores.items():
        if not isinstance(score, int) or not 1 <= score <= 5:
            raise ValueError(f"{criterion}: score must be an integer from 1 to 5.")
    return round(sum(scores.values()) / len(scores), 2)


if __name__ == "__main__":
    print(build_prompt(
        "Beginner-friendly Python tutor",
        "The learner is new to programming",
        "Explain Python lists",
        ["Use simple English", "Include one short example"],
        "Definition, code, explanation"
    ))
    sample = '{"task_name":"Prompt testing","skills":["zero-shot"],"deliverables":["Colab notebook"]}'
    print("\\nParsed JSON:", json.dumps(parse_json_response(sample), indent=2))
    print("Example score (replace with real evaluation):",
          score_response({"accuracy": 4, "clarity": 5}))
