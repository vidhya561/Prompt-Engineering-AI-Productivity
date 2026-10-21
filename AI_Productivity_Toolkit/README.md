# AI Productivity Toolkit — Module 2

Beginner-friendly reusable prompt workflows for summarization, classification, generation, email drafting, resume improvement, research assistance, and coding/debugging.

## What this project demonstrates
- Zero-shot and few-shot prompting
- Role, context, task, instructions, and constraints
- Structured JSON output and validation
- AI-assisted coding/debugging and test cases
- Reusable productivity prompts
- A template for recording real model tests

**Important:** The Python code does not automatically call an AI model and does not require an API key. Copy prompts into an AI tool, paste the actual response into the notebook/report, and evaluate it honestly.

## Files
- `src/toolkit.py`: prompt builder, JSON validator, and scoring helper
- `prompts/prompt_templates.md`: reusable prompts
- `reports/evaluation_report_template.md`: record real test results
- `tests/test_toolkit.py`: basic tests
- `AI_Productivity_Toolkit_Colab.ipynb`: notebook for Google Colab

## Run locally
```bash
python src/toolkit.py
python -m unittest discover -s tests
```

## Test workflow
1. Test a zero-shot prompt.
2. Test an improved or few-shot prompt.
3. Use the same task and evaluation criteria when comparing models.
4. Check accuracy, relevance, completeness, clarity, instruction-following, and format.
5. Record actual prompts, responses, scores, and observations.

## Responsible use
Verify important claims and generated code. Do not enter passwords, private data, or confidential company information into an unapproved AI tool. Review AI-written resumes and emails for truthfulness.
