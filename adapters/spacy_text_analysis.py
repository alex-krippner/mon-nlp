from typing import Dict, List
import spacy
from domain.nlp_processor import NlpProcessor
import adapters.genproto.monNlpService_pb2

nlp = spacy.load("ja_core_news_sm")


def map_tokens(doc):
    tokens = []

    for token in doc:
        t = adapters.genproto.monNlpService_pb2.Token(
            text=token.text,
            orth_=token.orth_,
            lemma_=token.lemma_,
            norm_=token.norm_,
            lower_=token.lower_,
            shape_=token.shape_,
            prefix_=token.prefix_,
            suffix_=token.suffix_,
            pos_=token.pos_,
            tag_=token.tag_,
            dep_=token.dep_,
            lang_=token.lang_,
        )
        tokens.append(t)

    return tokens


class SpacyTextAnalysis(NlpProcessor):
    def tokenize(self, text) -> List[Dict[str, str]]:
        doc = nlp(text)

        tokens = map_tokens(doc)
        return tokens
