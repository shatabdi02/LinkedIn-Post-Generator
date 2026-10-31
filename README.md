# LinkedIn Post Generator

An AI-powered LinkedIn Post Generator built using Python, LangChain, and Groq LLMs. It generates LinkedIn posts based on a selected topic, language, and length while using few-shot prompting to produce content inspired by example posts.

## Features

- **AI-Powered Generation:** Uses Groq-hosted LLMs through LangChain.
- **Post Metadata Extraction:** Extracts line count, language, and relevant tags from existing LinkedIn posts.
- **Tag Unification:** Groups similar tags into standardized categories.
- **Few-Shot Learning:** Uses existing LinkedIn posts as examples to guide the writing style.
- **Customizable Generation:** Generates posts based on topic, language, and desired length.

## Tech Stack

- Python
- LangChain
- Groq API
- Pandas
- JSON
- python-dotenv

## Project Structure

```text
linkedin-post-generator/
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
├── llm_helper.py
├── preprocess.py
├── few_shot.py
├── post_generator.py
├── requirements.txt
├── .env
└── README.md
```

## Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd linkedin-post-generator
```

### 2. Create a virtual environment

```bash
python -m venv myenv
```

Activate it on Windows:

```bash
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/keys).

## Usage

### Step 1: Preprocess LinkedIn posts

Run:

```bash
python preprocess.py
```

This extracts metadata from raw posts, unifies similar tags, and saves the enriched data in `data/processed_posts.json`.

### Step 2: Generate a LinkedIn post

Run:

```bash
python post_generator.py
```

The generator uses the selected topic, language, and length to create a LinkedIn post using few-shot examples.

## Example Configuration

```python
post = generate_post("Short", "English", "Motivation")
print(post)
```

Supported length categories:

- Short: 1–10 lines
- Medium: 10–20 lines
- Long: 20–30 lines

Supported languages:

- English

## How It Works

1. Raw LinkedIn posts are loaded from a JSON file.
2. An LLM extracts metadata such as line count, language, and tags.
3. Similar tags are unified to create standardized categories.
4. Processed posts are stored in JSON format.
5. Few-shot examples are selected based on the requested length, language, and topic.
6. The LLM generates a new LinkedIn post using the selected examples as writing-style references.

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key used to access Groq-hosted language models |

## Future Improvements

- Add a web-based user interface.
- Support additional languages.
- Improve tag extraction and categorization.
- Add controls for tone, audience, and writing style.

## License

This project is intended for educational and personal use.
