"""Generate a word cloud from a list of phrases."""

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_word_cloud(phrases, output_file=None):
    """
    Generate a word cloud from a list of phrases.
    
    Args:
        phrases (list): List of phrases or a single string of text
        output_file (str, optional): Path to save the word cloud image.
                                     If None, displays the word cloud.
    """
    # Convert list to string if needed
    if isinstance(phrases, list):
        text = " ".join(phrases)
    else:
        text = phrases
    
    # Create word cloud with white background
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis"
    ).generate(text)
    
    # Display the word cloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    
    # Save or show
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        print(f"Word cloud saved to {output_file}")
    else:
        plt.show()


if __name__ == "__main__":
    # Example usage
    use_cases = [
    "Reasoning Path Tracing", "Tool Call Latency Monitoring", 
    "Token Consumption Tracking", "Loop Break Detection", 
    "Success vs Failure Rate Analytics", "Hallucination Detection", 
    "Planning Quality Evaluation", "Context Window Overload Monitoring", 
    "Model Drift Analysis", "Semantic Logging",  "Chain-of-thought", 
    "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics",
    "Inter-Agent Communication Tracing", "Conflict Resolution Monitoring", 
    "Agent Role Alignment", "Resource Contention Tracking", 
    "Guardrail Violation Alerts", "PII Leakage Detection", 
     "Chain-of-thought", 
    "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics",
    "Agent Permission Auditing", "Human-in-the-Loop Handoff Analytics", 
    "Prompt Injection Monitoring", "Audit Trail Compliance", "Chain-of-thought", 
    "Adoption Dashboard", "Performance Benchmarking","Success vs Failure Rate Analytics"
]
    
    # Generate and display word cloud
    generate_word_cloud(use_cases)
    
    # To save to a file instead, use:
    generate_word_cloud(use_cases, "wordcloud.png")
