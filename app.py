import spacy

nlp = spacy.load("ja_core_news_sm")

doc = nlp("ウクライナのウォロディミル・ゼレンスキー大統領は13日、キリスト教カトリック教会のローマ教皇庁 (ヴァチカン)を訪れ、教皇フランシスコと会談した")
print([ent.text for ent in doc.ents])