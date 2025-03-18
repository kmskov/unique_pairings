import json
import itertools
import random

def generate_new_pairings(entities, existing_pairings):
    all_possible_pairings = set(itertools.combinations(entities, 2))
    available_pairings = list(all_possible_pairings - existing_pairings)
    random.shuffle(available_pairings)
    
    used_entities = set()
    final_pairings = []
    
    for pair in available_pairings:
        if pair[0] not in used_entities and pair[1] not in used_entities:
            final_pairings.append(pair)
            used_entities.update(pair)
            
        if len(used_entities) == len(entities):
            break
    
    return final_pairings

def validate_pairings(entities, existing_pairings):
    entity_set = set(entities)
    for pair in existing_pairings:
        if pair[0] not in entity_set or pair[1] not in entity_set:
            raise ValueError(f"Invalid pairing {pair}: one or both entities are not in the entities list.")

def main():
    data = {
        "entities": ["Wallachia", "Caledor", "Pale City", "Blood Sweat", "Darkwood", "RDWH", "Dreaming Woods", "Khorne Dogs", 
                     "Squeaky Peekers", "Lords Or The Edge", "Jersey Giants", "Orchestrated Death", "Reikland", "Red Shirts", 
                     "MuckNuggets", "Da Grot Grabbuz"],
        "existing_pairings": [["Squeaky Peekers", "Red Shirts"], ["Reikland", "Wallachia"], ["Lords Or The Edge", "Jersey Giants"],
                              ["Darkwood", "Pale City"], ["Caledor", "Blood Sweat"], ["Khorne Dogs", "Orchestrated Death"], 
                              ["Dreaming Woods", "MuckNuggets"], ["RDWH", "Reikland"], ["Red Shirts", "Lords Or The Edge"], 
                              ["Wallachia", "Darkwood"], ["Jersey Giants", "Caledor"], ["Pale City", "Khorne Dogs"], 
                              ["Blood Sweat", "Dreaming Woods"], ["MuckNuggets", "Orchestrated Death"], ["Da Grot Grabbuz", "RDWH"], 
                              ["Squeaky Peekers", "Da Grot Grabbuz"]]
    }
    
    entities = data.get("entities", [])
    existing_pairings = set(tuple(sorted(pair)) for pair in data.get("existing_pairings", []))
    
    validate_pairings(entities, existing_pairings)
    new_pairings = generate_new_pairings(entities, existing_pairings)
    
    result = {"new_pairings": new_pairings}
    print(json.dumps(result))

if __name__ == "__main__":
    main()
