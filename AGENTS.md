# Contribute to Momentum Community

Read [README.md](README.md) before changing this repository. It is a public community space for questions, bug reports, and ideas, not Momentum's product source or a deployment repository.

## Scope and public content

Improve participation guidance, navigation, and issue forms within the requested scope. Do not copy private product source, internal architecture, customer material, proposals, credentials, or operational configuration into this repository. Link an access-controlled resource when relevant and label the access requirement.

Do not infer supported product features, release status, or service availability from a demonstration video or an issue report. Preserve the distinction between a user's observation and a verified product claim.

## Find the owner

- [README.md](README.md) routes community participants.
- [.github/ISSUE_TEMPLATE/bug_report.yml](.github/ISSUE_TEMPLATE/bug_report.yml) owns the bug report fields.
- [.github/ISSUE_TEMPLATE/config.yml](.github/ISSUE_TEMPLATE/config.yml) owns the issue chooser's contact links and whether blank issues are allowed.
- [.github/workflows/](.github/workflows/) and [tests/test_review_gate.py](tests/test_review_gate.py) contain existing review automation and its checks. A documentation change does not authorize changing review policy.

Before changing a link, verify its destination and access requirement. Before changing a form, inspect its field identifiers, required fields, and contact routes. For documentation-only work, inspect the rendered Markdown, check local destinations, and record which external links were actually checked. Automation tests are separate evidence; they do not prove that the guidance is understandable.
