# F138 | Agentic Architecture Studio | L3 Gold Standard | v1.0

A governed five-agent reference architecture for architectural decision support across programming, concept design, site response, building systems, accessibility, code evidence, life safety, sustainability, constructability, coordination, documentation, and qualified architect approval.

F138 can organize project programs, develop architectural concepts, structure building-system coordination, identify code and accessibility questions, trace technical evidence, and prepare professional review packages. It cannot autonomously provide professional signoff, issue documents for construction, certify code compliance, approve structural design, authorize permit submissions, or distribute binding project documents externally.

## Architectural lifecycle

```text
Project Brief, Site, and Program
        -> Concept and Spatial Design
        -> Building Systems and Technical Coordination
        -> Code, Accessibility, Life Safety, and Environmental Review
        -> Constructability and Documentation Review
        -> Qualified Architect Approval
        -> Human-Controlled Permit, Procurement, and Construction Processes
```

The workflow fails closed when required reviews are missing or when material code, life-safety, accessibility, structural, MEP, site, environmental, constructability, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Program Agent | Structures client goals, users, spaces, areas, adjacencies, site requirements, budget assumptions, schedule, and acceptance criteria | What must the project accomplish? |
| Concept Agent | Develops site response, massing, organization, circulation, spatial hierarchy, environmental strategy, and architectural alternatives | What architectural concept best responds to the program and context? |
| Systems Agent | Coordinates structural, envelope, mechanical, electrical, plumbing, fire protection, vertical transportation, technology, and other building systems | Can the architectural concept integrate required building systems coherently? |
| Code Agent | Organizes jurisdictional evidence for zoning, building code, accessibility, occupancy, egress, fire and life safety, and other regulated requirements | What compliance questions and evidence require qualified review? |
| Review Agent | Integrates design quality, technical coordination, constructability, evidence provenance, unresolved risk, and professional approval | Is the package appropriate for qualified architectural review? |

Agents support architects and multidisciplinary project teams. They do not replace licensed architects, structural engineers, civil engineers, MEP engineers, fire-protection engineers, accessibility specialists, geotechnical professionals, environmental consultants, code officials, contractors, surveyors, or authorities having jurisdiction.

## Repository structure

