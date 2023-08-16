import json
import re

# Charger le fichier JSON
with open('pharmacys2.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Parcourir les éléments dans le JSON
for item in data:
    # Obtenir la valeur de l'élément correspondant
    cell_value = item['name']

    # Supprimer les mots indésirables
    clean_value = re.sub(r'\b(?:PHARMACIE|pharmacie|Gynécologie|pediatrie|pediatre|Gynécologue|Gynécologie|-|:|(|)|à|Marrakech|Allergologue|cardiologie|pédiatrique|chirurgien|pédiatre|et|de|les|des)\b', '', cell_value, flags=re.IGNORECASE)
    clean_value = re.sub(r'\s+', ' ', clean_value).strip()  # Supprimer les espaces supplémentaires

    # Mettre à jour la valeur dans l'élément JSON
    item['name'] = clean_value

# Enregistrer les modifications dans un nouveau fichier JSON
with open('pharmacys2Clean.json', 'w', encoding='utf-8') as json_output:
    json.dump(data, json_output, ensure_ascii=False, indent=4)

print('Nettoyage terminé avec succès.')
