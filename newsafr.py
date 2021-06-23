import collections
import xml.etree.ElementTree as ET

def read_xml(file_path, max_len_word=6, top_word=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(file_path, parser)
    root = tree.getroot()
    xml_title = root.findall('channel/item/description')
    description_words = []
    for title in xml_title:
        description = [word for word in title.text.split(' ') if len(word) > max_len_word]
        description_words.extend(description)
        counter_words = collections.Counter(description_words)
    return counter_words.most_common(top_word)



print(read_xml('newsafr.xml'))