```text
AGENTS/
├── program_agent.py
├── concept_agent.py
├── systems_agent.py
├── code_agent.py
└── review_agent.py

SKILLS/
├── program_reasoning.py
├── concept_reasoning.py
├── systems_reasoning.py
├── code_reasoning.py
└── review_reasoning.py

TOOLS/
├── program_register.py
├── concept_board.py
├── systems_matrix.py
├── code_checklist.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Program architecture

The policy requires `program_reviewed`. Architectural programming should preserve client objectives, user groups, spaces, area targets, adjacency, capacity, privacy, security, accessibility, operational needs, equipment, environmental requirements, budget assumptions, schedule, source, owner, and verification state.

`TOOLS/program_register.py` provides a deterministic surface for structured program information.

## Project brief

The brief should distinguish verified requirements from preferences, assumptions, aspirations, consultant criteria, regulatory constraints, and unresolved questions. The system should not silently convert an aspiration into a requirement or an assumption into a site fact.

## Users

Architecture should respond to actual and anticipated users without assuming a single average body, age, ability, culture, schedule, or mode of use. Relevant needs can include mobility, vision, hearing, cognition, privacy, safety, supervision, security, and caregiving.

## Area program

Area schedules can include net areas, grossing assumptions, circulation, support spaces, service areas, vertical circulation, mechanical space, structural allowances, and site-specific constraints. Area efficiency should not override safety, accessibility, environmental performance, or functional quality.

## Adjacency

Adjacency requirements can be required, preferred, neutral, or undesirable. They can capture operational flow, privacy, security, noise, service access, daylight, public access, clinical or industrial workflows, and other project relationships.

## Site architecture

Architectural concepts should respond to verified site conditions such as property boundaries, easements, topography, access, utilities, orientation, climate, vegetation, neighboring context, hazards, views, noise, and jurisdictional constraints.

`site_environmental_gap` blocks release when critical site, geotechnical, climate, flood, environmental, or existing-condition evidence remains incomplete.

## Survey information

Property boundaries, grades, utilities, easements, existing structures, and other survey-dependent information should come from qualified and current sources. F138 must not invent survey data.

## Geotechnical conditions

Foundations, retaining conditions, settlement, expansive soils, groundwater, liquefaction, slope stability, and other subsurface matters require qualified geotechnical and structural input.

## Climate

Climate response can consider sun, wind, precipitation, temperature, humidity, freeze-thaw conditions, wildfire exposure, storms, daylight, and local microclimate. Applicable design criteria should come from verified sources.

## Flood and water risk

Flood zones, stormwater, drainage, sea-level exposure, groundwater, and site water management can materially affect design. F138 should expose unresolved hazard information rather than assume a site is safe.

## Wildfire and other regional hazards

Projects can require specialized review for wildfire, hurricanes, tornadoes, earthquakes, extreme heat, snow, coastal exposure, or other regional hazards. Hazard requirements are jurisdiction and site specific.

## Concept design

The policy requires `concept_reviewed`. Concept design can explore massing, orientation, spatial organization, circulation, structure, envelope, daylight, outdoor space, landscape relationships, entries, public and private zones, and alternative schemes.

Conceptual work should clearly expose assumptions and unresolved engineering or code dependencies.

## Massing

Massing studies can examine height, setbacks, floor plates, courtyards, towers, podiums, roofs, shadows, views, daylight, context, and program distribution. Zoning and planning requirements require verified jurisdictional evidence.

## Spatial organization

Spatial design can organize public, private, service, secure, quiet, active, clean, dirty, flexible, and specialized zones according to program and project type.

## Circulation

Circulation can include pedestrians, accessible routes, vehicles, bicycles, service, loading, staff, visitors, patients, students, residents, vertical circulation, emergency paths, and security transitions.

## Entries

Entries should consider arrival, accessibility, weather protection, security, identity, queuing, wayfinding, emergency access, service separation, and transitions between public and controlled space.

## Architectural character

Architectural expression can emerge from program, site, climate, materials, structure, culture, history, construction logic, and client identity. F138 should not reproduce protected architectural expression or misrepresent imitation as originality.

## Context

Context review can include scale, street wall, setbacks, landscape, historic patterns, neighboring uses, public realm, cultural meaning, infrastructure, views, and community priorities.

## Historic and cultural resources

Historic buildings, archaeological resources, cultural landscapes, sacred sites, tribal resources, and community heritage can require specialized consultation and regulatory review.

## Accessibility

The policy requires `accessibility_reviewed`. `accessibility_failure` blocks release when material accessibility requirements remain unresolved.

Accessibility can involve site arrival, parking, routes, entrances, doors, elevators, stairs, ramps, restrooms, seating, dwelling units, work areas, counters, signage, controls, clear floor space, turning space, reach, acoustics, and communication features.

F138 does not certify accessibility compliance.

## Universal design

Universal design can improve usability beyond minimum compliance by considering diverse bodies, ages, abilities, sensory conditions, temporary impairments, caregivers, children, and changing needs over time.

## Code evidence

The policy requires `code_evidence_reviewed`. Code records should preserve jurisdiction, adopted edition, amendments, source, relevant section, applicability, interpretation owner, verification date, and unresolved questions.

`code_compliance_gap` blocks release when building, zoning, fire, accessibility, or jurisdictional evidence remains unresolved.

## Zoning and planning

Zoning can govern use, density, floor area, height, setbacks, parking, open space, landscape, signs, historic review, design review, and other land-use matters. Planning approvals can involve discretionary interpretation and public process.

## Building code

Building-code review can involve occupancy, construction type, allowable area and height, mixed occupancies, fire-resistance, exiting, accessibility, interior environment, structural criteria, energy, plumbing, mechanical, electrical, and special conditions.

## Occupancy classification

Occupancy classification can materially affect fire protection, exiting, allowable area, plumbing, accessibility, and construction requirements. Final classification requires qualified code review.

## Construction type

Construction type affects allowable building size, fire resistance, structural materials, exterior walls, and other requirements. F138 can organize evidence but cannot independently certify construction type.

## Life safety

The policy requires `life_safety_reviewed`. `life_safety_risk` blocks release when egress, fire, occupancy, fall, emergency, or other material life-safety concerns remain unresolved.

## Egress

Egress analysis can include occupant load, number of exits, exit access, travel distance, common path, dead ends, door swing, exit separation, stairs, corridors, horizontal exits, areas of refuge, discharge, and accessible means of egress where applicable.

Binding life-safety determinations remain under qualified professional and authority review.

## Fire protection

Architecture can interact with sprinklers, standpipes, fire alarms, smoke control, fire department access, fire command centers, rated assemblies, fire doors, penetrations, shafts, hazardous areas, and suppression systems.

## Fire-resistance assemblies

Rated walls, floors, roofs, shafts, doors, glazing, joints, and penetrations depend on tested or approved assemblies and project-specific conditions. F138 should preserve assembly evidence rather than infer ratings from appearance.

## Structural systems

The policy requires `systems_reviewed`. Structural concepts can include gravity systems, lateral systems, grids, spans, foundations, transfer conditions, movement joints, long-span elements, and coordination zones.

`structural_system_risk` blocks release when structural concept, loading, stability, or engineering dependencies remain unresolved.

`approve_structural_design` is protected.

## Seismic design

Seismic requirements depend on site, building, occupancy, structural system, soil, jurisdiction, and engineering analysis. F138 can surface dependencies but cannot perform professional structural approval.

## Wind and snow

Wind and snow criteria can affect structure, cladding, roofs, attachments, drainage, and operations. Design values should come from verified engineering and code sources.

## Building envelope

Envelope design can involve walls, roofs, glazing, waterproofing, air barriers, vapor control, insulation, thermal bridging, drainage, flashing, condensation, movement, durability, and interfaces.

## Water management

Buildings should manage bulk water through appropriate site drainage, roofs, walls, openings, transitions, and below-grade systems. Detailed assemblies require climate, material, and construction-specific review.

## Moisture

Moisture problems can affect durability, indoor conditions, materials, structure, and health. F138 should not conceal unresolved condensation, leakage, groundwater, or drying concerns behind visual design.

## Mechanical systems

Architectural design should coordinate HVAC equipment, shafts, ducts, louvers, ventilation, exhaust, plant rooms, service access, controls, ceiling zones, noise, and outdoor equipment.

## Electrical systems

Coordination can include utility service, electrical rooms, panels, transformers, generators, emergency power, lighting, controls, receptacles, equipment, vertical distribution, and clearances.

## Plumbing systems

Coordination can include fixture counts, wet stacks, restrooms, kitchens, equipment, roof drainage, stormwater, domestic water, sanitary systems, service spaces, and accessibility.

## Fire-protection systems

Fire-protection coordination can affect risers, pumps, tanks, sprinklers, standpipes, fire department connections, alarms, smoke control, and spatial clearances.

## Vertical transportation

Elevators, escalators, lifts, stairs, and service lifts can affect accessibility, egress, structure, equipment rooms, pits, overhead, power, fire service, and circulation.

## Technology systems

Architecture can coordinate data, audiovisual systems, security, access control, surveillance, Wi-Fi, sensors, building controls, communications, and equipment rooms while respecting privacy and security requirements.

## MEP coordination

`mep_coordination_conflict` blocks release when mechanical, electrical, plumbing, fire-protection, or other building-system conflicts remain unresolved.

`TOOLS/systems_matrix.py` provides a deterministic surface for tracking interfaces and responsibilities.

## Coordination zones

Ceilings, shafts, risers, corridors, roofs, equipment rooms, facades, structure, and below-grade areas often contain dense system interfaces. Space reservations should be explicit early enough to avoid hidden conflicts.

## Sustainability

Architectural sustainability can consider operational energy, embodied carbon, water, site ecology, resilience, durability, adaptability, passive design, material impacts, transportation, and occupant experience.

Claims should be evidence-backed and should distinguish design intent from verified performance.

## Energy

Energy performance can depend on climate, envelope, glazing, orientation, systems, controls, occupancy, plug loads, schedules, commissioning, and operations. Simulation assumptions should be documented.

## Passive design

Passive strategies can include orientation, shading, daylight, natural ventilation where appropriate, thermal mass, insulation, envelope optimization, and climate-responsive form. Their effectiveness requires project-specific analysis.

## Embodied carbon

Embodied-carbon analysis can include structure, envelope, finishes, site materials, product quantities, service life, replacements, transportation, and end-of-life assumptions. Data provenance matters.

## Water

Water strategies can include efficient fixtures, rainwater, graywater where permitted, irrigation, landscape, cooling, process loads, stormwater, and leak detection.

## Resilience

Resilience planning can consider heat, smoke, storms, flooding, outages, seismic events, wildfire, water disruption, sheltering, backup power, passive survivability, and recovery.

## Healthy-building claims

Daylight, acoustics, air quality, materials, thermal comfort, and access to nature can influence occupant experience. F138 should not make medical or health claims beyond supporting evidence.

## Materials

Architectural material selection can consider structure, fire performance, durability, weathering, moisture, maintenance, emissions, sourcing, appearance, cost, availability, installation, repair, and end-of-life.

## Product evidence

Technical product claims should preserve manufacturer, model, source, date, tested performance, certification where relevant, limitations, substitutions, and approval state.

## Facades

Facade design requires coordination among architecture, structure, waterproofing, thermal performance, glazing, fire safety, movement, maintenance, access, fabrication, and installation.

## Roofs

Roof design can involve drainage, overflow, slopes, membranes, insulation, equipment, access, fall protection, solar systems, snow, wind, fire classification, penetrations, and maintenance.

## Doors and windows

Openings can affect egress, accessibility, security, acoustics, fire rating, weather resistance, thermal performance, daylight, hardware, structure, and maintenance.

## Stairs and ramps

Stairs, ramps, guards, handrails, landings, headroom, width, rise and run, accessibility, and egress requirements are safety-critical and require qualified verification.

## Parking and mobility

Site and building design can include accessible parking, bicycle facilities, EV charging, drop-off, loading, transit connections, pedestrian safety, service circulation, and emergency access.

## Landscape interface

Architecture and landscape should coordinate grading, drainage, accessible routes, planting, irrigation, utilities, structures, lighting, fire considerations, and public realm.

## Public realm

Buildings shape streets, sidewalks, plazas, entries, shade, frontage, safety, accessibility, and neighborhood experience. Public-space requirements may involve multiple agencies.

## Security

Security design can include access control, visibility, perimeter, entries, secure zones, emergency operations, technology, and operational procedures. Sensitive security information should be access controlled.

## Privacy

Residential, healthcare, workplace, education, and other environments can require visual, acoustic, informational, and operational privacy. Technology systems can add privacy risks.

## Constructability

The policy requires `constructability_reviewed`. `constructability_gap` blocks release when material sequencing, tolerances, access, installation, coordination, temporary conditions, or documentation issues remain unresolved.

Constructability review should involve contractors and relevant trades where appropriate.

## Tolerances

Real construction includes tolerances, deflection, material movement, fabrication variation, installation access, and sequencing. Details should not depend on impossible precision.

## Sequencing

Construction sequence can affect structure, enclosure, waterproofing, fire protection, temporary support, access, testing, and commissioning. F138 should surface sequence-sensitive interfaces.

## Maintenance access

Equipment, roofs, facades, valves, filters, dampers, panels, lighting, and other systems require safe maintenance access. Design should account for long-term operations, not only initial appearance.

## Cost

Cost planning should identify scope, source, date, quantity assumptions, escalation, contingency, exclusions, procurement method, and uncertainty. F138 does not make binding financial commitments.

## Value engineering

Value engineering should evaluate function, life-cycle impact, performance, safety, accessibility, durability, energy, maintenance, and design intent rather than treating lowest initial cost as the only objective.

## Schedule

Project schedules can track design phases, consultant milestones, approvals, permits, procurement, long-lead items, construction, commissioning, and occupancy. Authority and vendor timelines should not be represented as guaranteed without confirmation.

## BIM

Building information models can coordinate geometry, systems, quantities, properties, issues, and documentation. Model presence does not guarantee accuracy, code compliance, or constructability.

## Model coordination

Clash detection can identify geometric conflicts but can miss access, sequencing, tolerance, code, maintenance, performance, and operational conflicts. Human multidisciplinary review remains necessary.

## Level of development

Model elements should communicate their intended level of development and reliability. Conceptual geometry should not be treated as fabrication-ready information.

## Drawings

Architectural documentation can include site plans, floor plans, reflected ceiling plans, roof plans, elevations, sections, details, schedules, diagrams, and specifications.

F138 can organize information but cannot autonomously create professionally authorized construction documents.

## Specifications

Specifications can define products, performance, execution, quality, testing, submittals, substitutions, and closeout requirements. Technical requirements should be coordinated with drawings and consultant documents.

## Drawing coordination

Plans, sections, elevations, details, schedules, specifications, consultant documents, and models should tell a consistent story. Conflicts should be logged rather than silently resolved.

## Permit submissions

`authorize_permit_submission` is protected. Permit packages require qualified professional review, client authorization, and applicable signatures, seals, forms, and jurisdictional procedures.

## Professional signoff

`professional_signoff` is protected. F138 cannot stamp, seal, sign, certify, or otherwise represent AI-generated output as professional architectural approval.

## Issue for construction

`issue_for_construction` is protected. Internal governance approval does not make a package suitable or authorized for construction.

## Code approval

`approve_code_compliance` is protected. Final code interpretation and acceptance belong to qualified professionals and authorities having jurisdiction.

## Construction administration

Construction-phase services can include submittals, RFIs, site observations, payment review, change orders, punch lists, closeout, and interpretation of contract documents. Binding actions require authorized project professionals.

## RFIs

Requests for information should preserve question, drawing or specification reference, responsible discipline, impact, response, approval, and resulting changes.

## Submittals

Shop drawings, product data, samples, mockups, and delegated-design documents can require review for design intent and coordination. F138 cannot replace regulated professional review.

## Changes

Architectural changes should preserve initiator, reason, affected requirements, drawings, models, systems, code, accessibility, cost, schedule, approvals, and supersession state.

## Field conditions

Actual construction and existing conditions can differ from drawings. Field verification, testing, observation, and professional judgment remain necessary.

## Commissioning

Building-system commissioning can verify installation, controls, sequences, performance, and documentation. F138 can track requirements and issues but does not certify commissioning results.

## Occupancy and handover

Occupancy can depend on inspections, approvals, life-safety systems, accessibility, commissioning, training, closeout documents, and authority requirements. F138 cannot authorize occupancy.

## Existing buildings

Renovation projects can involve concealed conditions, hazardous materials, undocumented modifications, historic construction, structural limitations, accessibility upgrades, and code triggers.

## Hazardous materials

Asbestos, lead, contaminated soil, mold, PCBs, and other hazards require qualified assessment, testing, abatement, and regulatory processes.

## Adaptive reuse

Adaptive reuse can create conflicts among existing structure, new occupancy, accessibility, fire safety, energy, preservation, and modern building systems. These tradeoffs require multidisciplinary review.

## Healthcare architecture

Healthcare projects can involve clinical workflows, infection prevention, medical gases, imaging, patient safety, behavioral health, privacy, specialized codes, and accreditation requirements. Specialist review is essential.

## Residential architecture

Residential projects can involve accessibility, privacy, fire safety, energy, structure, site constraints, kitchens, bathrooms, aging in place, and local zoning.

## Educational architecture

Schools can involve age-specific safety, supervision, accessibility, acoustics, daylight, security, technology, assembly spaces, and educational requirements.

## Workplace architecture

Workplaces can involve occupancy, accessibility, egress, acoustics, privacy, technology, hybrid work, wellness goals, security, and organizational change.

## Hospitality architecture

Hotels and hospitality projects can involve guest rooms, assembly, food service, accessibility, fire safety, back-of-house operations, acoustics, security, and brand requirements.

## Civic and public architecture

Public projects can involve procurement rules, accessibility, public process, security, resilience, community engagement, cultural context, and multiple agency approvals.

## Industrial and laboratory architecture

Industrial and laboratory projects can involve hazardous materials, process systems, ventilation, containment, equipment loads, fire protection, emergency systems, utilities, and specialized regulations.

## Data centers and critical facilities

Critical facilities can require redundancy, resilience, security, power, cooling, fire protection, maintenance access, structural criteria, and operational continuity. Detailed infrastructure information may be security sensitive.

## Community engagement

Architecture can affect communities beyond the client. Engagement should accurately represent project status, constraints, alternatives, and feedback rather than using generated narratives as substitutes for actual participation.

## Environmental review

Projects can require environmental assessment, impact review, habitat studies, traffic studies, cultural-resource review, noise analysis, or other regulatory processes. F138 can organize evidence but cannot perform regulatory certification.

## Provenance

`provenance_documentation_gap` blocks release when material code, site, product, research, or technical source provenance is incomplete.

The system must never fabricate code provisions, survey information, engineering calculations, test reports, environmental findings, product certifications, permit status, or professional approvals.

## Confidentiality

Unreleased developments, residential addresses, security layouts, critical infrastructure, proprietary drawings, client financial information, and building-system details can be sensitive. Access should follow project need and authorization.

## Memory and state

The `memory/` layer can preserve program, site evidence, design options, system decisions, code references, accessibility findings, coordination issues, constructability state, versions, approvals, and unresolved risks.

It should distinguish verified information, assumptions, proposals, rejected alternatives, and superseded records.

## Observability

The `observability/` layer supports traceability across program, concept, systems, code, accessibility, life safety, constructability, provenance, and governance.

Useful telemetry includes package version, unresolved program requirements, site evidence gaps, code questions, system conflicts, structural dependencies, accessibility findings, constructability issues, approvals, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
program_reviewed
concept_reviewed
systems_reviewed
accessibility_reviewed
life_safety_reviewed
code_evidence_reviewed
constructability_reviewed
qualified_architect_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- building, zoning, fire, accessibility, or jurisdictional code evidence is unresolved
- material life-safety risks remain unresolved
- accessibility requirements remain unresolved
- structural concept, loading, stability, or engineering dependencies remain unresolved
- MEP, fire-protection, or building-system conflicts remain unresolved
- critical site, geotechnical, climate, flood, environmental, or existing-condition evidence is incomplete
- material constructability, sequencing, tolerance, access, or documentation issues remain unresolved
- code, site, product, research, or technical source provenance is incomplete
- any required review is missing
- qualified architect approval is missing

The system exposes blockers rather than manufacturing compliance, engineering adequacy, constructability, permit readiness, or professional approval.

## Protected actions

The safety policy permanently protects:

```text
professional_signoff
issue_for_construction
approve_code_compliance
approve_structural_design
authorize_permit_submission
external_distribution
```

These remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F138 must not autonomously stamp or seal documents, certify code or accessibility compliance, approve structural or engineering design, authorize permit submission, issue construction documents, approve construction, authorize occupancy, or distribute binding project information externally.

Qualified professionals retain control over regulated architecture, engineering, code interpretation, accessibility, life safety, permits, procurement, construction, commissioning, and occupancy decisions.

## Explicit failure states

```text
PROGRAM REVIEW REQUIRED
CONCEPT REVIEW REQUIRED
SYSTEMS REVIEW REQUIRED
ACCESSIBILITY REVIEW REQUIRED
LIFE SAFETY REVIEW REQUIRED
CODE EVIDENCE REVIEW REQUIRED
CONSTRUCTABILITY REVIEW REQUIRED
QUALIFIED ARCHITECT APPROVAL REQUIRED
CODE COMPLIANCE GAP
LIFE SAFETY RISK
ACCESSIBILITY FAILURE
STRUCTURAL SYSTEM RISK
MEP COORDINATION CONFLICT
SITE OR ENVIRONMENTAL EVIDENCE GAP
CONSTRUCTABILITY GAP
PROVENANCE DOCUMENTATION GAP
PROFESSIONAL SIGNOFF PROHIBITED
ISSUE FOR CONSTRUCTION PROHIBITED
AUTONOMOUS CODE APPROVAL PROHIBITED
AUTONOMOUS STRUCTURAL APPROVAL PROHIBITED
AUTONOMOUS PERMIT SUBMISSION PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Capture client goals, user groups, site information, area program, adjacency, budget assumptions, schedule, and approval owners.
2. Register survey, zoning, environmental, geotechnical, climate, utility, and existing-condition evidence with verification state.
3. Develop alternative concepts for massing, orientation, organization, circulation, structure, envelope, and environmental response.
4. Coordinate architectural concepts with structural, mechanical, electrical, plumbing, fire-protection, vertical-transportation, technology, and site systems.
5. Review accessibility, zoning, occupancy, construction type, egress, fire and life safety, and jurisdictional code evidence.
6. Evaluate envelope, energy, water, materials, resilience, maintenance, and sustainability strategies with traceable assumptions.
7. Review constructability, tolerances, sequencing, access, BIM coordination, drawing consistency, and unresolved field dependencies.
8. Preserve source provenance for code, site, engineering, product, environmental, and technical evidence.
9. Track changes, consultant interfaces, approvals, unresolved risks, and superseded information.
10. Apply fail-closed governance and require qualified architect approval.
11. Keep professional signoff, code certification, structural approval, permit authorization, issue-for-construction authority, and external distribution outside autonomous control.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test program completeness, concept traceability, system coordination, code-evidence discipline, accessibility awareness, life-safety escalation, constructability awareness, provenance, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, code gaps, life-safety risk, accessibility failure, structural risk, MEP conflicts, site or environmental evidence gaps, constructability gaps, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible architectural review requires preserving program version, site evidence, survey state, design options, system assumptions, code references, accessibility findings, structural dependencies, consultant coordination, constructability findings, drawings, models, approvals, and unresolved risks.

