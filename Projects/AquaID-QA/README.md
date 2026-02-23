# AquaID — QA Project (Manual + API)

**Date:** 2026-02-18  
**Scope:** Comprehensive QA testing for AquaID, a freshwater fish identification web application powered by Gemini AI. Modules covered: Authentication, Fish Identification (AI upload), My Aquarium, Compare Fish, Explore & Articles, Nearby Aquariums, Profile, and all REST API endpoints.  
**Artifacts:** Manual test cases, API test cases, bug reports, test summary reports (Excel), Selenium automation scripts, and markdown summaries (see `Artifacts/` and markdown summaries in this folder).

---

## Quick Summary

### Manual Testing

#### Test Cases
- Total: **57**
- Pass: **42**
- Fail: **0**
- Not Tested: **15**

#### Bugs
- Total: **20**
- Critical: **1**
- Major: **7**
- Minor: **10**
- Trivial: **2**

**Top Categories (bugs):**
- Fish Identification: 4
- My Aquarium: 3
- Explore & Articles: 3
- Nearby Aquariums: 3
- Authentication: 3
- Compare Fish: 2
- Profile: 2

---

### API Testing

#### API Test Cases
- Total: **40**
- Pass: **36**
- Fail: **4**
- Not Tested: **0**

#### API Bugs
- Total: **9**
- Critical: **2**
- Major: **4**
- Minor: **2**
- Trivial: **1**

**Top Failing Endpoints:**
- `POST /api/identify` — file type & size validation missing
- `DELETE /api/articles/:articleId` — endpoint not implemented
- `GET /api/compare` — same fish ID accepted without validation
- `POST /api/articles/generate` — no rate limiting

---


## Files

- `README.md` — this file; project overview and summary
- `TestCases_Summary.md` — all manual test cases in a readable table
- `API_TestCases_Summary.md` — all API test cases in a readable table
- `BugSheet_Summary.md` — all manual + API bugs in a readable table
- `Recommendations_Summary.md` — improvement recommendations
- `Artifacts/AquaID_QA_Report.xlsx` — manual test cases, bug reports, and test summary (Excel)
- `Artifacts/AquaID_API_Test_Report.xlsx` — API test cases, API bug reports, and API summary (Excel)
- `Screenshots/` — add evidence screenshots here

---

## Tech Stack Tested

| Layer | Technology |
| --- | --- |
| Frontend | React + TypeScript + Vite |
| Backend | Node.js + Express |
| Database | Firebase Firestore |
| Storage | Firebase Storage |
| Auth | Firebase Authentication (Email + Google SSO) |
| AI | Google Gemini API (fish identification + article generation) |
| TTS | Google Cloud Text-to-Speech |
| Maps | Google Maps API |
