import spacy
import csv
from spacy.matcher import PhraseMatcher
from pathlib import Path


class SkillExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab, attr="LOWER")
        self.skills = self._load_skills()
        self._add_patterns()

    def _load_skills(self):
        skills = []
        csv_path = Path(__file__).resolve().parent.parent / "data" / "skills.csv"
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                skills.append(row["skill"])
        return skills

    def _add_patterns(self):
        patterns = [self.nlp.make_doc(skill) for skill in self.skills]
        self.matcher.add("SKILLS", patterns)

    def extract(self, text: str):
        doc = self.nlp(text)
        matches = self.matcher(doc)
        found_skills = set()

        for _, start, end in matches:
            found_skills.add(doc[start:end].text)

        return list(found_skills)
