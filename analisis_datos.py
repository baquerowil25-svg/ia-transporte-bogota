import spacy

nlp = spacy.load("es_core_news_sm")

def analyze_data(data):

    issues = {}

    for text in data:
        doc = nlp(text)

        for ent in doc.ents:

            if ent.label_ == "LOC":

                if ent.text not in issues:
                    issues[ent.text] = 0

                issues[ent.text] += 1

    return issues

if __name__ == "__main__":

    datos = [
        "Mucha congestión en Suba",
        "Demoras en Kennedy",
        "Problemas de buses en Suba"
    ]

    print(analyze_data(datos))