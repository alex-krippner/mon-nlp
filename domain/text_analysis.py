from domain.nlp_processor import NlpProcessor


class TextAnalyzer:
    def __init__(self, analysis_adapter: NlpProcessor):
        self.analysis_adapter = analysis_adapter

    def analyze_text(self, text):
        return self.analysis_adapter.tokenize(text)
