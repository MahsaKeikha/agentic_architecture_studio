"""Fail-closed governance for F138 Agentic Architecture Studio."""

PROTECTED_ACTIONS = {
    "professional_signoff",
    "issue_for_construction",
    "approve_code_compliance",
    "approve_structural_design",
    "authorize_permit_submission",
    "external_distribution",
}

REQUIRED_REVIEWS = (
    "program_reviewed",
    "concept_reviewed",
    "systems_reviewed",
    "accessibility_reviewed",
    "life_safety_reviewed",
    "code_evidence_reviewed",
    "constructability_reviewed",
    "qualified_architect_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding professional, construction, compliance, permit, or distribution action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required architecture review", "missing": missing}
    checks = {
        "code_compliance_gap": "building, zoning, fire, accessibility, or jurisdictional code evidence unresolved",
        "life_safety_risk": "egress, fire, occupancy, fall, emergency, or other life-safety risk unresolved",
        "accessibility_failure": "material accessibility requirement unresolved",
        "structural_system_risk": "structural concept, loading, stability, or engineering dependency unresolved",
        "mep_coordination_conflict": "mechanical, electrical, plumbing, fire-protection, or building-system conflict unresolved",
        "site_environmental_gap": "critical site, geotechnical, climate, flood, environmental, or existing-condition evidence incomplete",
        "constructability_gap": "material constructability, sequencing, tolerance, access, or documentation issue unresolved",
        "provenance_documentation_gap": "material code, site, product, research, or technical source provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "architecture governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "architecture support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
