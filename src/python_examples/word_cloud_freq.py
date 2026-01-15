import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

# The 20 Agentic AI Observability use cases as full phrases
use_cases = [
    "Reasoning Path Tracing", "Tool Call Latency Monitoring", "Adoption Dashboard", "Adoption Dashboard", "Adoption Dashboard",
    "Token Consumption Tracking", "Loop Break Detection", 
    "Success vs Failure Rate Analytics", "Hallucination Detection", 
    "Planning Quality Evaluation", "Context Window Overload Monitoring", 
    "Model Drift Analysis", "Semantic Logging",  "Chain-of-thought", 
    "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics",
    "Inter-Agent Communication Tracing", "Conflict Resolution Monitoring", 
    "Agent Role Alignment", "Resource Contention Tracking", 
    "Guardrail Violation Alerts", "PII Leakage Detection", 
     "Chain-of-thought", "Chain-of-thought", "Chain-of-thought", "Chain-of-thought", 
    "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics",
    "Agent Permission Auditing", "Human-in-the-Loop Handoff Analytics", 
    "Prompt Injection Monitoring", "Audit Trail Compliance", "Chain-of-thought", 
    "Adoption Dashboard", "Adoption Dashboard", "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics", "Success vs Failure Rate Analytics", "Success vs Failure Rate Analytics", "Success vs Failure Rate Analytics"
]

# Count actual phrase frequencies
phrase_counts = Counter(use_cases)
frequencies = phrase_counts

# Create the WordCloud object
wordcloud = WordCloud(
    width=1600, 
    height=800, 
    background_color='white',
    colormap='tab10',       # Colorful professional palette
    prefer_horizontal=0.9,  # Higher value helps keep long phrases on one line
).generate_from_frequencies(frequencies)

# Display the result
plt.figure(figsize=(15, 7.5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# To save the file:
wordcloud.to_file("agentic_ai_phrase_cloud.png")