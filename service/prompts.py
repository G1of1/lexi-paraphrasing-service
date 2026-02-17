def standard_prompt(text: str):
    prompt = f'''You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT add new facts or information.

Task:
Rewrite the following text while preserving the original meaning, intent, and tone.
Improve clarity and flow where possible without changing the message.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}
'''
    return prompt

def simplify_prompt(text: str):
    prompt=f'''
You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT add new facts or information.

Task:
Rewrite the following text using simpler language.
Reduce sentence complexity and avoid jargon where possible.
Preserve accuracy and original meaning.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}

'''
    return prompt

def shorten_prompt(text: str):
    prompt=f'''
You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT remove essential information.

Task:
Rewrite the following text in a more concise form.
Remove redundancy while keeping all key information.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}

'''
    return prompt

def expand_prompt(text: str):
    prompt=f'''You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT add new facts or assumptions.

Task:
Rewrite the following text by expanding it with clearer explanations and smoother transitions.
Elaborate only on what is already implied in the text.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}
'''
    return prompt

def academic_prompt(text: str):
    prompt=f'''You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT add new facts or citations.

Task:
Rewrite the following text in an academic tone.
Use formal structure, precise language, and an objective voice.
Preserve the original meaning.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}
'''
    return prompt

def formal_prompt(text: str):
    prompt=f'''You are an expert paraphrasing assistant.

IMPORTANT:
- You must return ONLY valid JSON.
- Do NOT include markdown, code blocks, or explanations.
- Do NOT add new facts or information.

Task:
Rewrite the following text in a formal and professional tone.
Improve clarity and polish while preserving meaning.

Output format:
```json
  "paraphrased_text": "string"


Text:
{text}
'''
    return prompt
