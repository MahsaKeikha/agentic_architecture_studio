from AGENTS import program_agent,concept_agent,systems_agent,code_agent,review_agent
def run(c): return {'program':program_agent.run(c),'concept':concept_agent.run(c),'systems':systems_agent.run(c),'code':code_agent.run(c),'review':review_agent.run(c)}
