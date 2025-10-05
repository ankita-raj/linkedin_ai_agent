from transformers import pipeline

# Use a slightly larger model for better text quality
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_linkedin_post(topic):
    prompt = (
        f"Write a concise, professional, and engaging LinkedIn post about {topic}. "
        f"Keep it under 120 words, use a friendly tone, and end with a takeaway or motivational line."
    )

    result = generator(
        prompt,
        max_new_tokens=150,
        num_beams=4,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.5,
        early_stopping=True,
    )

    return result[0]["generated_text"].strip()

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    print("\n--- Generated LinkedIn Post ---\n")
    print(generate_linkedin_post(topic))
