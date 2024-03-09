from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L12-v2')
sentences=[' I often find myself getting angry very easily, especially in frustrating situations. It leads to me yelling and saying things I regret later. How can I learn to manage my anger more effectively?',
           'I struggle with controlling my temper, particularly when I feel disrespected or treated unfairly. I get frustrated and angry quickly, and sometimes I lash out verbally. Do you have any strategies to help me manage my anger in a healthier way?',
           'I am feeling overwhelmed and stressed lately. What are some relaxation techniques I can try to manage my stress?',
           'What are the different types of clouds and how are they formed?']
embeddings = model.encode(sentences)
print(embeddings)
print(len(embeddings))
print(len(embeddings[0]))
print(cosine_similarity(embeddings[0].reshape(1,-1),embeddings[1].reshape(1,-1)))
print(cosine_similarity(embeddings[2].reshape(1,-1),embeddings[3].reshape(1,-1)))
print(cosine_similarity(embeddings[0].reshape(1,-1),embeddings[3].reshape(1,-1)))
