# 🧪 QA Test Plan – Anonymized Version

> ⚠️ **Note on References**
> This document outlines the test approach, scope, environments, risks, stakeholders, and quality criteria used during the MVP phase of the `App` project. All internal references to company names, links, emails, domains, and repositories have been anonymized (e.g. `AnonCorp`, `anon@team.example.com`, `example.atlassian.net`, `github.com/anoncorp/app-repo`).  
> Almost all internal links in this document are provided for illustrative purposes only.  
> They point to this same document and do not represent external sources or separate files.
> 
> Exceptions are links to the [Jira workflows](/Test_Plans/Jira_workflows.md) and [TestRails workflows](/Test_Plans/TestRail_Flows.md)

---

## 📑 Version History

| Version      | Date          | Author            | Reviewer           |
|--------------|---------------|-------------------|--------------------|
| 0.1-draft    | 08 Aug 2022   | @John.Doe  |                    |
| 0.2-draft    | 22 Aug 2022   | @John.Smith  | @Jane.Smith (Unlicensed) |
| 0.3-draft    | 14 Sep 2022   | @Ievgen.Guk       | @Taylor.Reed     |
| 0.4-adapted  | 22 Sep 2022   | @Ievgen.Guk       | team approval      |

---

## 📑 Table of Contents

1. [🎯 Stakeholders](#-stakeholders)
2. [🔍 Project-Specific Impact to Testing](#-1-project-specific-impact-to-testing)
3. [📦 Scope of Testing](#-2-scope-of-testing)
   - [✅ In Scope](#-21-in-scope)
   - [❌ Out of Scope](#-22-out-of-scope)
   - [🧰 Third-Party Systems](#-23-third-party-systems)
   - [🤝 Systems Validated Externally](#-24-systems-validated-by-externalother-organizations)
4. [✅ Quality and Acceptance Criteria](#-3-quality-and-acceptance-criteria)
5. [🧪 Test Process Description](#-4-test-process-description)
   - [🔍 Testing Types Overview](#-41-testing-types-overview)
   - [🔍 Testing Types Summary](#-41-testing-types-summary)
   - [📌 Jira Tasks](#-42-jira-tasks)
   - [🐞 Defects & RCA](#-43-defects--rca)
     - [🔄 Defect Lifecycle](#-431-defect-lifecycle)
     - [🧷 Defect Raising Rules](#-432-defect-raising-rules)
     - [🧠 Root Cause Analysis](#-433-root-cause-analysis-rca)
   - [📋 Test Case Management & Execution](#-44-test-cases-managment-and-execution)
     - [✅ General Rules](#-441-general-rules)
     - [⏳ Milestones](#-442-milestones)
     - [🧾 Test Case Creation Rules](#-443-test-cases-creation-rules)
     - [▶️ Test Case Execution](#-444-test-cases-execution)
   - [📊 Test Report Containment](#-45-test-report-containment)
   - [📐 Project Metrics](#-46-list-of-the-metrics-to-track-on-a-project)
6. [⚠️ Risks and Assumptions](#-5-risks-and-assumptions)
   - [⚠️ Risks](#-51-risks)
   - [🧾 Assumptions](#-52-assumptions)
7. [📱 Devices](#-6-devices)
8. [🛠️ Toolset](#-7-toolset)
9. [🌐 Test Environments](#-8-test-environments)
10. [📣 Communication Plan](#-9-communication-plan)
11. [🚨 Escalation Plan](#-10-escalation-plan)
12. [🗓️ Test Schedule](#-11-test-schedule)
    - [📅 Sprint Schedule](#-111-sprint-schedule)
    - [📅 Phase Schedule](#-112-phase-schedule)
13. [🧾 Test Deliverables](#-12-test-deliverables)

---

## 🎯 Stakeholders

Stakeholders are tracked in the internal stakeholder register. Refer to:  
[Project Management Plan | Stakeholders](/Test_Plans/Test_plan_example.md)

---

## 🔍 1. Project-Specific Impact to Testing

- Goal: unify fragmented features and improve UX.
- Tech stack: React Native + native APIs.
- Current phase: MVP.
- UX audit and interviews highlight performance bottlenecks and design challenges.

---

## 📦 2. Scope of Testing

### ✅ 2.1 In Scope

JIRA: [DemoApp Release Plan](/Test_Plans/Test_plan_example.md)

## 📋 Core Features for MVP Phase – Sample Table

| System / Component / Interface | Description                                                                                                   | Responsible Side  | Reference                                                                                                                 |
|-------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| 🟢 **Access Gateway**         | User opens DemoApp and can log in with ease, selecting preferred environment.                                 | QA Engineers       | [DemoApp Planning / Access](/Test_Plans/Test_plan_example.md)  |
| 🟠 **Dashboard Hub**          | User navigates to dashboard and verifies whether all data reflects actual and updated state.                  | QA Engineers       | [DemoApp Planning / Dashboard](/Test_Plans/Test_plan_example.md)  |
| 🐄 **Entity Profiles**        | User searches for a specific entity and opens its card to view all detailed information.                      | QA Engineers       | [DemoApp Planning / Profiles](/Test_Plans/Test_plan_example.md)  |
| 📋 **Activity Queue**         | User reviews task list and planned activity workflows that must be completed today.                           | QA Engineers       | [DemoApp Planning / Tasks](/Test_Plans/Test_plan_example.md)  |
| 🛠️ **Tools Panel**           | User accesses extended settings including device syncing and data refresh actions.                            | QA Engineers       | [DemoApp Planning / Tools](/Test_Plans/Test_plan_example.md)  |
| 🔊 **Advanced Capabilities**  | Additional functionalities under review: voice interaction, localization, and user onboarding tool.           | TBD               | [DemoApp Planning / Extras](/Test_Plans/Test_plan_example.md)  |




### ❌ 2.2 Out of Scope

| Component Name            | Description                                                                                         |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| Legacy Server Module      | Back-end logic is frozen for MVP phase and excluded from active QA activities.                     |
| Classic Mobile App        | App built on deprecated framework. No new features, tests or fixes planned.                        |
| Application Replacement   | The new app does not support updates or automatic migration from legacy version.                   |
| Cross-Version Sync        | Migration paths between old and new versions are not addressed during MVP.                         |

### 🧰 2.3 Third-Party Systems

| System Name           | Usage Description                                                            | Responsible Side  | Reference                                                                                                                     |
|-----------------------|------------------------------------------------------------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------|
| CloudBridge OnPrem    | Existing server infrastructure used for basic back-end connectivity. No new implementation or QA scope. | Test Engineer      | [Architecture Overview | OnPrem](/Test_Plans/Test_plan_example.md)                                                     |
| CloudBridge Cloud     | Cloud-based mirror for OnPrem server, identical purpose and constraints.      | Test Engineer      | [Architecture Overview | Cloud](/Test_Plans/Test_plan_example.md)                                                      |
| OnboardIQ             | Tool used by UX team to implement in-app walkthroughs and notifications. Exact testing scope is TBD.   | Test/UX TBD         | [Integration Plan | OnboardIQ](/Test_Plans/Test_plan_example.md)                                                  |

### 🤝 2.4 Systems Validated by External/Other Organizations

| Component Name         | Description                                                                 | Responsible Side            | Reference                                                                                                                   |
|------------------------|-----------------------------------------------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| CloudBridge OnPrem     | Infrastructure managed and tested by partner QA teams or VAS service org.   | Third-Party or QA Team       | [Architecture Overview | External Validation](/Test_Plans/Test_plan_example.md)                                     |
| CloudBridge Cloud      | Infrastructure hosted and validated externally. QA may review indirectly.   | External Team / QA Oversight | [Architecture Overview | External Validation](/Test_Plans/Test_plan_example.md)                                     |

---

## ✅ 3. Quality and Acceptance Criteria

The following attributes define whether the application meets the required quality level and is eligible for release:

- The product must align with business requirements, functional specs, and UI designs (see [Scope of Testing](/Test_Plans/Test_plan_example.md)).
- No Critical or Major bugs may remain unresolved before production release.
- Entry and Exit criteria must comply with the [Test Strategy](/Test_Plans/Test_plan_example.md).
- A formal Test Exit Report is required at the end of System Testing.
- All defects must be resolved or confirmed by business for deferment before proceeding.
- Minimum 95% test case pass rate must be achieved.

---

## 🧪 4. Test Process Description

The overall QA flow follows previously defined practices from [QA Process Improvements | Requirements Traceability](/Test_Plans/Test_plan_example.md) and the automation framework documented in [Test Automation Flow](/Test_Plans/Test_plan_example.md).

### 🔍 4.1 Testing Types Overview

| 🧪 Test Type                   | ✍️ Designed By       | 🛠️ Devices / Tools                                | 👤 Performed By          | 📎 Reference Link                                  |
|-------------------------------|----------------------|---------------------------------------------------|--------------------------|----------------------------------------------------|
| Manual Functional Testing      | @Ievgen.Guk          | Personal devices, RFID/BLE Scanner, BrowserStack | Manual QA Engineers       |  |
| Usability Testing              | @Ievgen.Guk          | Same as above                                     | Manual QA Engineers       |   |
| Automated Functional Testing   | @Tobias.Feldman      | Emulators & Simulators                            | Automation Engineers      | [Automation Strategy](/Test_Plans/Test_plan_example.md) |
| Automated Smoke Testing        | @Tobias.Feldman      | Emulators & Simulators                            | Automation Engineers      | [Smoke Automation](/Test_Plans/Test_plan_example.md)    |
| Performance Testing            | @Quentin.Rossmoor    | Physical devices + RFID/BLE Scanner               | MQA & AQA Engineers       | [Performance Plan](/Test_Plans/Test_plan_example.md)    |
| Regression Testing             | @Ievgen.Guk, @Tobias.Feldman | All device types                          | Manual + Automation QA     | [Regression Flow](/Test_Plans/Test_plan_example.md)     |
| Security Testing               | @John.Doe            | Same devices/tools                                | Security QA Engineers     | [Security Strategy](/Test_Plans/Test_plan_example.md)   |


## 🔍 4.1 Testing Types Summary

| 🧪 Test Type             | 👤 Responsible Role   | 📝 Description                                                                                                            | 📅 Phase / Schedule                           | ✅ Completion Criteria                                                              | 📊 Expected Results                                                                                                   | 🤝 Responsible Contacts               |
|--------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Unit Testing             | Developer            | Testing of individual code units to ensure they function as intended.                                                    | Ad hoc during development                      | Code units implemented, high-level design finalized, requirements available.         | All unit tests passed, major issues resolved.                                                                       | Developer implementing code          |
| Functional Testing       | Test Engineer        | Verification of all application features including device integration (BT/RFID). Includes installation, upgrade, etc.     | In-sprint scope (manual + automation)          | Requirements approved, environment set up, test cases ready.                         | All functional cases executed, critical bugs resolved, coverage complete.                                           | @Ievgen.Guk / @Tobias.Feldman       |
| Smoke Testing            | Test Engineers       | Basic validation of critical functionality after new build deployment.                                                   | Each new master build                          | Master build available, no blockers, test tools configured.                          | All smoke cases executed, no showstoppers or blockers.                                                              | @Ievgen.Guk / @Tobias.Feldman       |
| Regression Testing       | Test Engineers       | Re-execution of previously validated functionality to check for impact of new code changes.                              | Per phase release (EPIC)                       | App and regression scope finalized, code freeze applied.                             | Existing functionality intact, no regressions, test run completed.                                                 | @Ievgen.Guk / @Tobias.Feldman       |
| Performance Testing      | Test Engineers       | Assessment of responsiveness, throughput and stability under load.                                                       | Early sprint (first five sprints)              | Real device setup, environment clean, app passed smoke and unit tests.               | Performance report shared; Confluence & Jira updated with fault logs.                                               | @Ievgen.Guk / @Tobias.Feldman       |
| Usability Testing        | Test Engineers       | Evaluation of ease of use and accessibility. WCAG (A/AA) coverage TBD.                                                   | Within scope of functional testing             | Environment ready, UX test cases approved, valid data prepared.                      | App evaluated for intuitive design, no UX blockers; feedback documented.                                            | @Ievgen.Guk                          |
| Security Testing         | Security Engineers   | Vulnerability and penetration testing to prevent breaches. Conducted upon request and after approval.                    | On-demand                                      | Owner’s approval; test tools validated; sensitive modules identified.                | Issues documented; security defects tracked; risk report issued.                                                    | @Vitaliy.Parichenko (Unlicensed)     |
| User Acceptance Testing  | Business / VAS       | Final testing by client to validate business workflows and readiness before production.                                  | Alpha/Beta phases                              | Requirements finalized; all previous testing stages passed.                          | No critical defects open; business processes validated; UAT sign-off obtained.                                      | Business stakeholders               |
| Automation Testing       | Automation Engineers | Execution of automated scripts for smoke, regression and core coverage. Goal: >80% automation.                          | Sprint-based, post-feasibility validation       | Manual tests baselined; Feasibility of AUT confirmed; tool readiness verified.        | Scripts executed; dry run completed; integration with TestRail successful.                                           | @Tobias.Feldman                    |

---

## 📌 4.2 Jira Tasks

All testing tasks are tracked via Jira and linked with development features:

- 🧩 **Feature Testing Tasks:** Per epic/sprint.
- 🔄 **Retest & Bug Tasks:** Triggered by defect fixes.
- 🤖 **Automation Tasks:** Track script progress and integration.
- 📂 **Regression Packs:** Updated monthly or per major release.

[ JIRA Workflow | 1. The Jira tasks for testing:](/Test_Plans/Test_plan_example.md)

---

## 🐞 4.3 Defects & RCA

Bug management handled jointly via Jira and TestRail dashboards.

### 🔄 4.3.1 Defect Lifecycle
- Standard workflow: Log -> Triaged -> Assigned -> Retest -> Closed.
- Severity and impact defined in defect metadata.  

More details on [JIRA workflows | 2. Defect lifecycle](/Test_Plans/Test_plan_example.md)

### 🧷 4.3.2 Defect Raising Rules
- **In-scope bugs**: Raised within active sprint via story subtask (aka `Failed Tests`).
- **Out-of-scope bugs**: Logged separately with full impact analysis (aka `Defect`).

More details on: 
- [JIRA workflows | 3.1. In the scope of sprint feature testing](/Test_Plans/Jira_workflows.md#31-in-the-scope-of-sprint-feature-testing) 
- [JIRA workflows | 3.2. Not in the scope of sprint feature testing](/Test_Plans/Jira_workflows.md#32-not-in-the-scope-of-sprint-feature-testing)

### 🧠 4.3.3 Root Cause Analysis (RCA)
📌 The root cause analysis can be done in a few simple steps which are as follows:

1. Identify the exact issue and when it was introduced.
2. Investigate logs, reports, and reproduction steps.
3. Confirm contributing components (e.g., code module, data error).
4. Categorize the root cause (e.g., human error, environment setup, regression).
5. Document findings in the defect or RCA section of Confluence/Jira.
6. Suggest mitigation steps to prevent recurrence.

More details on [Root Cause Analysis Template](/Test_Plans/Test_plan_example.md)

---

## 📋 Test cases managment and execution

The Test milestone\Test Plan\Test Run\Test cases should be created before the test execution started.
All manual and automated cases tracked via TestRail Milestones.

### ✅ 4.4.1 General Rules

[TestRail flow | 1. General rules](/Test_Plans/TestRail_Flows.md#-1-general-rules)

- No execution without approved test plan.
- Test cases must follow naming conventions and traceability.

### ⏳ 4.4.2 Milestones

[TestRail flow | 2. Milestones](/Test_Plans/TestRail_Flows.md#-2-milestones)

- Defined per epic or phase.
- Include planned test runs and linked requirements.

### 🧾 4.4.3 Test cases creation rules

[TestRail flow | 3. Test cases creation rules](/Test_Plans/TestRail_Flows.md#-3-test-case-creation-rules)

- Include functional, edge, negative, and recovery scenarios.
- Reviewed before activation.

### ▶️ 4.4.4 Test cases execution

[TestRail flow | 4. Test cases execution](/Test_Plans/TestRail_Flows.md#-4-test-cases-execution)

- **Manual:** Executed by QA with real-time defect logging.
- **Automated:** Results pushed to TestRail; reviewed after dry run.

### 📊 4.5 Test Report Containment

This section outlines the content and reporting practices for maintaining visibility across QA activities during each iteration.

- 🗂 **Weekly task summary:**  
  Includes list of all active testing tasks with assigned priorities and current statuses (e.g., in progress, completed, blocked).

- 📈 **Iteration metrics tracking:**  
  Key metrics collected weekly to measure progress and efficiency. Data includes pass rate, defect rate, failed test cases, and trend comparison against previous iterations.

- 💡 **Recommendations:**  
  Based on the latest testing results, QA may provide suggestions to improve testing coverage, automation scope, test data relevance, or process efficiency. Recommendations are documented and shared during weekly team syncs and sprint demos.

### 📐 4.6 List of the Metrics to Track on a Project

This section presents a comprehensive overview of QA and development metrics to assess product quality, team efficiency, and testing effectiveness throughout the project lifecycle.

### 📐 4.6 List of the Metrics to Track on a Project

| 🧪 **Metric Name**                | 🧮 **Formula**                                                                  | 👤 **Responsible Role**                     | ⏱️ **Frequency**                  | 📤 **Way to Provide**                         |
|----------------------------------|----------------------------------------------------------------------------------|---------------------------------------------|----------------------------------|------------------------------------------------|
| DCE – defect containment efficiency | Number of bugs found after release / Total number of bugs                       | Test Team Lead                              | After each release               | Store on Confluence space                      |
| Requirements coverage             | (Number of requirements covered / Total requirements) × 100                      | Test Team Lead                              | Each iteration                   | Store on Confluence space                      |
| Defect distribution by status & phase | (Total defects / Functional area(s)) × Status × Phase                           | Test Team Lead                              | Each iteration                   | TMT or Confluence space                        |
| Failed Test Cases %               | (Failed tests / Total tests executed) × 100                                     | TMT or Test Team Lead                       | Each iteration                   | TMT or Confluence space                        |
| Passed Test Cases %               | (Passed tests / Total tests executed) × 100                                     | TMT or Test Team Lead                       | Each iteration                   | TMT or Confluence space                        |
| Fixed Defects %                   | (Defects fixed / Defects reported) × 100                                        | Test Team Lead                              | Each iteration                   | Store on Confluence space                      |
| Defect Reopen Ratio               | (Reopened defects / Defects reported) × 100                                     | Test Team Lead                              | Each iteration                   | Store on Confluence space                      |
| Defects Rejection Rate            | (Invalid defects / Defects reported) × 100                                      | Test Team Lead                              | Each iteration                   | Store on Confluence space                      |
| Code Coverage                     | (Executed code lines during testing / Total code lines) × 100                   | Developer                                   | TBD                              | TBD                                            |
| Automation Test Coverage          | (Automated test cases / Total test cases) × 100                                 | TMT or Test Team Lead                       | Each iteration                   | TMT or Confluence space                        |

---

## ⚠️ 5. Risks and Assumptions

This section identifies potential obstacles that may impact QA timelines and test coverage, along with project assumptions that guide planning and execution.

### ⚠️ 5.1 Risks

| # | 🧨 Risk                                                                 | 🔢 Probability | 🔴 Severity | 🛠️ Mitigation Plan                                                                 |
|---|------------------------------------------------------------------------|----------------|-------------|-------------------------------------------------------------------------------------|
| 1 | Feature is not ready for testing                                       | M              | M           | Reschedule affected tests to the next sprint                                        |
| 2 | Mobile devices unavailability                                          | M              | L           | Use emulators/simulators locally; reschedule if needed                             |
| 3 | Late approval of designs/mock-ups; design changes                      | M              | M           | Set deadlines; confirm changes before feature implementation; reschedule tests     |
| 4 | Unplanned new features or modifications                                | L              | L           | Define deadlines for new requirements; reschedule tests if needed                  |
| 5 | Changes in requirements                                                | M              | L           | Continuously analyze scope to adapt proactively                                    |
| 6 | Scope exceeds test team capacity                                       | M              | H           | Prioritize Critical/High tests; optimize scope review                              |
| 7 | Delays in schedule                                                     | L              | H           | Restructure test activities; continuously review scope                             |
| 8 | Team member leaves (sick/vacation)                                     | L              | L           | Reschedule affected testing                                                        |
| 9 | Availability of a new OS version                                       | L              | L           | Add new OS to TMT configuration; assess manual compatibility                       |

### 🧾 5.2 Assumptions

- Each release includes notes with details of implemented features and their impact  
- All **blocker** defects are marked with **high priority**  
- All detected defects are resolved before next software release  
- All project documentation is up-to-date and delivered timely to the QA team  
- All necessary equipment and tools are available and ready for testing
- The test schedule is reviewed in case there are any obstacles to testing

---

## 📱 6. Devices

📌 See [Tools List | Devices](/Test_Plans/Test_plan_example.md)  
ℹ️ According to [Research: JiraTicket-80](/Test_Plans/Test_plan_example.md), two physical devices are selected — one per OS platform (e.g., iOS and Android).  

> ⚠️ Note: **Portrait orientation** is prioritized; tablets are excluded from device scope.

---

## 🛠️ 7. Toolset

📌 See [CI/CD Pipeline](/Test_Plans/Test_plan_example.md) and [Tools List](/Test_Plans/Test_plan_example.md)  
Describes test automation frameworks, build pipelines, reporting and toolchain integrations used for quality assurance.

---

## 🌐 8. Test Environments

| 🏷️ **Environment Name** | 💬 **Comments**                      |
|--------------------------|--------------------------------------|
| Staging                  | [Server Platform – Staging link](/Test_Plans/Test_plan_example.md) |
| Production               | [Server Platform – Production link](/Test_Plans/Test_plan_example.md) |

---

## 📣 9. Communication Plan

A detailed communication matrix is provided in a separate document:  🔗 [Communication Matrix](/Test_Plans/Test_plan_example.md)

Primary channels used for collaboration between QA, Development, and Product Management include:

- **Daily stand-ups** – via Slack or MS Teams  
- **Test progress updates** – displayed on TMT dashboards  
- **Issue tracking and reporting** – managed through Jira tickets  
- **Documentation and technical notes** – maintained in Confluence  
- **Release coordination and demos** – handled through Email and Sprint ceremonies


---

## 🚨 10. Escalation Plan

For problem resolution and escalation procedures, refer to:  🔗 [Problem Resolution and Escalation Draft](/Test_Plans/Test_plan_example.md)

---

## 🗓️ 11. Test Schedule

The test schedule defines the QA coverage timeline for each sprint:

- Defined scope of testing per release  
- Execution windows  
- Regression periods  
- Defect triage and retesting sessions  
- QA sign-off checkpoints  

A detailed calendar view is available in Confluence or maintained via TMT tracking.

---

## 🗓️ 11. Test Schedule

### 11.1 Sprint schedule

<style>
  td.activity { font-weight: bold; background-color: #f2f2f2; }

  /* Color Classes */
  .blue-light  { background-color: #e0f2ff; }     /* light blue */
  .blue        { background-color: #a5d8ff; }     /* medium blue */
  .green-light { background-color: #d3f9d8; }     /* light green */
  .green       { background-color: #8ce99a; }     /* medium green */
  .red         { background-color: #ffc9c9; }     /* light red/pink */
  .yellow      { background-color: #fff3bf; }     /* yellow */
  .yellow-light{ background-color: #fff9db; }     /* light yellow */
  .gray        { background-color: #e9ecef; }     /* gray */
</style>

<table>
  <thead>
    <tr>
      <th>Activity</th>
      <th>Day 1</th>
      <th>Day 2</th>
      <th>Day 3</th>
      <th>Day 4</th>
      <th>Day 5</th>
      <th>Day 6</th>
      <th>Day 7</th>
      <th>Day 8</th>
      <th>Day 9</th>
      <th>Day 10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="activity">Test Plan creation</td>
      <td class="blue">TestRail Sprint plan</td>
      <td></td><td></td><td></td><td></td>
      <td class="blue">Backlog Refinement</td>
      <td></td>
      <td class="blue">Backlog Refinement (Optional)</td>
      <td></td><td></td>
    </tr>
    <tr>
      <td class="activity">Manual test cases creation</td>
      <td class="blue-light"></td>
      <td class="blue"></td>
      <td class="blue"></td>
      <td class="blue"></td>
      <td class="blue-light"></td>
      <td class="blue-light"></td>
      <td class="blue-light"></td>
      <td class="blue-light"></td>
      <td class="blue-light"></td>
      <td class="blue-light"></td>
    </tr>
    <tr>
      <td class="activity">Manual test cases execution</td>
      <td></td><td></td><td></td>
      <td class="green-light"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green-light"></td>
    </tr>
    <tr>
      <td class="activity">Performance testing</td>
      <td class="blue"></td>
      <td class="blue"></td>
      <td class="blue"></td>
      <td></td><td></td><td></td><td></td><td></td><td></td><td></td>
    </tr>
    <tr>
      <td class="activity">Smoke testing</td>
      <td class="gray">Manual/Automation</td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
      <td class="gray"></td>
    </tr>
    <tr>
      <td class="activity">Defining what to automate next</td>
      <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
      <td class="red"></td>
      <td class="red"></td>
    </tr>
    <tr>
      <td class="activity">Automation test cases creation</td>
      <td class="yellow"></td>
      <td class="yellow"></td>
      <td class="yellow"></td>
      <td class="yellow"></td>
      <td class="yellow-light"></td>
      <td class="yellow-light"></td>
      <td class="yellow-light"></td>
      <td class="yellow-light"></td>
      <td class="yellow-light"></td>
      <td class="yellow-light"></td>
    </tr>
    <tr>
      <td class="activity">Automation test cases execution</td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
      <td class="green"></td>
    </tr>
    <tr>
      <td class="activity">Sprint Demo</td>
      <td></td><td></td><td></td><td></td><td></td>
      <td></td><td></td><td></td><td></td>
      <td class="blue">Demo</td>
    </tr>
  </tbody>
</table>


### 11.2 Phase schedule
<style>
  td.activity { font-weight: bold; background-color: #f2f2f2; }
  .c1 { background-color: #fefddbff; }  /* Color 1 */
  .c2 { background-color: #dbeafe; }  /* Color 2 */
  .c3 { background-color: #e0ffd4ff; }  /* Color 3 */
  .c4 { background-color: #60a5fa; }  /* Color 4 */
  .c5 { background-color: #cdf8f8ff; }  /* Color 5 */
  .c6 { background-color: #6c29d8ff; color: white; }  /* Color 6 */
  .c7 { background-color: #1d4ed8; color: white; }  /* Color 7 */
</style>

<table>
  <thead>
    <tr>
      <th class="c7">Activity</th>
      <th class="c7">Sprint 1</th>
      <th class="c7">Sprint 2</th>
      <th class="c7">Sprint 3</th>
      <th class="c7">Sprint 4</th>
      <th class="c7">Sprint 5</th>
      <th class="c7">Sprint 6</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="activity">Functional Testing</td>
      <td class="c1">✓</td>
      <td class="c1">✓</td>
      <td class="c1">✓</td>
      <td class="c1">✓</td>
      <td class="c1">✓</td>
      <td class="c1">✓</td>
    </tr>
    <tr>
      <td class="activity">Non-Functional Testing</td>
      <td></td>
      <td></td>
      <td></td>
      <td class="c2">✓</td>
      <td class="c2">✓</td>
      <td class="c2">✓</td>      
    </tr>
    <tr>
      <td class="activity">Smoke Testing</td>
      <td></td>
      <td class="c4">✓</td>
      <td class="c4">✓</td>
      <td class="c4">✓</td>
      <td class="c4">✓</td>
      <td class="c4">✓</td>
    </tr>
    <tr>
      <td class="activity">Regression Testing</td>
      <td></td>
      <td></td>
      <td></td>
      <td class="c3">✓</td>
      <td class="c3">✓</td>
      <td class="c3">✓</td>
    </tr>
    <tr>
      <td class="activity">Performance Testing</td>
      <td class="c5">Old App</td>
      <td class="c5">Old + New App</td>
      <td class="c5">New App</td>
      <td class="c5">New App</td>
      <td class="c5">New App</td>
      <td class="c5">New App</td>
    </tr>
    <tr>
      <td class="activity">Release Readiness</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td class="c6">✓</td>
      <td class="c6">✓</td>
    </tr>
  </tbody>
</table>

---

### 12. TEST DELIVERABLES

| #  | Artifact to be provided | Target audience                                                | Author/Responsible Person(s) | Frequency (delivery time)                                 | Method of delivery                   |
|----|-------------------------|----------------------------------------------------------------|------------------------------|------------------------------------------------------------|--------------------------------------|
| 1  | Test Plans              | Stakeholders register, Project Management Plan, Stakeholders, Development Team | Test Lead                   | Once before the testing start, Every time when changed     | Confluence page                      |
| 2  | Test Strategy           | Stakeholders                                                   | Test Lead                    | Once before the testing start, Every time when changed     | Confluence page                      |
| 3  | Bug Reports             | Anyone                                                         | QA Team                      | Upon finding a bug                                        | e-mail                               |
| 4  | Test Result Reports     | Test Engineers                                                 | QA Team                      | Weekly                                                    | e-mail                               |
| 5  | Test Cases              | Development Team                                               | Test Engineers               | Before the testing start                                  | e-mail, TestRail link in Jira        |
| 6  | Test Execution Result   | Development Team                                               | Test Engineers               | After execution                                           | e-mail, TestRail link in Jira        |

---
