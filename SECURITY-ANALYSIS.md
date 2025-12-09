# Security Analysis – tasks_devsecops

## 1. Introduction

This document contains the security analysis for the **tasks_devsecops** application. It is a FastAPI-based task management system where admins create and assign tasks to users, and users view their assigned tasks. This analysis identifies main threats, corresponding security requirements, and testing strategies.

---

## 2. Threat Identification

| ID | Threat | Description |
|----|--------|------------|
| T1 | Injection attacks | Possible attacks via malicious input (JSON, SQL if using DB). |
| T2 | Cross-Site Scripting (XSS) | Malicious code injected into task content or responses. |
| T3 | Broken Authentication | Improper or missing authentication allowing unauthorized access. |
| T4 | Sensitive Data Exposure | Exposure of user emails, internal notes, or other sensitive fields in API responses. |
| T5 | Broken Access Control | Users accessing tasks not assigned to them, or non-admins creating/deleting tasks. |
| T6 | Security Misconfiguration | Misconfigured CORS, missing security headers, or insecure error handling. |
| T7 | Information Leakage | Stack traces or internal system details exposed in error responses. |

---

## 3. Security Requirements

| Threat ID | Threat Description | Requirement | Motivation | Implementation | Testability | Priority |
|-----------|-----------------|------------|-----------|----------------|-------------|---------|
| T1 | Injection attacks (malicious JSON input) | Validate all input using Pydantic models | Prevent attackers from sending malicious or malformed data that could compromise the app | Use Pydantic models for request bodies for POST/PUT endpoints | Send invalid/malicious JSON and assert 422 validation errors | Critical |
| T2 | Cross-Site Scripting (XSS) | Sanitize output before sending to frontend | Prevent attackers from executing scripts via task content | Escape HTML or use safe JSON serialization in responses | Add a task with `<script>` tags and verify frontend renders safely without executing scripts | Important |
| T3 | Broken Authentication | Require authentication for all modifying endpoints (POST, DELETE) | Ensure only authorized users can create, modify, or delete tasks | Implement JWT authentication with token verification | Attempt requests without token or with invalid token → should fail with 401 | Critical |
| T4 | Sensitive Data Exposure | Filter sensitive fields from responses | Prevent leaking emails, internal notes, or other confidential info | Only return allowed fields in GET /tasks | Request tasks and verify sensitive fields are not present | Important |
| T5 | Broken Access Control | Verify task ownership before DELETE | Prevent users from deleting tasks that are not theirs | Backend checks task owner ID against authenticated user ID | Attempt deletion of another user’s task → should fail with 403 | Critical |
| T6 | Security Misconfiguration | Ensure proper headers, HTTPS, and CORS | Prevent attackers from exploiting server misconfigurations | Configure CORS, HTTPS (if applicable in production), and secure headers | Check response headers, test CORS policies, attempt HTTP access if applicable | Desired |
| T7 | Error Handling / Info Leakage | Do not expose stack traces or sensitive info in responses | Prevent attackers from gaining internal server info | Use proper exception handling and custom error messages | Trigger server errors and verify response does not reveal sensitive info | Important |

---

## 4. Notes

- Critical requirements must be implemented before pushing to the `main` branch.  
- All requirements must be covered by automated tests integrated into the CI/CD pipeline.  
- Any change affecting security must be documented here and tested.
