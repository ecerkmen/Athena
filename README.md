# Athena 🦉
**A local RAG (Retrieval-Augmented Generation) system for your research and study notes.**

Athena lets you ask questions and get answers — not from the internet, but from your own documents. Feed it your lecture notes, papers, and research files, and it will retrieve the most relevant parts to answer your questions using Claude AI.

Built with Python · ChromaDB · sentence-transformers · Anthropic API

---

## What it does

- Ingests your `.txt`, `.pdf`, and `.docx` files
- Breaks them into chunks and converts them into vector embeddings
- Stores everything locally on your machine
- Takes your question, finds the most relevant chunks from your documents, and generates an answer using Claude

---

## Who it's for

- Graduate and PhD students with large volumes of notes and papers
- Researchers who want to query their own corpus instead of relying on general AI
- Anyone who needs to navigate through large amounts of personal documents

---

## Requirements

- Python 3.11 (important — do not use 3.12 or later)
- An Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com) — requires a minimum $5 credit purchase)

---

## Installation

**1. Clone the repository**

```
git clone https://github.com/ecerkmen/athena.git
cd athena
```

**2. Install the required libraries**

Open your terminal and run:

```
pip install sentence-transformers chromadb pymupdf python-docx anthropic
```

**3. Set your Anthropic API key**

In your terminal, run the following (replace the value with your actual key):

On Windows (PowerShell):
```
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

On Mac/Linux:
```
export ANTHROPIC_API_KEY="your-api-key-here"
```

> Important: you must do this every time you open a new terminal window before running `generate.py`. The key is not saved permanently.

---

## How to use

### Step 1 — Run `vectorise.py`

```
python vectorise.py
```

This script sets up your folder structure, lets you add documents, and converts everything into vectors stored locally.

**What the script will ask you:**

**"Enter the name of the subject folder:"**
Type the name of a subject (e.g. `Machine Learning`, `Thesis`, `History`). Press Enter to create it.
When you are done creating subject folders, press Enter without typing anything to move on.

**"Enter pathname for the document:"**
After each folder is created, the script immediately asks you to add documents to it.

You have two options here:

- **Option A — Enter the file path:** Copy the full path of your file and paste it here. Do not include quotation marks around the path.

  Example on Windows: `C:\Users\yourname\Desktop\notes.pdf`

  Example on Mac: `/Users/yourname/Desktop/notes.pdf`

  To copy a file path on Windows: right-click the file → "Copy as path", then remove the quotation marks before pasting.

- **Option B — Add files manually:** Press Enter without typing anything to skip this step. Then go to your Desktop, open the `Athena/athena_train/` folder, find the subject folder you just created, and drag your files directly into it. You can do this for as many files as you like.

Press Enter without typing anything when you are done adding documents to a subject folder. The script will then ask for the next subject folder name.

Once you have finished adding all subjects and documents, press Enter without typing anything at the subject folder prompt to exit. The script will then process all your documents and store them as vectors. This may take a few minutes depending on the size of your files.

---

### Step 2 — Run `generate.py`

```
python generate.py
```

**What the script will ask you:**

**"Enter your question:"**
Type your question in plain language and press Enter. Athena will search your documents and return an answer based on what it finds.

Example questions:
- `What are the main challenges of BPE tokenization for agglutinative languages?`
- `Summarize the methodology in my paper on transfer learning`
- `What did my notes say about attention mechanisms?`

---

## Important notes

- Run `vectorise.py` again any time you add new documents to your collection
- Your documents and vectors are stored locally — nothing is uploaded anywhere
- The API key must be set in the terminal before running `generate.py`
- Supported file types: `.txt`, `.pdf`, `.docx`

---

## Project structure

```
athena/
├── vectorise.py       # ingestion, chunking, embedding, storage
├── generate.py        # querying and answer generation
└── README.md
```

The `Athena/` folder (created on your Desktop when you run the script) is not part of the repository — it lives locally on your machine.

---

## Built by

Ece — [github.com/ecerkmen](https://github.com/ecerkmen)
