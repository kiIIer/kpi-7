# Laboratory Work №5

## Topic

Service Level Agreement (SLA) and Contingency Plan for Risk Management

## Objective

To develop a detailed Service Level Agreement (SLA) and contingency plan to mitigate and manage risks identified in Laboratory Work №4, ensuring minimal disruption and timely recovery in the event of risk materialization.

## Variant

Молчанов Михайло Валерійович, IA-12, Variant 14\
Mobile banking application (Low complexity) with a project duration of 25 months. Technical characteristics: Support of artificial intelligence for analyzing user behavior.

## Links

- [Report on GitHub](https://github.com/kiIIer/kpi-7/tree/main/projm/lab/lab-5/readme.md)
- [Presentation on YouTube](https://youtu.be/af3GR0OnU5w)

## Execution

### Introduction

In this laboratory work, we address the risks identified in Laboratory Work №4 by creating a detailed Service Level Agreement (SLA) and contingency plan. These plans provide a structured approach to handling risks that might disrupt the development of a mobile banking application. Given the sensitive nature of banking systems and the inclusion of AI, this document ensures preparedness and accountability for handling technical, resource, schedule, and external risks.

### SLA and Contingency Plan

#### Technical Risks

##### AI Integration Challenges

- Trigger: The AI module produces incorrect outputs or fails to integrate with the backend API.
- Immediate Action:
  - Halt all dependent tasks.
  - Notify the Senior AI Engineer and Project Manager immediately.
- Roles and Responsibilities:
  - Senior AI Engineer: Debug and validate model outputs.
  - Backend Team: Ensure backend APIs are correctly implemented and provide simulated data for testing.
  - Project Manager: Adjust timelines and inform stakeholders.
- Recovery Plan:
  - Use a simplified fallback model for immediate operations.
  - Conduct joint debugging sessions between the AI and backend teams.
  - Schedule additional testing iterations to validate outputs.
- Post-Risk Assessment:
  - Document the root cause of integration failure.
  - Develop better testing frameworks for future integration phases.

##### Database Performance Issues

- Trigger: The database experiences query slowdowns, timeouts, or crashes during peak loads.
- Immediate Action:
  - Shift traffic to a read-replica database if available.
  - Notify the Database Administrator (DBA) and DevOps Engineer.
- Roles and Responsibilities:
  - DBA: Analyze query logs and optimize slow queries.
  - DevOps Engineer: Scale up database instances or introduce caching mechanisms.
  - Project Manager: Reassess task timelines and inform stakeholders of delays.
- Recovery Plan:
  - Enable database sharding or horizontal scaling.
  - Introduce caching for frequently accessed data.
  - Perform extensive load testing to identify bottlenecks.
- Post-Risk Assessment:
  - Update database design with performance optimizations.
  - Include database stress testing in future development cycles.

##### Security Breaches

- Trigger: Unauthorized access to sensitive user data or system vulnerabilities exploited.
- Immediate Action:
  - Isolate affected systems to prevent further damage.
  - Notify the Security Analyst and initiate a security audit.
  - Inform legal teams if the breach involves user data.
- Roles and Responsibilities:
  - Security Analyst: Identify and patch vulnerabilities.
  - Legal Team: Handle communication with affected users and ensure regulatory compliance.
  - Project Manager: Coordinate with all teams and manage stakeholder communication.
- Recovery Plan:
  - Deploy updated security patches.
  - Enhance monitoring systems to detect future intrusions.
  - Implement stricter access controls and two-factor authentication (2FA).
- Post-Risk Assessment:
  - Conduct a post-mortem analysis of the breach.
  - Update security protocols and employee training.

#### Resource Risks

##### Resource Overload

- Trigger: Teams report delays or reduced productivity due to overlapping or excessive responsibilities.
- Immediate Action:
  - Review team workloads and reassign tasks to alleviate pressure.
  - Notify the Project Manager of resource bottlenecks.
- Roles and Responsibilities:
  - Team Leads: Provide updates on team capacities.
  - Project Manager: Adjust task assignments and allocate additional resources if needed.
- Recovery Plan:
  - Hire temporary contractors or consultants to fill gaps.
  - Delay non-critical tasks to allow teams to focus on immediate priorities.
- Post-Risk Assessment:
  - Improve task allocation processes and resource planning for future phases.

##### Skill Gaps

- Trigger: Teams lack the required skills to complete certain tasks, such as AI model implementation or database optimization.
- Immediate Action:
  - Identify tasks requiring expertise and notify the Project Manager.
  - Consult with external experts if internal solutions are unavailable.
- Roles and Responsibilities:
  - Project Manager: Arrange training sessions or hire external consultants.
  - Team Leads: Evaluate current skill levels and recommend training needs.
- Recovery Plan:
  - Partner with vendors for on-demand expertise.
  - Schedule training programs for team members.
- Post-Risk Assessment:
  - Include upskilling initiatives in resource planning.
  - Maintain a directory of external consultants for future needs.

#### Schedule Risks

##### Dependency Bottlenecks

- Trigger: A delay in one task (e.g., database setup) affects multiple dependent tasks.
- Immediate Action:
  - Identify alternative workflows or interim solutions.
  - Notify the affected teams and adjust timelines.
- Roles and Responsibilities:
  - Project Manager: Reprioritize tasks and communicate new timelines.
  - Team Leads: Ensure tasks proceed where possible without dependency resolution.
- Recovery Plan:
  - Use placeholder data or simulated environments to continue progress.
  - Reallocate resources to non-dependent tasks.
- Post-Risk Assessment:
  - Strengthen dependency analysis during planning stages.
  - Allocate buffer time for critical tasks in future schedules.

##### Underestimated Timelines

- Trigger: Teams report consistent delays due to unrealistic initial estimates.
- Immediate Action:
  - Notify the Project Manager to reassess project milestones.
  - Realign priorities based on team feedback.
- Roles and Responsibilities:
  - Project Manager: Revise timelines and negotiate extended deadlines with stakeholders.
  - Teams: Provide updated estimates for incomplete tasks.
- Recovery Plan:
  - Use agile sprints to deliver incremental progress.
  - Communicate updated schedules transparently to stakeholders.
- Post-Risk Assessment:
  - Refine estimation techniques with input from historical data.

#### External Risks

##### Tool Reliance

- Trigger: Third-party tools or services such as Auth0 or Azure experience outages or limitations.
- Immediate Action:
  - Switch to backup tools or workflows where possible.
  - Notify affected teams and stakeholders of potential delays.
- Roles and Responsibilities:
  - DevOps Engineer: Implement failover strategies and alternative configurations.
  - Project Manager: Coordinate communication and resource reallocation.
- Recovery Plan:
  - Develop in-house solutions as temporary replacements.
  - Negotiate SLA agreements with vendors for quicker recovery.
- Post-Risk Assessment:
  - Diversify dependencies to reduce reliance on single providers.

##### Requirement Changes

- Trigger: Stakeholders introduce new requirements or change project scope mid-development.
- Immediate Action:
  - Evaluate the feasibility and impact of new requirements.
  - Communicate changes to all affected teams.
- Roles and Responsibilities:
  - Project Manager: Assess impacts and renegotiate deadlines or budgets.
  - Teams: Adjust task plans based on updated requirements.
- Recovery Plan:
  - Implement changes in iterative stages to minimize disruptions.
  - Document all changes to ensure alignment with initial goals.
- Post-Risk Assessment:
  - Conduct requirement-gathering workshops to improve initial scoping.

## Conclusion

This SLA and contingency plan provide a structured framework for addressing the risks identified in the project. By defining triggers, immediate actions, roles, and recovery measures for each risk type, the plan ensures that the team is prepared to respond effectively. Regular reviews and updates to the SLA will further enhance its relevance and effectiveness, enabling the successful delivery of the mobile banking application.
