# Contribute to Momentum Community

<!-- dmc-review-policy:start -->
## Pull requests and review

This block is the DMC review standard. Every DMC repository carries it at the top of `AGENTS.md`; the shared PR proof check refuses a pull request whose target branch lacks it. The source is `configs/global/review-policy.md` in `dmc-technologies/agent-ops`; change it there.

- Open pull requests under the GitHub login this machine is configured with, and never switch to another person's login. DMC-managed machines use the agent account `dmc-agents`; a teammate's machine uses that teammate's own login, and `.github/agent-accounts` lists the agent accounts. Open the pull request as a draft with `Proof: pending`; mark it ready when CI is green and the proof is recorded.
- The description starts with `Proof: clip`, `Proof: screenshots`, or `Proof: checks — <why nothing a person runs changed>`, then the headings What problem this solves, User impact, Why this change was made, Evidence, and Excluded. Evidence holds the exact commands with their results and exit status. Write no `Criticality:` line, no agent attribution footer, and no Co-Authored-By trailer. Set a body with `gh api -X PATCH repos/<owner>/<repo>/pulls/<n> -F body=@file`; `gh pr edit --body` fails on DMC repositories.
- CodeRabbit reviews every non-draft pull request into `main` or a `demo/` branch, reviews each later push, and applies one tier label: `routine`, `moderate`, or `critical`. Never add or remove a tier label. A person may add `critical`. A change under `.github/workflows/` or of more than 40 files is critical whatever the label says.
- `routine` and `moderate` merge on their own once CodeRabbit approved them and the required checks pass; after pushing, fix findings and wait. `critical` needs an approving review from a person who is neither the author nor an agent account; PR proof requests the people in `.github/critical-reviewers`, blocks the merge until that approval exists, and the merge rule then lands it. Never use `gh pr merge --admin` on a critical pull request.
- Post `@coderabbitai review` only when no review ran, and `@coderabbitai full review` after a redesign. Verify a finding before changing code, add a failing test before a correction, and resolve a conversation only after the correction passes.
- Full guide: the README and `docs/coderabbit-for-dummies.md` in `dmc-technologies/coderabbit`. The check: `.github/workflows/pr-proof.yml` in `dmc-technologies/agent-ops`.
<!-- dmc-review-policy:end -->

Read [README.md](README.md) before changing this repository. It is a public community space for questions, bug reports, and ideas, not Momentum's product source or a deployment repository.

## Scope and public content

Improve participation guidance, navigation, and issue forms within the requested scope. Do not copy private product source, internal architecture, customer material, proposals, credentials, or operational configuration into this repository. Link an access-controlled resource when relevant and label the access requirement.

Do not infer supported product features, release status, or service availability from a demonstration video or an issue report. Preserve the distinction between a user's observation and a verified product claim.

## Find the owner

- [README.md](README.md) routes community participants.
- [.github/ISSUE_TEMPLATE/bug_report.yml](.github/ISSUE_TEMPLATE/bug_report.yml) owns the bug report fields.
- [.github/ISSUE_TEMPLATE/config.yml](.github/ISSUE_TEMPLATE/config.yml) owns the issue chooser's contact links and whether blank issues are allowed.
- [.github/workflows/ci.yml](.github/workflows/ci.yml) runs [scripts/check_links.py](scripts/check_links.py), which refuses a Markdown link whose local destination does not exist. CodeRabbit reviews every pull request under the DMC central configuration. A documentation change does not authorize changing review policy.

Before changing a link, verify its destination and access requirement. Before changing a form, inspect its field identifiers, required fields, and contact routes. For documentation-only work, inspect the rendered Markdown, check local destinations, and record which external links were actually checked. Automation tests are separate evidence; they do not prove that the guidance is understandable.
