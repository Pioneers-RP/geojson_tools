import json
from geojson_dict import get_geojson_dict

def read_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_geojson(file_path, data):
    """Écrire le contenu modifié dans le fichier GeoJSON."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_area_in_geojson(geojson_data, areas_list):
    """Met à jour le champ AREA pour chaque région avec la liste fournie."""
    for feature in geojson_data['features']:
        region_name = feature['properties'].get('NAME_1') or feature['properties'].get('VARNAME_1')
        for region in areas_list:
            if region_name in region:
                feature['properties']['AREA'] = region[region_name]
                break
    return geojson_data


def main():
    
    args = get_geojson_dict()
    file = args[0]
    geojson_data = read_geojson(file)
    areas_list = args[1]
    print(areas_list)
    updated_data = update_area_in_geojson(geojson_data, areas_list)
    write_geojson(file, updated_data)
    print("Le fichier GeoJSON a été mis à jour avec les nouvelles valeurs d'AREA.")

if __name__ == "__main__":
    main()
