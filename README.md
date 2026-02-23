# 🔍 Tilesha Madulantha — Quality Assurance Engineer  

**Software Engineering graduate specializing in Software Quality Assurance**, focused on delivering reliable systems through structured testing, defect analysis, and comprehensive validation processes.
This repository showcases practical QA work including complete test cycles, defect documentation, test planning, execution reporting, API validation, and SQL-based data verification.

---

## 🎓 Education
- B.Sc. (Hons) in Software Engineering — University of Plymouth (2025)
- Information Technology — NIBM
- NVQ Level 4 in Graphic Design — NAITA

---

## 🎯 Career Goals
Seeking opportunities as:

- Junior QA Engineer
- QA Tester
- Test Engineer
- Software Quality Assurance Analyst

**Interested in:**

- Web application testing
- Mobile application testing
- API testing and validation
- Agile/Scrum testing environments
- Learning test automation frameworks

---


## 🧠 Testing Methodology

My testing approach is built on industry best practices:

- ✅ Requirement Analysis - Understanding acceptance criteria and user stories
- ✅ Test Design - Positive, negative, and boundary scenario coverage
- ✅ Risk-Based Prioritization - Focus on high-impact areas first
- ✅ Defect Classification - Severity and priority-based bug reporting
- ✅ Structured Documentation - Clear, reproducible test cases and bug reports
- ✅ Regression Validation - Ensuring fixes don't introduce new issues

I focus on identifying functional gaps, validation weaknesses, usability issues, and data inconsistencies early in the development lifecycle to reduce costs and improve product quality.

---

## 📊 Featured QA Project

### 🐟 AquaID — Manual + API + Automation Testing
Objective: Comprehensive quality validation of a Gemini AI-powered freshwater fish identification web application

Project Scope:

- Authentication (Email/Password + Google SSO)
- Fish Identification via AI Image Upload
- My Aquarium — Personal Collection Management
- Compare Fish — Side-by-side attribute comparison
- Explore & Articles — AI-generated fish care content
- Nearby Aquariums — Google Maps integration
- REST API Endpoints — All 14 server routes tested

Testing Results:

- ✅ 57 Manual Test Cases designed and executed
- ✅ 40 API Test Cases validated via Postman
- 🐞 20 Manual Defects identified and documented
- 🐞 9 API Defects identified and documented
- 🔴 Critical Issues: 3 (offline crash, unimplemented DELETE, no rate limiting)
- 🟠 Major Issues: 11 (file validation, Safari audio, TTS persistence)
- 🟡 Minor/Trivial Issues: 15 (UI feedback, filter state, confirmation dialogs)
- 🤖 ~94 Automated Tests written in Python + Selenium WebDriver

Key Findings:

- App crashes with white screen when network is offline during identification
- DELETE /api/articles endpoint handler is not implemented — articles cannot be deleted
- No rate limiting on AI article generation — Gemini API quota risk
- File type and size not validated client-side — non-image files reach Gemini API
- Audio player non-functional on Safari iOS
- Fish notes card does not refresh after editing — stale UI state
- No confirmation dialog before removing fish from aquarium

Deliverables:

- 57 Manual Test Cases with preconditions, steps, and expected results
- 40 API Test Cases with request payloads and response validation
- 29 Bug Reports (manual + API) with severity, priority, and reproduction steps
- 20 Recommendations for fixes and improvements
- Excel Test Reports (Manual + API) with auto-calculated metrics
- Selenium + requests Python automation test suite (~94 tests)

👉 [View Full Project](Projects/AquaID-QA/)

### 🧾 Employee Form — Comprehensive Manual Testing
Objective: End-to-end quality validation of an employee management form application
Project Scope:

- Personal Information Module
- Contact & ID Validation
- Employment Information
- Dropdown Controls
- Form Validation & Error Handling
- UI/UX Consistency
- Data Integrity & Loss Prevention

Testing Results:

