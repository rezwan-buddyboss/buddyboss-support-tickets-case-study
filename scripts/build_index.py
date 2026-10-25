"""Rebuild index/errors.md and index/catalog-<type>.md from the case files.

Run from the repo root after adding or changing a case:
    python3 scripts/build_index.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = "https://raw.githubusercontent.com/rezwan-buddyboss/buddyboss-support-tickets-case-study/main/"
TYPES = ["app", "web", "addon", "integration"]


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    fields = {}
    if not match:
        return fields
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.split("  #")[0].strip().strip('"')
        fields[key.strip()] = value
    return fields


def main():
    cases = []
    for path in sorted((ROOT / "cases").rglob("*.md")):
        fields = front_matter(path)
        rel = path.relative_to(ROOT).as_posix()
        fields["path"] = rel
        fields["url"] = RAW + rel
        cases.append(fields)

    index = ROOT / "index"
    index.mkdir(exist_ok=True)

    errors = [
        "# Error index",
        "",
        "Exact error message or code, then the case that holds it. Search this first.",
        "",
        "| Error | Case | URL |",
        "|---|---|---|",
    ]
    for case in sorted(cases, key=lambda c: c.get("error", "").lower()):
        if case.get("error"):
            errors.append(f"| {case['error']} | {case.get('title', '')} | {case['url']} |")
    (index / "errors.md").write_text("\n".join(errors) + "\n", encoding="utf-8")

    for case_type in TYPES:
        rows = [
            f"# Catalog: {case_type}",
            "",
            "One line per case. Match on title and keywords, then open only the URL of the best 2 or 3.",
            "",
            "| Area | Title | Keywords | Tickets | URL |",
            "|---|---|---|---|---|",
        ]
        for case in cases:
            if case.get("type") == case_type:
                rows.append(
                    f"| {case.get('area', '')} | {case.get('title', '')} | {case.get('keywords', '')}"
                    f" | {case.get('tickets', '')} | {case['url']} |"
                )
        (index / f"catalog-{case_type}.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"Indexed {len(cases)} cases")


if __name__ == "__main__":
    main()
