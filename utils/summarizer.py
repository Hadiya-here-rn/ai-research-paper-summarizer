from transformers import pipeline
from typing import List
import torch

# Use GPU if available
device = 0 if torch.cuda.is_available() else -1

# Load the summarization model only once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

def chunk_text(text: str, max_chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + max_chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def summarize_text(text: str) -> str:
    """Summarize long text by processing in chunks and combining the results."""
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=300,
            min_length=100,
            do_sample=False
        )
        summaries.append(result[0]["summary_text"])

    final_summary = "\n\n".join(summaries)
    return final_summary
