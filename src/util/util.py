import re

from urllib.parse import urlparse, urlencode, parse_qs, urlunparse


def remove_non_printable_chars(input_string):
    # Keep only printable ASCII characters
    printable_chars = re.sub(r'[^\x20-\x7E]', '', input_string)
    return printable_chars


def extract_links_from_text(text):
    # Define a regular expression pattern for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # Find all matches in the text
    links = re.findall(url_pattern, text)
    return links


def edit_url_attribute(url_: str, attribute_name, new_attribute_value):
    attribute_index = url_.index(attribute_name)
    before_url = url_[:attribute_index]
    next_attribute_index = url_.find('&', attribute_index, len(url_)-1)
    after_url = ''
    if next_attribute_index != -1:
        after_url = url_[next_attribute_index:]

    new_url = f'{before_url}{attribute_name}={new_attribute_value}{after_url}'
    return new_url

