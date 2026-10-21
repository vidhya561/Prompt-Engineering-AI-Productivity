# Reusable Prompt Templates — Module 2

Replace square-bracket placeholders before using each prompt.

## 1. Zero-shot summarization
```text
Summarize the following text in five bullet points using simple English.
Keep the key facts and do not add information that is not in the source.
Text:
[PASTE TEXT]
```

## 2. Few-shot classification
```text
Classify each message as Bug Report, Feature Request, or General Question.

Example:
Message: "The app crashes when I click Save."
Label: Bug Report

Example:
Message: "Please add dark mode."
Label: Feature Request

Example:
Message: "Where can I update my profile?"
Label: General Question

Now classify this message:
"[PASTE MESSAGE]"
Return only the label and one short reason.
```

## 3. Role + context + constraints
```text
Role: You are a beginner-friendly technical writing assistant.
Context: I am a college student preparing a professional internship update.
Task: Rewrite my notes into a LinkedIn post.
Constraints: 120–160 words, truthful, professional, no invented achievements.
Output: Short paragraphs and 3–6 relevant hashtags.
Notes:
[PASTE YOUR NOTES]
```

## 4. Structured JSON output
```text
Extract task details from the text below.
Return ONLY valid JSON with exactly these keys:
{
  "task_name": "string",
  "skills": ["string"],
  "deliverables": ["string"],
  "next_steps": ["string"]
}
If something is not stated, use an empty string or list. Do not invent details.
Text:
[PASTE TASK DESCRIPTION]
```

## 5. Summarization
```text
Summarize the source for a beginner.
Output:
- Main idea (one sentence)
- Key points (five bullets)
- Important terms (up to five with simple definitions)
- What the source does not tell us, if anything
Use only the source content.
Source:
[PASTE SOURCE]
```

## 6. Email drafting
```text
Role: Professional email-writing assistant.
Write a polite email to [RECIPIENT] about [PURPOSE].
Context: [BACKGROUND]
Include a subject, greeting, concise request, thanks, and sign-off.
Constraints: 100–140 words; do not invent dates or facts.
Return the subject and body separately.
```

## 7. Resume improvement
```text
Act as a resume editor for an entry-level candidate.
Improve these resume bullets for clarity and relevance.
Do not invent skills, metrics, projects, or experience.
Preserve the original meaning and use concise action verbs.
Return a table with Original, Revised, and Information to Verify.
Resume bullets:
[PASTE BULLETS]
```

## 8. Coding and debugging
```text
Role: Patient Python programming tutor.
Task: Explain and improve the code below.
Please:
1. Explain what it should do.
2. Identify errors or weaknesses.
3. Give corrected code.
4. Explain changes line by line.
5. Give three test cases, including an edge case.
Do not claim the code was executed unless it was actually run.
Code:
[PASTE CODE]
Error message:
[PASTE ERROR]
```

## 9. Research assistance
```text
Help me research [TOPIC].
Separate established facts, claims needing verification, open questions, and reliable source types.
Do not invent citations, URLs, statistics, or publication details.
If sources are not verified, say so clearly.
```

## 10. Prompt improvement
```text
Evaluate this prompt without answering its original task yet.
Identify ambiguity, missing context, conflicting instructions, and unclear output format.
Then provide problems found, an improved prompt, and an evaluation checklist.
Prompt:
[PASTE PROMPT]
```