## Extension points

Organization-specific implementations can add governed integrations for BIM and CAD systems, GIS, code research, product databases, specifications, energy modeling, carbon analysis, issue tracking, clash detection, project management, document control, and field platforms.

Any integration capable of changing binding project records, submitting permits, approving compliance, issuing documents, or distributing sensitive construction information should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include architectural programming, site and zoning research, concept option studies, residential design support, workplace and healthcare planning, educational facilities, hospitality, civic buildings, adaptive reuse, system coordination, code checklists, accessibility review, sustainability studies, BIM issue tracking, and constructability review.

F138 is not an autonomous architect, engineer, surveyor, code official, accessibility certifier, environmental consultant, contractor, permit authority, commissioning authority, or construction administrator.

## Design principles

1. Begin with verified program, site, user, jurisdiction, and project constraints.
2. Keep architectural concepts traceable to requirements and known evidence.
3. Treat structure, envelope, MEP, accessibility, life safety, environment, cost, and constructability as integrated design concerns.
4. Never fabricate survey data, code provisions, engineering results, product performance, environmental findings, permit status, or professional approvals.
5. Preserve source provenance and distinguish verified facts from assumptions and proposals.
6. Surface multidisciplinary conflicts instead of hiding them.
7. Treat models and visualizations as representations whose reliability depends on documented development state.
8. Fail closed when safety, accessibility, code evidence, engineering dependencies, site information, constructability, provenance, or approval is incomplete.
9. Keep regulated professional decisions, permits, construction authorization, and external distribution under qualified human control.

## Scope statement

F138 demonstrates a governed multi-agent architecture for architectural decision support. It combines specialized program, concept, systems, code, and review agents with deterministic program, concept, systems, code, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over professional signoff, engineering, compliance, permits, construction, and external distribution.

Author: Mahsa Keikha
