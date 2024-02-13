import json
import re

def find_json_value(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from find_json_value(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from find_json_value(item, lookup_key)

def find_text_value(text_input, lookup_key):
    if isinstance(text_input, dict):
        for k, v in text_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from find_text_value(v, lookup_key)
    elif isinstance(text_input, list):
        for item in text_input:
            yield from find_text_value(item, lookup_key)

def get_sdnext_tags(image):
    tags = []
    items = image.info or {}
    if "parameters" in items:
        parameter_text = items["parameters"]

        # Extract information using regular expressions
        parameter_pattern = re.compile(r'(\w+): (.+?)(?:,|$)')
        parameters = re.findall(parameter_pattern, parameter_text)

        # Add extracted key-value pairs as tags
        for key, value in parameters:
            tags.append(f"{key}:{value.strip()}")

    return tags