- ✅ 32 Test Cases designed and executed
- 🐞 47 Defects identified and documented
- 🔴 Critical Issues: 12 (data loss, security concerns)
- 🟠 High Priority: 16 (validation failures, incorrect calculations)
- 🟡 Medium Priority: 10 (UI inconsistencies)
- 🟢 Low Priority: 9 (cosmetic issues)

Key Findings:

- NIC field accepts invalid special characters
- Age calculation incorrect (DOB: 18/11/2020 shows Age 3 instead of 5)
- Employee ID generation doesn't follow specification format
- Contact number validation missing (accepts <10 digits and special chars)
- Email validation not enforced (accepts incomplete emails)
- Future dates allowed in Date of Birth and Date Joined fields
- Form submission fails with generic error instead of field-level validation

Deliverables:

- Detailed Test Plan with scope and approach
- 32 Test Cases with preconditions, steps, and expected results
- 47 Bug Reports with severity, priority, and reproduction steps
- Test Summary Report with recommendations
- Visual evidence (screenshots) for critical defects

👉 [View Full Project](Projects/Employee-Form-QA-Practical/)

---

## 📦 Repository Sections

| Section | Description |
|----------|-------------|
| 🔌 API_Testing | API validation scenarios, mock responses & request checks |
| 🐞 Bug_Reports | Structured defect reports with reproduction steps |
| ✅ Checklists | UI, regression & validation checklists |
| 📁 Projects | Complete QA practical implementations |
| 🗂️ Test_Plans | Scope, approach, entry & exit criteria |
| 🧪 Test_Cases | Functional and boundary-based test scenarios |
| 📊 Test_Reports | Execution summaries, defect metrics & release risk |

---

## 🧰 Skills & Tools

- 🧪 Manual Testing (Functional, Regression, Smoke, Exploratory)
- 🧩 Test Design (Positive / Negative / Boundary Analysis)
- 🐞 Defect Reporting (Severity, Priority, Evidence-based documentation)
- 📮 API Testing (Postman)
- 🛢️ SQL Validation (MySQL queries for data verification)
- 🧾 Jira & Confluence
- 🐙 Git & GitHub
- 📝 Documentation (Excel, Google Sheets, Markdown)

---

## 💼 QA Artifacts & Documentation

Available in this repository:
- ✅ Test Plans - Scope, approach, entry/exit criteria, resource planning
- ✅ Test Scenarios - High-level test conditions for each module
- ✅ Test Cases - Detailed step-by-step test procedures with expected results
- ✅ Bug Reports - Structured defect documentation with reproduction steps
- ✅ Test Summary Reports - Execution metrics, defect analysis, recommendations
- ✅ Testing Checklists - Quick validation guides for various testing types
- ✅ API Test Collections - Postman collections with validation rules

---

## 🌱 Continuous Learning

Currently expanding my expertise in:

- 🤖 Test Automation - Selenium WebDriver, Python automation scripts
- 🔧 Advanced API Testing - Postman scripting, automated API validation
- 💾 Database Testing - Complex SQL joins, stored procedure validation
- 📊 Performance Testing - Load testing fundamentals with JMeter
- 🎯 Risk-Based Testing - Prioritization frameworks and impact analysis

---

## 💡 Why Work With Me?

- ✅ Systematic Approach - Structured testing methodology with clear documentation
- ✅ Detail-Oriented - Thorough analysis with focus on edge cases and boundary conditions
- ✅ Quality-Focused - Committed to delivering reliable, user-friendly software
- ✅ Team Player - Collaborative mindset with strong communication skills
- ✅ Continuous Learner - Always improving technical skills and QA knowledge

---

## 🌍 Contact

- 📧 tilesha.madulantha@gmail.com  
- 🔗 https://www.linkedin.com/in/tilesha-madulantha/  
- 📍 Sri Lanka  
- 🌐 English | Sinhala

---
## ⭐ Thank you for reviewing my QA portfolio! Feel free to reach out for collaboration or opportunities.
