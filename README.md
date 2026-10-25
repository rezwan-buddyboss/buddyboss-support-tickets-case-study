# BuddyBoss support tickets case study

Real complex BuddyBoss support tickets, solved by the Tier 2 support team and written up as short case studies. Each case says what the customer saw, how it was debugged, what fixed it and how to spot it next time.

All customer data is removed before a case is published: no names, emails, domains, logins, keys or site details.

## Folders

| Folder | What it holds |
|---|---|
| cases/ | One file per root cause, by product type then area: cases/app/builds, cases/web/groups, cases/integration/learndash |
| debug-guides/ | How to debug an area in general, same folders as cases |
| index/ | Generated search files: errors.md, and one catalog per product type |
| templates/ | case-template.md, the format every case follows |
| scripts/ | build_index.py rebuilds the index, find_cases.py ranks cases for a ticket |
| claude-code-search-skill/ | Small Claude Code skill that searches this repo while solving tickets |

## Product types

app, web, addon, integration. Area is the feature or integration name, such as builds, groups, readylaunch, learndash.

## Searching

1. index/errors.md for an exact error match
2. index/catalog-app.md, catalog-web.md, catalog-addon.md or catalog-integration.md for title and keyword matches
3. Open only the best 2 or 3 cases

From a local clone: `python3 scripts/find_cases.py "E017 ios build failed" --type app --area builds`

## Adding a case

Copy templates/case-template.md into the right cases/type/area folder, name it after the issue in lowercase with dashes, then run `python3 scripts/build_index.py` and commit the case together with the index.
