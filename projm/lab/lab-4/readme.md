# Laboratory Work №4

## Topic

Risk Analysis for Project Execution

## Objective

To analyze potential risks based on the Work Breakdown Structure (WBS), Gantt chart, and resource plan of the project, and to understand the importance of risk management in project planning.

## Variant

Молчанов Михайло Валерійович, IA-12, Variant 14\
Mobile banking application (Low complexity) with a project duration of 25 months. Technical characteristics: Support of artificial intelligence for analyzing user behavior.

## Links

- [Report on GitHub](https://github.com/kiIIer/kpi-7/tree/main/projm/lab/lab-4/readme.md)
- [Presentation on YouTube](https://youtu.be/DWesM7_VExA)

## Execution

### Introduction

Every project carries inherent risks that, if left unaddressed, can negatively impact its timeline, budget, or quality. Identifying and managing these risks is an integral part of project planning. Risk analysis allows project managers to foresee potential obstacles, devise mitigation strategies, and allocate resources efficiently.

In this laboratory work, we build upon the Work Breakdown Structure (WBS), Gantt chart, and resource plan created in previous labs to focus on potential risks. These tools provide a clear view of the project's structure, timelines, and resource allocation, making it easier to spot areas prone to delays, technical challenges, or other issues.

### The Importance of Risk Management

Risk management is a proactive approach to handling uncertainties in a project. By considering risks during the planning phase, project managers can reduce the likelihood of surprises that could derail the project. The key benefits of risk analysis include:

- Improved Decision-Making: With a clear understanding of risks, teams can prioritize tasks and allocate resources more effectively.

- Enhanced Preparedness: Identifying risks early allows teams to prepare contingency plans, reducing downtime and project disruptions.

- Budget and Timeline Control: Understanding risks helps in setting realistic budgets and timelines, ensuring that projects are delivered within expectations.

- Stakeholder Confidence: Risk management shows stakeholders that the project is being handled professionally and with foresight, increasing trust in the team's capabilities.

Considering risks in a project of this nature—a mobile banking application with AI functionality—is especially important. The integration of AI introduces technical complexities, while handling sensitive financial data demands rigorous security measures. Proper risk analysis ensures that these challenges are met without compromising the project’s goals or deadlines.

### The Role of WBS, Gantt Chart, and Resource Plan in Risk Analysis

The WBS provides a breakdown of the project into manageable tasks, making it easier to identify specific areas where risks might arise. The Gantt chart adds a temporal dimension, highlighting task dependencies and potential bottlenecks. The resource plan reveals how human and material resources are distributed, pointing out possible conflicts or shortages.

By analyzing these tools together, we gain a comprehensive understanding of the project's vulnerabilities. This foundation enables us to identify and prioritize risks, ensuring that mitigation strategies are implemented where they are needed most.

### Identified Risks for the Project

#### 1. Technical Risks

Technical risks pertain to challenges or failures in the technology stack used in the project. Given the integration of AI and the handling of sensitive banking data, several technical risks could emerge:

- AI Integration Challenges: The complexity of integrating AI modules with the backend may result in issues such as incorrect data processing, misaligned APIs, or inefficient performance.
  - Cause: Lack of proper testing, inadequate communication between backend and AI teams, or unforeseen compatibility issues.
  - Impact: Delays in implementing core features like user behavior analysis or fraud detection.
  - Mitigation: Implement early prototyping and continuous integration pipelines to validate compatibility at each stage. Allocate dedicated resources for thorough testing and debugging.

- Database Performance Issues: With the anticipated high volume of transactional data, the database may face performance bottlenecks or even failures.
  - Cause: Suboptimal query design, poor indexing, or underestimating infrastructure needs.
  - Impact: Slower response times for users and potential downtime.
  - Mitigation: Perform stress testing on the database early in the project lifecycle. Optimize database queries and consider horizontal scaling options.

- Security Breaches: Vulnerabilities in the application could expose sensitive user data.
  - Cause: Inadequate implementation of security protocols like encryption and access control.
  - Impact: Data breaches, reputational damage, and legal consequences.
  - Mitigation: Engage security analysts throughout the development phase and conduct regular penetration testing.

#### 2. Resource Risks

Resource risks arise when there is an imbalance in resource allocation, skill shortages, or over-reliance on key personnel.

- Resource Overload: Overlapping responsibilities, especially between backend and frontend teams, may lead to inefficiencies.
  - Cause: Lack of clear task delegation or unrealistic scheduling.
  - Impact: Missed deadlines and reduced productivity.
  - Mitigation: Use project management tools to track workload distribution and ensure a balanced assignment of tasks.

- Skill Gaps: Teams may lack the necessary expertise in certain domains like AI or advanced security measures.
  - Cause: Limited exposure to specialized technologies.
  - Impact: Delays in implementation and potential quality issues.
  - Mitigation: Provide training programs for team members or hire external consultants to fill knowledge gaps.

#### 3. Schedule Risks

Schedule risks occur when task dependencies or unrealistic deadlines create bottlenecks or cause delays.

- Dependency Bottlenecks: Critical tasks like database setup or API integration could delay other dependent tasks.
  - Cause: Misaligned task scheduling or unforeseen complications in earlier tasks.
  - Impact: Cascading delays throughout the project timeline.
  - Mitigation: Identify and prioritize tasks on the critical path, and allocate buffer time to mitigate delays.

- Underestimated Task Durations: Teams may overestimate their ability to complete tasks within the allocated timeframe.
  - Cause: Limited experience or overly optimistic planning.
  - Impact: Compromised quality due to rushed development or extended timelines.
  - Mitigation: Base estimates on historical data and include contingency time for each task.

#### 4. External Risks

External risks are outside the control of the project team but can significantly impact its progress.

- Tool Reliance: Dependence on third-party tools such as Auth0 or Azure services increases vulnerability to their outages or limitations.
  - Cause: Lack of alternative options or over-reliance on external services.
  - Impact: Disruptions in critical functionalities.
  - Mitigation: Establish fallback mechanisms, such as secondary authentication providers or backup hosting environments.

- Requirement Changes: Stakeholders may introduce changes to the project scope during development.
  - Cause: Evolving business needs or inadequate requirement gathering in the initial phases.
  - Impact: Additional workload, extended timelines, and increased costs.
  - Mitigation: Employ an agile methodology with iterative deliverables to accommodate changing requirements more flexibly.

## Conclusion

The identified risks highlight areas requiring proactive management to ensure project success. By addressing technical, resource, schedule, and external risks early, the project team can minimize potential disruptions and maintain control over the project’s timeline, budget, and quality. This assessment underscores the importance of integrating risk management into every stage of the project lifecycle.
