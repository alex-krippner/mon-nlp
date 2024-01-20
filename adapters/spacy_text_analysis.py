from typing import Dict, List
import spacy
from domain.nlp_processor import NlpProcessor

nlp = spacy.load("ja_core_news_sm")


class SpacyTextAnalysis(NlpProcessor):
    def tokenize(self, text) -> List[Dict[str, List[str]]]:
        doc = nlp(text)
        entities = []
        for ent in doc.ents:
            named_entity = {"text": ent.text, "label": ent.label}
            entities.append(named_entity)
        return entities
