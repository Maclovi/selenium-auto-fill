import json
import re

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

data = {}
doc = Document("basedata/attestation.docx")
key = None
count = 1
i = 1

for content in doc.iter_inner_content():
    if isinstance(content, Paragraph):
        pattern = r"(ответ(а)?|последовательность|действий)\)"
        if re.search(pattern, content.text):
            pattern = r"^(\s+)?(\d+.)?(\s+)?|\n|:(\s+)?$"
            text = " ".join(re.sub(pattern, "", content.text).split())
            text = f"{i}. " + text
            key = text
            data[key] = []
            count = 1
            i += 1

        elif key:
            text = " ".join(
                content.text.strip().replace("\n", "").split()
            )
            if not text:
                key = None
                continue

            text = re.sub(r"^\d+\)\s?|;$", "", text)
            numeric = f"{count}) "
            if any(run.bold and run.text.strip() for run in content.runs):
                numeric = "." + numeric
            data[key].append(numeric + text)
            count += 1

    elif isinstance(content, Table) and key:
        data[key] = []
        for row in content.rows:
            cells = row.cells
            pattern = r"^\d+(\.)?"
            if coincs := re.search(pattern, cells[0].text):
                coinc = coincs.group()
                string_row = " ".join(cell.text.strip() for cell in row.cells)
                string_row = string_row.replace(coinc, f"№-{coinc}", 1)
                data[key].append(string_row)


for k, v in data.items():
    print(k)
    print(*v, sep="\n", end="\n\n")


with open("attestation.json", "w") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
