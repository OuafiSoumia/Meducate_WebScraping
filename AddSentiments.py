#!pip install -q transformers
#!pip install sentencepiece

import json
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from transformers import pipeline

# French sentiment analysis
class SentimentAnalysis:
    def __init__(self):
        tokenizer = AutoTokenizer.from_pretrained("tblard/tf-allocine")
        model = TFAutoModelForSequenceClassification.from_pretrained("tblard/tf-allocine")
        self.nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

    def predict(self, text):
        return self.nlp(text)

# Chargement du fichier JSON
input_file_path = 'medicals.json'
with open(input_file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Création de l'objet SentimentAnalysis
sentiment_analysis = SentimentAnalysis()

# Parcourir les données et prédire les sentiments
segment_sentiments = []
for item in data:
    if "comments" in item and isinstance(item["comments"], list):
        all_comments_combined = " ".join(item["comments"])

        # Décomposer le texte combiné en segments de longueur admissible
        max_segment_length = 512  # Taille maximale d'un segment pour le modèle
        segments = [all_comments_combined[i:i + max_segment_length] for i in range(0, len(all_comments_combined), max_segment_length)]

        # Prédiction du sentiment pour chaque segment et stockage des résultats
        for segment in segments:
            if len(segment.strip()) == 0:
                segment_sentiments.append({'label': 'NEUTRAL', 'score': 0.5})
            else:
                segment_sentiments.extend(sentiment_analysis.predict(segment))

# Prédiction du sentiment global en prenant en compte toutes les prédictions de segments
overall_sentiment = max(segment_sentiments, key=lambda x: x['score'])['label']

# Ajout du sentiment global à chaque élément du JSON
for i, item in enumerate(data):
    if "comments" in item and isinstance(item["comments"], list):
        if len(item["comments"]) == 0:
            item["sentiments"] = "NEUTRAL"
        elif i < len(segment_sentiments):
            item["sentiments"] = segment_sentiments[i]['label']
        else:
            item["sentiments"] = "NEUTRAL"  # Si segment_sentiments n'a pas assez d'éléments
    else:
        item["sentiments"] = "NEUTRAL"  # Si 'comments' n'est pas présent ou n'est pas une liste

# Sauvegarde des résultats dans un nouveau fichier JSON
output_file_path = "medicals2.json"
with open(output_file_path, 'w', encoding='utf-8') as json_output_file:
    json.dump(data, json_output_file, ensure_ascii=False, indent=4)

print("Prédictions de sentiments terminées. Le résultat global est enregistré dans", output_file_path)
