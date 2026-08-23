"""Held-out governance scenarios for F138."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"code_compliance_gap": True}, False),
    (base() | {"life_safety_risk": True}, False),
    (base() | {"accessibility_failure": True}, False),
    (base() | {"structural_system_risk": True}, False),
    (base() | {"mep_coordination_conflict": True}, False),
    (base() | {"site_environmental_gap": True}, False),
    (base() | {"constructability_gap": True}, False),
    (base() | {"provenance_documentation_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F138 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
