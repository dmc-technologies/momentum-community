# Contribute to Momentum Community

<!-- dmc-review-policy:start -->
## Pull requests and review

This block is the DMC review standard. Every DMC repository carries it at the top of `AGENTS.md`; the shared PR proof check refuses a pull request whose target branch lacks it. The source is https://github.com/dmc-technologies/agent-ops/blob/main/configs/global/review-policy.md; change it there.

- Open pull requests under the GitHub login this machine is configured with, and never switch to another person's login. DMC-managed machines use the agent account `dmc-agents`; `.github/agent-accounts` lists the agent accounts. Open the pull request as a draft with `Proof: pending`; mark it ready when CI is green and the proof is recorded.
- The description starts with `Proof: clip`, `Proof: screenshots`, or `Proof: checks - <why nothing a person runs changed>`, then the headings What problem this solves, User impact, Why this change was made, Evidence, and Excluded. Evidence holds the exact commands with their results and exit status. Write no `Criticality:` line. Set a body with `gh api -X PATCH repos/<owner>/<repo>/pulls/<n> -F body=@file`.
- CodeRabbit applies one tier label: `routine`, `moderate`, or `critical`. Never add or remove a tier label. A person may add `critical`. A change under `.github/workflows/` or of more than 40 files is critical whatever the label says.
- Every pull request follows five steps:
  1. CodeRabbit reviews when the pull request leaves draft, and again only when you post `@coderabbitai review`. Fix only Critical and Major findings, each with a failing test first; Minor and Trivial findings are optional. Batch the fixes, reply on each thread, and never request a review after every push. Review rounds follow the tier label: `routine` gets one review, one batch of fixes, and one confirming review only when PR proof needs the head reviewed; `moderate` and `critical` get one review, one batch of fixes, and one confirming review. Findings on code that fixed an earlier finding count toward the same rounds. After the last round, change no code except for a security or correctness defect that a failing test or a concrete reproduction demonstrates, and list anything left in one pull request comment whose first line starts with `What's left`. The source is the Current standard in https://github.com/dmc-technologies/coderabbit/blob/main/README.md. Never resolve a CodeRabbit thread yourself. CodeRabbit closes what it verifies; it approves a low-risk pull request itself.
  2. CI is green on the head commit.
  3. For a `critical` pull request, stop after the second round. Give each point in the `What's left` comment a reason. PR proof then requests the review once, from the `dmc-developers` team, when that approval is the only thing left. The author then changes nothing. That approval settles the leftovers, except an open `CodeRabbit Security` finding, which blocks on every tier.
  4. An approval of the head from a person who did not do the work is final: not the author, not a commit author, and not an agent account. Anyone may add another reviewer. For `routine` and `moderate`, CodeRabbit's approval is the approval.
  5. When you mark the pull request ready, run `gh pr merge <n> --auto --merge` as yourself. Without write access, ask someone who has it to turn auto-merge on. GitHub merges it once `CI`, `PR proof`, and `CodeRabbit Security` pass on the head and step 4's approval exists. If GitHub reports that auto-merge is not allowed, ask a repository admin to turn on **Allow auto-merge**. A person may merge any pull request that is green and approved. Agents never merge by hand, and nobody uses `gh pr merge --admin`.
- PR proof's refusals name each next step. Full guide: https://github.com/dmc-technologies/coderabbit/blob/main/docs/coderabbit-for-dummies.md. The check: https://github.com/dmc-technologies/agent-ops/blob/main/.github/workflows/pr-proof.yml.
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
