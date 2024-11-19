# Laboratory Work №2

## Topic

Creating a Work Breakdown Structure (WBS) for the Project

## Objective

To thoughtfully plan and create a Work Breakdown Structure (WBS) for the project based on the given variant.

## Variant

Молчанов Михайло Валерійоич, IA-12, Variant 14  
Mobile banking application (Low complexity) with a project duration of 25 months. Technical characteristics: Support of artificial intelligence for analyzing user behavior.

## Links

- [Report on GitHub](https://github.com/kiIIer/kpi-7/tree/main/projm/lab/lab-2/readme.md)
- [Presentation on YouTube](https://youtu.be/zy1cZqTn0hM)
- [Excel Spreadsheet on Google Drive](https://docs.google.com/spreadsheets/d/12L4fTINkNx-vud7qh2VTWJFWEJ4sadvb/edit?usp=sharing&ouid=108706181521622783833&rtpof=true&sd=true)

## Execution

### Project Overview

The project involves developing a Mobile Banking Application of low complexity with a project duration of 25 months. The application will feature Artificial Intelligence (AI) support for analyzing user behavior. The primary goal is to create a secure, efficient, and user-friendly mobile application that enhances banking services through personalization and advanced security measures provided by AI integration.

### Project Objectives

- Security: Ensure robust data protection and compliance with industry security standards.
- Performance: Optimize infrastructure to minimize transaction processing times.
- Accessibility: Provide cross-platform compatibility for both iOS and Android devices.
- AI Integration: Utilize AI technologies to analyze transactions and personalize user services.

### Use of Cloud Technologies

Given the need for handling large volumes of data and ensuring high availability, the project will leverage cloud services on the Microsoft Azure platform.

- Infrastructure in the Cloud:
  - Kubernetes: Employ Azure Kubernetes Service (AKS) for container orchestration, facilitating easy scaling and management of microservices.
  - Terraform: Use Infrastructure as Code (IaC) with Terraform to automate the creation and updating of Azure resources efficiently.
  - Auth0: Implement Auth0 for authentication and authorization, integrating multi-factor authentication to enhance security.

### Architectural Aspects

1. Frontend (Client Side):
   - Develop an intuitive and user-friendly interface.
   - Utilize modern frameworks like React Native for cross-platform development.

2. Backend (Server Side):
   - Implement robust APIs to handle client requests.
   - Integrate with a relational database system, such as PostgreSQL.
   - Develop AI modules for data analysis and personalization.

3. AI Modules:
   - Analyze transaction data to detect suspicious activities.
   - Personalize service recommendations (e.g., credit products).
   - Use Python-based libraries like TensorFlow or PyTorch for AI development.

### Project Phases

The project is divided into several phases to organize work effectively and ensure a logical progression from inception to completion.

#### 1. Initiation Phase

Objective: Establish the project's foundation by defining objectives, requirements, and initial planning.

- Stakeholder Engagement:
  - Conduct meetings to define the main product requirements.
  - Agree on functional and non-functional requirements.
  - Develop a project roadmap outlining milestones and deliverables.

- Project Structuring:
  - Create technical documentation detailing system requirements.
  - Plan the system architecture, including technology stack decisions.
  - Set up the cloud infrastructure using Azure, Kubernetes, Terraform, and Auth0.
  - Prepare UI/UX designs and wireframes for the application interface.

Reason for Order: This phase is crucial for aligning all stakeholders and team members on the project's goals and scope. Establishing clear requirements and a solid architectural plan prevents misunderstandings and sets a strong foundation for subsequent development activities.

#### 2. Development Phase

Objective: Build all components of the mobile application, including frontend, backend, and AI modules.

- Backend Development:
  - Develop backend logic and RESTful APIs to handle business processes and data management.
  - Ensure secure integration with the cloud infrastructure.
  - Implement authentication and authorization using Auth0.

- Frontend Development:
  - Implement the user interface based on UI/UX designs.
  - Develop the mobile application using React Native for cross-platform support.
  - Integrate frontend components with backend services through APIs.

- AI Development and Integration:
  - Design and train AI models to analyze user behavior.
  - Test AI models to ensure accuracy and efficiency.
  - Integrate AI functionalities into the backend services.

- Initial Testing:
  - Perform unit testing for individual components to identify and fix bugs early.
  - Conduct integration testing to ensure different components work together seamlessly.

Reason for Order: Development follows the initiation phase as it builds upon the established plans and designs. By structuring development into backend, frontend, and AI components, the team can work in parallel while maintaining focus on their specific areas, leading to efficient progress.

#### 3. Stabilization and User Acceptance Testing (UAT)

Objective: Ensure the application is stable, secure, and meets user expectations before deployment.

- System Stabilization:
  - Optimize application performance by refining code and server configurations.
  - Resolve any bugs identified during initial testing.
  - Validate AI integration and the accuracy of AI models.

- Security Assessments:
  - Conduct thorough security audits to identify vulnerabilities.
  - Implement security enhancements based on audit findings.
  - Ensure compliance with industry regulations like PCI DSS and GDPR.

- User Acceptance Testing (UAT):
  - Engage a group of end-users to test the application in real-world scenarios.
  - Collect feedback on usability, functionality, and performance.
  - Make necessary adjustments based on user feedback to improve the application.

- Preparation for Launch:
  - Finalize all documentation, including user manuals and technical guides.
  - Deploy the application to the production environment on Azure.

Reason for Order: Stabilization and UAT are essential before launch to ensure the application is reliable and user-friendly. Addressing security and compliance at this stage mitigates risks and builds user trust. Gathering user feedback allows for final adjustments that enhance the overall quality of the application.

#### 4. Deployment and Launch

Objective: Release the application to the market and ensure a smooth transition to the operational phase.

- Production Deployment:
  - Deploy the application using Kubernetes clusters for scalability.
  - Configure monitoring and logging for ongoing performance tracking.
  - Submit the application to app stores (Apple App Store and Google Play Store).

- Post-Launch Monitoring:
  - Monitor application performance and user feedback closely after launch.
  - Quickly address any critical issues that arise to maintain user satisfaction.

Reason for Order: Deployment follows successful testing and stabilization, marking the transition from development to operation. Monitoring post-launch ensures any unforeseen issues are promptly managed, maintaining the application's reliability and reputation.

#### 5. Post-Launch Support and Maintenance

Objective: Provide ongoing support to users and continuously improve the application based on feedback and performance data.

- Bug Fixing and Updates:
  - Regularly update the application to fix bugs and improve features.
  - Implement enhancements based on user feedback and technological advancements.

- Performance Optimization:
  - Continuously monitor system performance and make optimizations as needed.
  - Scale infrastructure resources in response to user growth and demand.

- Technical Support:
  - Offer support services to assist users experiencing issues.
  - Maintain high levels of user satisfaction and trust.

Reason for Order: Ongoing support is vital for the application's long-term success. It ensures the application remains relevant, secure, and efficient, adapting to changing user needs and technological landscapes.

#### 6. Project Closure

Objective: Officially conclude the project, document outcomes, and release resources.

- Documentation Finalization:
  - Compile all project documentation, including technical specs, user guides, and compliance records.
  - Document lessons learned and best practices identified during the project.

- Team Release:
  - Release project team members from their project roles.
  - Recognize team contributions and provide feedback for professional development.

- Contract Closure:
  - Finalize any outstanding contracts and agreements.
  - Ensure all legal and financial obligations are met.

Reason for Order: Formal closure provides a clear endpoint for the project, allowing resources to be reallocated efficiently. Documenting the project's outcomes and lessons learned contributes to organizational knowledge and improves future project executions.

### Work Breakdown Structure (WBS)

The WBS is organized hierarchically to break down the project into manageable sections, ensuring clarity in task assignments and timelines.

1. Initiation Phase
   - Stakeholder Engagement
   - Project Structuring

2. Development Phase
   - Backend Development
   - Frontend Development
   - AI Development and Integration
   - Initial Testing

3. Stabilization and UAT
   - System Stabilization
   - Security Assessments
   - User Acceptance Testing
   - Preparation for Launch

4. Deployment and Launch
   - Production Deployment
   - Post-Launch Monitoring

5. Post-Launch Support and Maintenance
   - Bug Fixing and Updates
   - Performance Optimization
   - Technical Support

6. Project Closure
   - Documentation Finalization
   - Team Release
   - Contract Closure

Explanation of Order:

- Logical Progression: The sequence follows the natural flow of software development, starting from planning and moving through development, testing, deployment, and closure.
- Dependency Management: Each phase depends on the successful completion of the previous one, ensuring that prerequisites are met before moving forward.
- Risk Mitigation: By addressing potential issues early (e.g., security considerations during design), the project minimizes risks in later stages.
- Resource Optimization: Allocating resources according to the project's needs at each phase ensures efficient use of personnel and time.

### Detailed Justification for Task Order

- Initiation Before Development: Establishing clear requirements and a solid architectural plan is essential before any development begins to prevent rework and misunderstandings.
- Backend and Frontend Parallel Development: While these can be developed in parallel, they both rely on the initial designs and requirements established in the initiation phase.
- AI Integration After Backend Development: The AI modules need a functioning backend to integrate with, so backend development must be sufficiently advanced.
- Testing Phases Post-Development: Testing follows development to validate the functionality and performance of the built components.
- Security Assessments Before Deployment: Ensuring security and compliance before deployment protects against vulnerabilities and legal issues.
- User Acceptance Testing Before Launch: UAT provides a final check from the user's perspective, ensuring the application meets their needs.
- Post-Launch Support After Deployment: Continuous support is only possible after the application is live, addressing any issues that arise in real-world use.
- Project Closure After All Activities: Formal closure signifies the end of the project, after all deliverables are met and resources can be released.

## Conclusion

The project plan is meticulously structured to ensure a logical flow of activities, efficient resource utilization, and the successful delivery of a secure, high-quality mobile banking application with AI capabilities. Each phase builds upon the previous one, mitigating risks and addressing critical aspects like security and user satisfaction at appropriate stages. The Work Breakdown Structure provides a clear roadmap for the project, facilitating effective management and communication among all stakeholders involved.
