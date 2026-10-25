"""Rank cases against words from a new ticket. Used by Claude Code on a local clone.

    python3 scripts/find_cases.py "E017 ios build failed certificate" --type app --area builds

Scoring: exact error match counts most, then title words, then keywords,
then symptoms, then the rest of the file. Version is never used to rank.
"""
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
WEIGHTS = {"error": 10, "title": 4, "keywords": 3, "symptoms": 2, "body": 1}
# Below this a match is noise, such as one shared common word
MIN_SCORE = 6


def parts(path):
    text = path.read_text(encoding="utf-8").lower()
    match = re.match(r"---\n(.*?)\n---(.*)", text, re.S)
    head, body = (match.group(1), match.group(2)) if match else ("", text)
    fields = dict(
        (k.strip(), v.strip().strip('"'))
        for k, v in (line.split(":", 1) for line in head.splitlines() if ":" in line)
    )
    symptoms = re.search(r"## symptoms\n(.*?)(\n## |\Z)", body, re.S)
    return {
        "error": fields.get("error", ""),
        "title": fields.get("title", ""),
        "keywords": fields.get("keywords", ""),
        "symptoms": symptoms.group(1) if symptoms else "",
        "body": body,
    }


def score(query, case):
    total = 0
    for error in filter(None, (e.strip() for e in case["error"].split(","))):
        if error in query:
            total += WEIGHTS["error"] * 3
    for word in set(re.findall(r"[a-z0-9]{3,}", query)):
        for field, weight in WEIGHTS.items():
            if word in case[field]:
                total += weight
    return total


def search(query, folder):
    files = sorted(folder.rglob("*.md")) if folder.exists() else []
    ranked = [(score(query, parts(f)), f) for f in files]
    return sorted([r for r in ranked if r[0] >= MIN_SCORE], reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--type")
    parser.add_argument("--area")
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()
    query = args.query.lower()

    # Narrow by folder first, then widen when fewer than 2 good matches
    folders = []
    if args.type and args.area:
        folders.append(ROOT / "cases" / args.type / args.area)
    if args.type:
        folders.append(ROOT / "cases" / args.type)
    folders.append(ROOT / "cases")

    results = []
    for folder in folders:
        results = search(query, folder)
        if len(results) >= 2:
            break

    if not results:
        print("No matching case found")
        return
    for points, path in results[: args.top]:
        print(f"{points:>4}  {path.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
