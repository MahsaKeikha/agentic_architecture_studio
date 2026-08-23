from AGENTS import code_agent, concept_agent, program_agent, review_agent, systems_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "program": program_agent.run(case),
        "concept": concept_agent.run(case),
        "systems": systems_agent.run(case),
        "code": code_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
