from transformers import pipeline

def summarize_text(text: str) -> str:
    if len(text) > 1000:
        text = text[:1000]

    # Load model only when this function is used
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    result = summarizer(text, max_length=200, min_length=100, do_sample=False)
    return result[0]["summary_text"]
