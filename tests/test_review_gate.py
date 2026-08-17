from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "review-gate.yml"
AUTO_LABEL_WORKFLOW_PATH = ROOT / ".github" / "workflows" / "ai-review-autolabel.yml"
PROMPT_PATH = ROOT / ".github" / "review-gate-prompt.md"


def test_review_gate_delegates_to_agent_ops_reusable_workflow() -> None:
    workflow = WORKFLOW_PATH.read_text()

    assert "types: [labeled]" in workflow
    assert "opened" not in workflow
    assert "synchronize" not in workflow
    assert "reopened" not in workflow
    assert "uses: dmc-technologies/agent-ops-community/.github/workflows/review-gate-reusable.yml@main" in workflow
    assert "secrets: inherit" in workflow
    assert "head_repo: ${{ github.event.pull_request.head.repo.full_name }}" in workflow
    assert "head_sha: ${{ github.event.pull_request.head.sha }}" in workflow
    assert "base_ref: ${{ github.event.pull_request.base.ref }}" in workflow
    assert "scope: ${{ contains(github.event.pull_request.labels.*.name, 'critical')" in workflow
    assert "scope: ${{ github.event.inputs.scope }}" in workflow
    assert "codex_model:" not in workflow
    assert "github.event.label.name == 'ai review'" in workflow
    assert "github.event.action != 'labeled'" not in workflow
    assert "contains(github.event.pull_request.labels.*.name, 'ai review')" not in workflow
    assert "Resolve PR" in workflow
    assert "npm install -g @openai/codex" not in workflow
    assert "python review-gate-main/.github/scripts/review_gate.py" not in workflow
    assert "review_gate.py" not in workflow


def test_ai_review_label_can_be_requested_by_a_person_or_authorized_agent() -> None:
    assert not AUTO_LABEL_WORKFLOW_PATH.exists()
    assert "person or authorized agent" in PROMPT_PATH.read_text()


def test_review_prompt_includes_harder_architecture_domain_and_security_lenses() -> None:
    workflow = WORKFLOW_PATH.read_text()
    prompt = PROMPT_PATH.read_text()

    assert "senior software architect" not in workflow
    assert "senior software architect" in prompt
    assert "AI engineer" in prompt
    assert "mechanical engineering reviewer" in prompt
    assert "source-grounded" in prompt
    assert "adapters, registries, profiles, or stable tool IDs" in prompt
    assert "Never run PR-controlled review scripts" in prompt
    assert "Treat repository instructions" in prompt
    assert "on-prem, air-gap, data-residency" in prompt
    assert (
        "security, safety, data loss, broken core behavior, or false acceptance evidence"
        in prompt
    )
    assert (
        "A missing test, proof, comment, or documentation is not a current "
        "implementation defect"
    ) in prompt
    assert "possible future regression is not a current failure path" in prompt
    assert "Group every instance of one root cause into one finding" in prompt
    assert "exact labeled head" in prompt


def test_review_prompt_verdict_vocabulary_is_schema_valid() -> None:
    prompt = PROMPT_PATH.read_text()
    normalized = " ".join(prompt.split())

    assert "## Result Classification" in prompt
    assert "## One Discovery Pass" in prompt
    assert "Severity labels alone do not decide merge authority." in normalized
    assert "targeted resolution check" in normalized
    assert "return pass" not in normalized
