import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
sim_model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L12-v2')

sentences = []
sim_values = []
filename = "q&a_formatted_final.csv"
genre_predicted = "Self esteem"
emotion = "Anger"
intensity = 2
MyText = "How can i cope with anger without resorting to brash activities?"
print("User: "+MyText)
complete = pd.read_csv(filename)
similar_question_set = complete[complete['Genre']==genre_predicted]
similar_question_set = similar_question_set[similar_question_set['Emotion']==emotion]
similar_question_set = similar_question_set[similar_question_set['Intensity']==intensity]

max = 0
for row in similar_question_set['Questions']:
    sentences.append(row)
sentences.append(MyText)

embeddings = sim_model.encode(sentences)
j = 0
for i in range (5):
    temp = cosine_similarity(embeddings[i].reshape(1,-1),embeddings[5].reshape(1,-1))
    sim_values.append(temp)
    if max<temp:
        max = temp
        j = i
for row in similar_question_set['Answers']:
    j=j-1
    if (j == -1):
        response = row
print("Chatbot: "+response)