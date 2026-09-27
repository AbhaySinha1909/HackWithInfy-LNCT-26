import re
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        mapping = dict(knowledge)
        return re.sub(r"\((.*?)\)", lambda m: mapping.get(m.group(1), "?"), s)