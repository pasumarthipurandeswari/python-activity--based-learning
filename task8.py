
# Student Feedback Sentiment Scoring

# Supplied keyword lists
positive_keywords = [
    "good", "excellent", "helpful", "clear",
    "interesting", "best", "amazing", "useful"
]

negative_keywords = [
    "bad", "poor", "boring", "difficult",
    "confusing", "worst", "slow", "unhelpful"
]

# Sentiment classification thresholds
positive_threshold = 2
negative_threshold = -2

# Get student feedback
n = int(input("Enter number of feedback sentences: "))

for i in range(n):
    print("\nFeedback", i + 1)
    feedback = input("Enter feedback sentence: ").lower()

    words = feedback.split()

    positive_count = 0
    negative_count = 0

    # Count positive and negative indicators
    for word in words:
        word = word.strip(".,!?;:\"'()")

        if word in positive_keywords:
            positive_count += 1

        if word in negative_keywords:
            negative_count += 1

    # Calculate sentiment score
    score = positive_count - negative_count

    # Classify feedback
    if score >= positive_threshold:
        sentiment = "Positive"
    elif score <= negative_threshold:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Display results
    print("Positive indicators:", positive_count)
    print("Negative indicators:", negative_count)
    print("Sentiment score:", score)
    print("Feedback classification:", sentiment)

print("\nFeedback analysis completed.")
