# Auth Module — Test Summary Report

## Build/Release
- Build: v1.0 (Sample)
- Date: (Fill)

## Scope
Login, Signup, Forgot Password

## Execution Summary
| Area | Planned | Executed | Passed | Failed | Blocked |
| --- | ---:| ---:| ---:| ---:| ---:|
| Login | 20 | 20 | 18 | 2 | 0 |
| Signup | 12 | 12 | 11 | 1 | 0 |
| Forgot Password | 8 | 8 | 7 | 1 | 0 |
| **Total** | **40** | **40** | **36** | **4** | **0** |

## Defect Summary (Sample)
| Severity | Count | Notes |
| --- | ---:| --- |
| High | 2 | Must fix before release |
| Medium | 2 | Fix soon / acceptable with workaround |
| Low | 0 | Cosmetic |

## Key Issues / Observations
- Some validations do not behave as expected (see Bug Reports folder).
- Ensure forgot password messaging does not disclose account existence.
- Review logout + browser back behavior to prevent protected content flash.

## Risks
- Account lock/rate limiting not verified in all environments.
- Accessibility labels may be incomplete.

## Recommendation
Proceed only after fixing **High severity** defects and re-running regression checklist.
