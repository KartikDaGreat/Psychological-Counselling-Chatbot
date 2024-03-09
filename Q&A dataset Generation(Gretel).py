import openai
import csv

openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo"):
    message = ({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model=model, messages=message)
    return response.choices[0].message.content

def generate_and_store_queries(topics, emotions, intensity, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Query', 'Response']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for genre in topics:
            for emt in emotions:
                for intense in intensity:
                    prompt = f"What are the 5 most common questions a person who currently has {intense} {emt} might ask a psychological counsellor now on the topic of {genre} and what is a similar answer that can be given? Give the results in question followed by $ symbol followed by answer format."
                    response = get_completion(prompt)
                    writer.writerow({'Query': prompt, 'Response': response})
                    print(prompt)

if __name__ == "__main__":
    topics = ["Self esteem", "Relationships", "Anger Management", "Domestic Violence", "Substance Abuse", "Family Conflict"]
    emotions = ["Anger", "Disgust", "Fear", "Happy", "Sad", "Surprised"]
    intensity = ["Little(Low)", "Kind of(Medium)", "Extremely(High)"]  # Low, Medium, High
    csv_filename = "generated_queries.csv"

    generate_and_store_queries(topics, emotions, intensity, csv_filename)
