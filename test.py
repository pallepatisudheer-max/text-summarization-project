from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    framework="pt"   # Force PyTorch
)

text = """
Artificial intelligence is transforming industries around the world.
Machine learning and deep learning techniques are helping businesses
analyze large amounts of data and make better decisions.
"""

result = summarizer(
    text,
    max_length=50,
    min_length=10,
    do_sample=False
)

print(result[0]["summary_text"])