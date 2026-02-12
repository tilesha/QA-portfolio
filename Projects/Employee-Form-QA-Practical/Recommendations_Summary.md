# Recommendations Summary

| Recommendation ID | Area | Recommendation Description | Reason / Benefit |
| --- | --- | --- | --- |
| REC-01 | Validation | Implement client-side validation before attempting submission (email format, contact length, required fields). | Prevents unnecessary backend calls, improves user guidance and reduces errors. |
| REC-02 | Employee ID | Make Employee ID strictly read-only and auto-generated based on Gender + NIC + DOB (MMDD) as per spec. | Ensures data integrity and compliance with requirements. |
| REC-03 | Age Calculation | Make Age read-only and fix calculation logic to reflect correct age in years based on current date. | Prevents incorrect employee data and improves reliability. |
| REC-04 | Blood Group | Remove AB+ and AB- from Blood Group dropdown; keep only allowed values. | Enforces business rule and reduces invalid registrations. |
| REC-05 | UX Messages | Replace technical error messages with user-friendly messages; include guidance and Retry option. | Improves usability and reduces user confusion. |
| REC-06 | Exit Handling | Add exit confirmation dialog and unsaved-changes warning. | Prevents accidental data loss. |
| REC-07 | Field Labels | Align all UI labels with specification terminology (E-mail Address, Contact Number, Age, Permanent Address). | Improves requirement traceability and consistency. |
| REC-08 | Input Masking | Add input masks/constraints for NIC and Contact Number (digits-only, length enforcement). | Prevents invalid inputs and reduces data cleanup. |
| REC-09 | Character Counters | Add remaining character counter for Full Name and optionally for other long fields. | Helps users stay within limits and improves data quality. |
| REC-10 | Date Format | Use a consistent locale-appropriate date format (e.g., DD/MM/YYYY) and remove extra spacing/weekday. | Improves readability and avoids ambiguity. |