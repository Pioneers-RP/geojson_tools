import json
import argparse

def read_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_prompt(data):
    country = data['features'][0]['properties']['COUNTRY']  # On récupère le pays
    regions_info = []
    
    for feature in data['features']:
        varname = feature['properties'].get('NAME_1')  # On récupère le nom de la région
        if varname != "NA":
            regions_info.append(f"- {varname}")
        elif feature['properties'].get('VARNAME_1'):
            regions_info.append(f"- {feature['properties']['VARNAME_1']}:")
    
    regions_list = "\n".join(regions_info)  # Crée la liste sous forme de string
    prompt_text = '[{"NOM": TAILLE}, ...]'
    prompt = (f"Pour l'intégralité de la liste des régions du pays {country}, "
        f"donne moi une liste de dictionnaires, dont les dictionnaires doivent avoir pour clé le nom de la région, "
        f"""et pour valeur un int de sa superficie en kilomètres carrés. Ce dictionnaire doit être en oneline, et sous la forme suivante : '{prompt_text}'.\n"""
        f"{regions_list}")
    
    return prompt

def main():
    
    parser = argparse.ArgumentParser(description="Gestion des fichiers GeoJSON.")
    parser.add_argument("file", type=str, help="Chemin vers le fichier GeoJSON.")
    args = parser.parse_args()
    geojson_data = read_geojson(args.file)
    prompt = generate_prompt(geojson_data)
    print(prompt)

if __name__ == "__main__":
    main()
