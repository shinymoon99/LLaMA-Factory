import re
import json
def insert_after_pattern(input_string, pattern, content_to_insert):
    # Find the position of the pattern match
    match = re.search(pattern, input_string)
    if match:
        # Insert content after the pattern match
        position = match.end()
        return input_string[:position] + " "+content_to_insert+" "+ input_string[position:]
def augment_event_label(input_string,label_string):
    # Identify event tokens and their labels
    events = {}
    for token in input_string.split():
        if token.startswith("<event"):
            event_label = token[1:-1]
            event_token = input_string[input_string.find(token) + len(token): input_string.find("</" + event_label + ">")].strip()
            events[event_label] = event_token
    alabel = insert_after_pattern(label_string,"event1",events["event1"])
    alabel = insert_after_pattern(alabel,"event2",events["event2"])
    return alabel
def load_json_line_by_line(filename):
    data = []
    with open(filename, 'r',encoding="utf-8") as file:
        for line in file:
            try:
                json_data = json.loads(line.strip())
                data.append(json_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    return data