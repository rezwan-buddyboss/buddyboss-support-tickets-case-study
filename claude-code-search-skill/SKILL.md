---
name: buddyboss-kb-search
description: Search the BuddyBoss support case study knowledge base for previously solved tickets that match a new ticket. Use whenever a BuddyBoss support ticket, error message or customer issue is being diagnosed, before suggesting a cause or fix.
---

# BuddyBoss KB search

Solved complex tickets live as case files in the public repo rezwan-buddyboss/buddyboss-support-tickets-case-study. Read only the index and the best 2 or 3 cases, never the whole repo.

## 1. Pull five signals from the ticket

Error message or code, product type (app, web, addon, integration), area (builds, groups, learndash and so on), 3 to 8 keywords in the customer's words, version if mentioned.

## 2. Get the KB

Local clone first. If ~/buddyboss-support-tickets-case-study exists, run `git -C ~/buddyboss-support-tickets-case-study pull --quiet` once per session, then:

    python3 ~/buddyboss-support-tickets-case-study/scripts/find_cases.py "<error and keywords>" --type <type> --area <area>

No clone: fetch over the web instead.

1. https://raw.githubusercontent.com/rezwan-buddyboss/buddyboss-support-tickets-case-study/main/index/errors.md when the ticket has an error message or code
2. https://raw.githubusercontent.com/rezwan-buddyboss/buddyboss-support-tickets-case-study/main/index/catalog-<type>.md for the product type
3. Fetch only the URLs of the best 2 or 3 matching rows

## 3. Use what you find

- Exact error match is strongest, then title, then keywords, then symptoms.
- Version is never used to find a case. Compare it only after a case is found and both sides have one.
- A similar case is a lead, not a diagnosis. Try the old fix or its debugging steps on the current setup before trusting it.
- Name the case file you used, so it can be checked.
- No match: say "No matching KB case" and carry on. Never stretch a near match into a diagnosis, and never invent a case.
