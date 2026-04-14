I'll help you create a comprehensive, detailed README for your resume. Let me first read through all your project files to gather complete information about the architecture, modules, and systems.     

Searched for text `FROM|run|build|stage` (`**/Dockerfile*`), 20 results

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/backend/pyproject.toml#1-1), lines 1 to 100

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docs/SystemArchitecture.md#1-1), lines 1 to 200

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docs/AuthDataFlow.md#1-1), lines 1 to 150

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docs/README-AP.md#1-1), lines 1 to 150

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/azure-pipelines-back.yaml)

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docs/PayrollDataFlow.md#1-1), lines 1 to 150

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docs/PreawardDataFlow.md)

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/azure-pipelines-back.yaml)

Searched for text `class|def|async def` (`**/backend/app/**/*.py`), 30 results

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/azure-pipelines-front.yaml)

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/azure-pipelines-worker.yaml)

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/docker-compose.yml#1-1), lines 1 to 100

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/frontend/package.json#1-1), lines 1 to 50

Read [](file:///Users/prateekrauniyar/Documents/Nexus/nexus/tests/jest.config.js#1-1), lines 1 to 80

Read memory

I now have comprehensive information about your project. Let me create a detailed, professional README that covers all aspects of the system for your resume:

---

# **NEXUS: Integrated University Resource Management System**

## **Project Overview**

**Nexus** is a sophisticated, full-stack web application developed for the University of Idaho that integrates three core business modules—Accounts Payable, Payroll, and Pre-Award—into a unified platform. The system leverages modern cloud-native architecture, advanced AI capabilities, and enterprise security standards to streamline university administrative workflows. Built with a microservices mindset using a plug-and-play modular design, Nexus enables independent module deployment, scalability, and future extensibility.  

**Current Version:** 1.3.4  
**Repository:** Azure DevOps (UILIB/nexus)  
**Deployment:** Oracle Cloud Infrastructure (OCI) Kubernetes  
**Status:** Production-Ready

---

## **Table of Contents**

1. High-Level Architecture
2. Technology Stack
3. Core Modules
   - Authentication & Authorization Module
   - Accounts Payable (AP) Module
   - Payroll Module
   - Preaward Module
4. Frontend Architecture
5. Backend Architecture
6. Data Persistence Layer
7. CI/CD & Deployment Pipeline
8. Observability & Monitoring
9. Testing Strategy
10. Development Workflow
11. Key Design Patterns & Best Practices

---

## **High-Level Architecture**

### **System Diagram**

Nexus follows a **three-tier layered architecture** deployed on Oracle Cloud Infrastructure:

```
┌─────────────────────────────────────────────────────────────────┐
│                    React SPA Frontend (nginx)                    │
│        (5173 port - Static assets + API proxy routing)          │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  FastAPI Web Server (8000)                      │
│         (Request routing, authentication, middleware)           │
└──────────────────────────┬──────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐
    │   Auth   │      │    AP    │      │ Payroll  │
    │  Module  │      │ Module   │      │ Module   │
    └────┬─────┘      └────┬─────┘      └────┬─────┘
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
   ┌──────────────┐              ┌─────────────────┐
   │  PostgreSQL  │              │ Redis (Cache &  │
   │  (Primary DB)│              │ Task Queue)     │
   └──────────────┘              └─────────────────┘
         │
         ├─→ Email Server (SMTP relay)
         ├─→ Microsoft Entra ID (Auth provider)
         ├─→ Microsoft Graph API (User sync)
         ├─→ Ellucian Ethos API (Banner data)
         ├─→ Mindrouter AI (Invoice processing)
         └─→ Cisco Duo (MFA)

Background Worker (RQ + Redis)
   └─→ Invoice processing jobs
   └─→ Async task queue management
```

### **Key Architectural Principles**

1. **Modular Design**: Each domain module (Auth, AP, Payroll, Preaward) is independently deployable with its own API, service layer, and database schema.
2. **Separation of Concerns**: Three-tier layering (API → Service → Data Access) ensures clean boundaries and testability.
3. **Secured by Default**: All endpoints use role-based access control (RBAC) inherited from Entra ID group memberships.
4. **Scalable Backend**: FastAPI with Gunicorn/Uvicorn workers, horizontal scaling via Kubernetes, connection pooling for databases.
5. **Real-time Observability**: OpenTelemetry instrumentation across HTTP, database, and Redis components with Jaeger visualization.

---

## **Technology Stack**

### **Backend**
| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Framework** | FastAPI | 0.135.1 | Async web framework with auto-documentation |
| **ASGI Server** | Uvicorn | 0.41.0 | Fast ASGI server for production |
| **App Server** | Gunicorn | 25.1.0 | Process manager for multiple workers |
| **ORM** | SQLAlchemy | 2.0.48 | Object-relational mapping for PostgreSQL |
| **Migrations** | Alembic | 1.18.4 | Schema versioning and migrations |
| **Auth / JWT** | PyJWT, Cryptography | 2.12.0, 46.0.5 | JWT token generation & verification |
| **OAuth2** | Authlib, MSAL | 1.6.9, 1.35.1 | Microsoft Entra ID integration |
| **Microsoft Graph** | msgraph-sdk | 1.55.0 | User sync and group membership queries |
| **Task Queue** | RQ | 2.7.0 | Background job processing with Redis |
| **Email** | aiosmtplib | 5.1.0 | Async SMTP for email notifications |
| **Validation** | Pydantic | 2.12.5 | Data validation and serialization |
| **Observability** | OpenTelemetry | 1.40.0 | Tracing and metrics instrumentation |

### **Frontend**
| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Framework** | React | 18.3.1 | Component-based UI library |
| **Build Tool** | Vite | 6.3.5 | Lightning-fast build tool and dev server |
| **Routing** | React Router | 7.6.2 | Client-side routing and navigation |
| **UI Components** | React Bootstrap, Mantine | Latest | Pre-built, accessible UI components |
| **Forms** | Pydantic validation (backend) | — | Client-side form handling |
| **HTTP Client** | Axios | 1.13.2 | Promise-based HTTP requests with interceptors |
| **State Management** | Context API + React Hooks | — | Built-in React state management |
| **Data Fetching** | TanStack React Query | 5.90.11 | Server state management and caching |
| **Rich Text Editor** | Mantine Editor, Tiptap | Latest | Markdown and WYSIWYG editing |
| **PDF Viewer** | pdfjs-dist | 5.5.207 | Client-side PDF rendering |

### **Database & Persistence**
| Service | Technology | Version | Purpose |
|---------|-----------|---------|---------|
| **Primary DB** | PostgreSQL | 17 | ACID-compliant relational database |
| **Caching & Queue** | Redis | Latest | In-memory cache and task queue |
| **Schema Mgmt** | Alembic | — | Database migration management |

### **Infrastructure & DevOps**
| Service | Technology | Purpose |
|---------|-----------|---------|
| **Container Runtime** | Docker | Multi-stage builds for backend, frontend, worker |
| **Orchestration** | Kubernetes on OCI | Container management and scaling |
| **CI/CD Pipeline** | Azure Pipelines | Build, test, and deployment automation |
| **Monitoring** | OpenTelemetry Collector + Jaeger | Distributed tracing |
| **Security** | Cisco Duo MFA | Multi-factor authentication and device trust |

---

## **Core Modules**

### **1. Authentication & Authorization Module**

#### **Purpose**
The Auth module is a **fixed, required foundation** that secures the entire application. It handles user identity verification, role-based access control (RBAC), session management, and integration with enterprise identity providers (Microsoft Entra ID).

#### **Key Features**

- **OAuth2 Authorization Code Flow**: Users authenticate via Entra ID, which returns an authorization code. The backend exchanges this code for tokens (access token, ID token, refresh token) using client credentials.
- **JWT Token Management**: 
  - Short-lived access tokens (embedded with user roles)
  - Long-lived refresh tokens (stored in PostgreSQL with secure HttpOnly cookies)
- **Role-Based Access Control (RBAC)**: User roles are dynamically pulled from Entra ID group memberships and cached. Module-specific roles (e.g., `payroll.viewer`, `ap.admin`, `preaward.analyst`) are assigned based on group membership.
- **Multi-Factor Authentication (MFA)**: Conditional Access policies in Entra ID trigger Cisco Duo authentication for high-risk operations.
- **Device Trust Validation**: Duo Desktop validates device posture before allowing access.
- **Token Refresh Flow**: Expired access tokens are automatically refreshed using the refresh token without user re-authentication.
- **Logout & Session Revocation**: Refresh tokens are revoked from the database; JWT tokens are invalidated.

#### **Data Models**

```python
# User (stored in PostgreSQL - auth schema)
class AuthUser:
    id: int              # Unique identifier
    email: str           # Entra ID email (unique)
    name: Optional[str]  # Full name from Entra ID
    roles: List[Role]    # Dynamically fetched from Microsoft Graph
    created_at: datetime # Account creation timestamp
    last_login: datetime # Last successful login

# RefreshToken (for session management)
class RefreshToken:
    id: int
    user_id: int         # Foreign key to User
    token: str           # Opaque random token
    expiry: datetime     # Token expiration
    created_at: datetime
    revoked: bool        # Soft deletion flag
```

#### **API Endpoints**

| Endpoint | Method | Purpose | Access |
|----------|--------|---------|--------|
| `/api/auth/login` | GET | Initiates OAuth2 flow | Public |
| `/api/auth/logout` | POST | Revokes session | Authenticated |
| `/api/auth/auth` | GET | OAuth2 callback (receives auth code) | Public |
| `/api/auth/user` | GET | Fetch current user info | Authenticated |
| `/api/auth/token` | POST | Refresh access token | Cookie-based |
| `/api/auth/graph-callback` | GET | Graph token bootstrap (admin only) | Restricted |

#### **Security Flow (Simplified)**

```
User Login Request
    ↓
Authlib generates authorize URL (low risk)
    ↓
User redirects to Entra ID (user enters credentials)
    ↓
Conditional Access triggers Duo MFA + device trust check
    ↓
Entra ID returns authorization code to backend callback
    ↓
Backend exchanges code for tokens (using client secret)
    ↓
Backend calls Microsoft Graph to fetch user groups
    ↓
Groups filtered against AUTH_ALLOWED_GROUPS allowlist
    ↓
JWT access token created with filtered roles embedded
    ↓
Refresh token stored in PostgreSQL
    ↓
Two HttpOnly cookies set: access_token, refresh_token
    ↓
User logged in with session established
```

#### **Module Structure**
```
backend/app/modules/auth/
├── api/
│   └── routes.py              # All auth endpoints
├── models/
│   ├── refresh_token.py        # RefreshToken ORM model
│   └── user.py                 # User ORM model
├── services/
│   ├── auth_services.py        # Authentication logic
│   ├── jwt_services.py         # JWT creation/verification
│   └── graph_role_service.py   # Microsoft Graph integration
├── db.py                       # Database connection & session
└── alembic/
    └── versions/               # Database migrations
```

---

### **2. Accounts Payable (AP) Module**

#### **Purpose**
The AP module automates invoice processing and validation using AI-assisted document extraction and data validation against authoritative university data sources. It transforms manual invoice handling into a sophisticated, audit-able, and ML-enhanced workflow.

#### **Key Features**

1. **Invoice Ingestion**:
   - emails with invoices are captured via **Microsoft Graph webhook notifications** from a designated Outlook mailbox
   - Fallback SMTP relay path for non-Graph email sources
   - Automatic deduplication using Graph message IDs (`graph_ingest_id`)

2. **Email & Document Parsing**:
   - Extracts email metadata (subject, sender, date, recipients)
   - Parses PDF, image, and text attachments
   - Stores attachments with metadata (filename, size, content type)

3. **AI-Assisted Classification & Field Extraction**:
   - Uses **Qwen2.5-VL** (vision-language model) to classify documents and extract invoice fields
   - Extracted fields include: vendor name, invoice date, due date, PO number, invoice number, total amount, payment terms, etc.
   - Confidence scores attached to each extraction
   - Complex invoice layouts handled via multimodal AI processing

4. **Data Validation**:
   - Validates extracted data against **Ellucian Ethos API** (Banner system) for vendor, PO, and invoice matching
   - Fuzzy matching for vendor names to handle variations
   - Multi-field cross-validation for consistency

5. **Content Flagging & Task Generation**:
   - Flags suspicious invoices (foreign vendors, missing PO, overdue, etc.)
   - Generates workflow tasks assigning invoices to responsible parties
   - Tracks invoice status: `in_processing`, `needs_review`, `validated`, `processed`

#### **Data Models**

```python
# ApInvoice (core invoice record)
class ApInvoice:
    id: int                              # Primary key
    collection: str                      # "raw" or "processed"
    graph_ingest_id: str                 # Microsoft Graph message ID (unique)
    status: str                          # in_processing, needs_review, validated, etc.
    assigned_to: str                     # Email of responsible user
    is_invoice: bool                     # Classification result (true/false/null)
    filter_flag: bool = False            # Flagged for manual review
    filter_reason: Optional[str]         # Reason for flag
    date_received: datetime              # Email receipt timestamp
    
    # JSON storage for complex nested data
    email_data: dict                     # {subject, body, sender, recipients, date}
    invoice_data: dict                   # {vendor, amount, date, po_number, terms, ...}
    validation_metadata: dict            # {found_in_banner, pidm, fuzzy_match, ...}
    classification_data: dict            # {classification, confidence, explanation}

# ApInvoiceEvent (immutable event log)
class ApInvoiceEvent:
    id: int
    invoice_id: int                      # FK to ApInvoice
    event: str                           # created, extracted, validated, processed
    event_reason: str                    # Detail or reason for event
    date_of_event: datetime              # When event occurred
    identity: str                        # User who triggered event

# Email (represents email envelope)
class Email:
    id: str                              # Microsoft Graph message ID
    subject: str
    body: str
    date_email_received: datetime
    sender: str
    recipients: List[str]
    attachments: List[Attachment]        # Files in email

# LLM Field Extraction Result
class InvoiceExtraction:
    invoice_number: str
    invoice_date: date
    invoice_due_date: date
    invoice_total_amount: Decimal
    vendor_name: str
    po_number: str
    payment_terms: str
    currency: str
    # ... + reasoning for each field
    confidence: str                      # "high", "mid", "low"
```

#### **API Endpoints**

| Endpoint | Method | Purpose | Parameters |
|----------|--------|---------|-----------|
| `/api/ap/invoices` | GET | List invoices with filters | status, collection, assigned_to |
| `/api/ap/invoices/{id}` | GET | Fetch single invoice | — |
| `/api/ap/invoices/{id}` | PATCH | Update invoice status | status, assigned_to, filter_flag |
| `/api/ap/invoices/{id}/events` | GET | Fetch invoice event log | — |
| `/api/ap/validate/{id}` | POST | Trigger validation against Ethos API | — |
| `/api/ap/process/{id}` | POST | Submit invoice to processing queue | — |

#### **Processing Pipeline**

```
Step 1: Email Ingestion
    └─→ Microsoft Graph webhook receives email
    └─→ Email + attachments parsed and stored
    └─→ Deduplication check (graph_ingest_id)

Step 2: AI Classification & Extraction
    └─→ Qwen2.5-VL analyzes PDF/images
    └─→ Classifies as "invoice" or "non-invoice"
    └─→ Extracts fields (vendor, date, amount, PO, etc.)
    └─→ Stores extraction in invoice_data (JSONB)

Step 3: Data Validation
    └─→ Ethos API lookup for vendor PIDM
    └─→ Fuzzy matching for vendor names
    └─→ PO number validation
    └─→ Cross-field consistency checks
    └─→ Stores validation results in validation_metadata

Step 4: Flagging & Review
    └─→ Suspicious patterns detected (foreign vendor, overdue, etc.)
    └─→ Invoice flagged with reason
    └─→ Assigned to workflow user for manual review

Step 5: Event Tracking
    └─→ Each step creates an ApInvoiceEvent record
    └─→ Immutable audit trail
    └─→ Queryable event log for reporting
```

#### **Module Structure**
```
backend/app/modules/accountspayable/
├── api/
│   └── routes.py                       # AP endpoints
├── models/
│   ├── ap_invoice.py                   # ApInvoice ORM model
│   ├── ap_invoice_event.py             # ApInvoiceEvent ORM model
│   └── schemas.py                      # Pydantic request/response models
├── services/
│   ├── invoice_services.py             # CRUD operations for invoices
│   ├── extraction_services.py          # Qwen2.5-VL integration
│   ├── validation_services.py          # Ethos API integration
│   └── queue_services.py               # Redis task queue
├── db.py                               # Database connection
└── invoice_processing/
    ├── config.py                       # Model configs (Qwen, OpenAI)
    └── redis_worker.py                 # RQ worker for async jobs
```

---

### **3. Payroll Module**

#### **Purpose**
The Payroll module manages **Retroactive Pay Requests (RPR)** — a complex workflow for university employees to claim additional compensation for previously unpaid work. The module implements comprehensive form validation, attachment management, and multi-stage approval workflows.

#### **Key Features**

1. **Retroactive Pay Request (RPR) Management**:
   - Employees submit forms with personal information, pay period, hours, rate, and amount
   - Form validation (required fields, numeric constraints, character limits)
   - Status tracking: `pending` → `needs-revision` → `approved` → `paid` or `canceled`
   - Supports bulk edits by admin users

2. **Attachment Management**:
   - Employees attach supporting documents (timesheets, receipts, proof of work)
   - Files stored in **MongoDB GridFS** for scalability
   - File metadata tracked in PostgreSQL with binary content hashed for deduplication
   - Secure JWT-based download tokens with time-limited access
   - File streaming for large attachments

3. **Workflow Approval**:
   - Employees submit requests (status: `pending`)
   - Payroll assistants review and approve/reject with comments (status: `approved` or `needs-revision`)
   - Admins mark as paid (status: `paid`) and handle cancellations
   - Audit trail tracks all status changes and who made them

4. **Role-Based Access**:
   - **Employee**: Submit own requests, view own requests, edit requests in `needs-revision` status
   - **Payroll Assistant**: View all requests, approve/reject, request revisions, view attachments
   - **Payroll Admin**: Perform all Payroll Assistant actions + edit user roles and permissions

#### **Data Models**

```python
# RPRForm (Retroactive Pay Request)
class RPRForm:
    id: int
    # Employee info
    employee_name: str
    employee_v_number: str
    employee_email: str
    employee_type: str                   # Faculty, Classified, Exempt, etc.
    department: str
    
    # Pay details
    pay_period: str
    hours: Decimal                       # Hours claimed
    rate: Decimal                        # Hourly rate
    amount: Decimal                      # hours * rate
    reason: str                          # Reason for retroactive pay
    
    # Workflow
    status: str                          # pending, needs-revision, approved, paid, canceled
    submitted_by: str                    # Employee email
    assigned_to: str                     # Payroll assistant email
    approver: Optional[str]              # Email of approver
    reviewer_comment: Optional[str]      # Reason for revision/rejection
    
    # Audit
    created_at: datetime
    updated_at: datetime

# Attachment (file storage metadata)
class Attachment:
    id: int
    rpr_form_id: int                     # FK to RPRForm
    filename: str
    content_type: str                    # application/pdf, etc.
    size_bytes: int
    content_hash: str                    # SHA-256 for deduplication
    gridfs_id: ObjectId                  # MongoDB GridFS object ID
    upload_time: datetime
    uploaded_by: str                     # Uploader email

# User (payroll module variant)
class PayrollUser:
    id: int
    email: str                           # University email
    name: str
    is_admin: bool                       # Admin privileges
    is_active: bool                      # Account status
    created_at: datetime
```

#### **API Endpoints**

| Endpoint | Method | Purpose | Parameters |
|----------|--------|---------|-----------|
| `/api/payroll/rpr_forms` | GET | List RPR forms | status, submitter_email, search |
| `/api/payroll/rpr_forms` | POST | Create new RPR form | form_data (JSON) |
| `/api/payroll/rpr_forms/{id}` | GET | Fetch single RPR form | — |
| `/api/payroll/rpr_forms/{id}` | PATCH | Update RPR form | updated_fields |
| `/api/payroll/rpr_forms/{id}` | DELETE | Delete RPR form | — |
| `/api/payroll/attachments` | POST | Upload attachment | file (multipart) |
| `/api/payroll/attachments/{id}` | DELETE | Delete attachment | — |
| `/api/payroll/attachments/by_form/{form_id}` | GET | List attachments for form | — |
| `/api/payroll/attachments/download` | GET | Download file | token (JWT) |
| `/api/payroll/users` | GET/POST/PATCH | Manage payroll users | role-restricted |

#### **Workflow Example**

```
Employee Submits Request
    ↓ (POST /api/payroll/rpr_forms with form data)
    ↓
Request stored with status="pending"
    ↓
Employee uploads supporting documents (attachments)
    ↓ (POST /api/payroll/attachments with file + form_id)
    ↓
Attachments stored in MongoDB GridFS
    ↓
Payroll Assistant reviews in dashboard
    ↓
Approves or requests revision (PATCH /api/payroll/rpr_forms/{id})
    ↓ (status="approved" or "needs-revision")
    ↓
If approved: Payroll Admin marks paid (status="paid")
    ↓
Audit trail records: who changed it, when, and why
```

#### **Module Structure**
```
backend/app/modules/payroll/
├── api/
│   └── routes/
│       ├── rpr_form_routes.py          # Form CRUD endpoints
│       └── attachment_routes.py        # File upload/download endpoints
├── models/
│   ├── rpr_form.py                     # RPRForm ORM model
│   ├── attachment.py                   # Attachment ORM model
│   └── user.py                         # PayrollUser ORM model
├── services/
│   ├── rpr_form_services.py            # Form business logic
│   └── rpr_attachment_services.py      # File management and JWT tokens
├── db.py                               # Database connection
└── alembic/
    └── versions/                       # Schema migrations
```

---

### **4. Preaward Module**

#### **Purpose**
The Preaward module streamlines the **pre-award proposal process** at the university. It automates deadline calculations for submission documents, manages task assignments, and provides real-time visibility into proposal status across different stages.

#### **Key Features**

1. **Due Date Calculator**:
   - Analyzes funding agency requirements and proposal submission deadlines
   - Calculates subsidiary document deadlines (budget justification, narrative, letters of commitment, etc.)
   - Accounts for university processing times and institutional review requirements
   - Generates email templates for Principal Investigators (PIs) and Department Grant Administrators (DGAs)

2. **Proposal Management**:
   - Create new proposals with metadata (title, funding agency, submission date, budget)
   - Track proposal lifecycle stages (in-progress, submitted, funded, declined)
   - Assign Sponsor Program Administrator (SPA) to each proposal
   - Bulk edit capabilities for admin users

3. **Task Management (SPA Taskboard)**:
   - Create, update, and delete tasks for each proposal
   - Task fields: description, deadline, status, assigned to, priority, notes
   - Task filtering by status (pending, in-progress, completed, overdue)
   - Visual indicators for overdue tasks and deadline proximity
   - Task history and status change tracking

4. **User & Role Management**:
   - Role-based access: Preaward Analysts, Preaward Admins
   - User management interface for admins (add, edit, deactivate users)
   - Role-based visibility of proposals and tasks

#### **Data Models**

```python
# Proposal
class Proposal:
    id: int
    title: str                           # Proposal title
    funding_agency: str                  # Sponsor name (NSF, NIH, etc.)
    principal_investigator: str          # PI email
    submission_deadline: datetime        # When proposal due to sponsor
    estimated_amount: Decimal            # Budget amount
    status: str                          # in-progress, submitted, funded, declined
    
    # Assignments
    assigned_spa: str                    # SPA email
    assigned_dga: str                    # DGA email (optional)
    department: str                      # Department code
    
    # Audit
    created_by: str                      # Analyst email
    created_at: datetime
    updated_at: datetime
    notes: Optional[str]                 # Internal notes

# Task
class Task:
    id: int
    proposal_id: int                     # FK to Proposal
    title: str                           # Task description
    deadline: datetime                   # When task due
    status: str                          # pending, in-progress, completed, overdue
    priority: str                        # low, medium, high
    assigned_to: str                     # User email
    
    # Details
    description: Optional[str]           # Detailed description
    notes: Optional[str]                 # Comments
    
    # Audit
    created_by: str
    created_at: datetime
    completed_at: Optional[datetime]

# Deadline (calculated based on submission date)
class CalculatedDeadline:
    document_type: str                   # budget, narrative, letters, etc.
    days_before_submission: int          # How many days before submission
    deadline_date: datetime              # Calculated deadline
    notes: str                           # Rationalε for deadline
```

#### **API Endpoints**

| Endpoint | Method | Purpose | Parameters |
|----------|--------|---------|-----------|
| `/api/preaward/deadline` | GET | Calculate document deadlines | submission_deadline |
| `/api/preaward/proposals` | GET | List proposals | status, assigned_spa, search |
| `/api/preaward/proposals` | POST | Create proposal | proposal_data |
| `/api/preaward/proposals/{id}` | GET | Fetch proposal details | — |
| `/api/preaward/proposals/{id}` | PATCH | Update proposal | updated_fields |
| `/api/preaward/proposals/{id}/tasks` | GET | List tasks for proposal | — |
| `/api/preaward/tasks` | POST | Create task | task_data |
| `/api/preaward/tasks/{id}` | PATCH | Update task | updated_fields |
| `/api/preaward/tasks/{id}` | DELETE | Delete task | — |
| `/api/preaward/users` | GET/POST/PATCH/DELETE | Manage preaward users | role-restricted |

#### **Workflow Example**

```
Preaward Analyst determines submission deadline
    ↓
Uses Due Date Calculator to compute subsidiary deadlines
    ↓ (GET /api/preaward/deadline?submission_deadline=2025-05-01)
    ↓
Calculator returns dates for budget, narrative, commitment letters
    ↓
Analyst emails PIs/DGAs with the calculated deadlines
    ↓
Analyst creates proposal in system (POST /api/preaward/proposals)
    ↓
System automatically creates task list based on deadline pattern
    ↓
SPA (Sponsor Program Administrator) assigned to proposal
    ↓
SPA views SPA Taskboard with all assigned proposals
    ↓
SPA manages task status, notes, and completion
    ↓
Real-time dashboard shows overdue tasks and upcoming deadlines
    ↓
Admin performs bulk operations, user management
```

#### **Module Structure**
```
backend/app/modules/preaward/
├── api/
│   └── routes/
│       ├── deadline_routes.py          # Due date calculator
│       ├── proposal_routes.py          # Proposal CRUD
│       └── task_routes.py              # Task management
├── models/
│   ├── proposal.py                     # Proposal ORM model
│   ├── task.py                         # Task ORM model
│   └── user.py                         # PreawardUser ORM model
├── services/
│   ├── proposal_services.py            # Proposal logic
│   ├── task_services.py                # Task management
│   └── deadline_services.py            # Deadline calculation
├── db.py                               # Database connection
└── alembic/
    └── versions/                       # Schema migrations
```

---

## **Frontend Architecture**

### **Technology Stack**

- **Framework**: React 18.3.1 (functional components with hooks)
- **Build Tool**: Vite 6.3.5 (lightning-fast build and HMR)
- **Routing**: React Router 7.6.2 (client-side navigation)
- **UI Library**: React Bootstrap + Mantine (pre-built accessible components)
- **HTTP Client**: Axios (with interceptors for auth and error handling)
- **State Management**: Context API + React Hooks (Auth, Toast, Confirmation modals)
- **Data Fetching**: TanStack React Query (server state caching, refetching)
- **Rich Text**: Mantine RichTextEditor + Tiptap (markdown support)
- **PDF Viewer**: pdfjs-dist (client-side rendering)
- **Testing**: Jest + Vitest, React Testing Library

### **Project Structure**

```
frontend/
├── src/
│   ├── main.jsx                        # Entry point
│   ├── App.jsx                         # Root component with routing
│   ├── App.css                         # Global styles
│   ├── index.css                       # Base styles
│   │
│   ├── api/
│   │   └── apiClient.js                # Axios instance with interceptors
│   │
│   ├── components/                     # Shared components
│   │   ├── Authorization.jsx           # Role-based component wrapper
│   │   ├── Footer.jsx
│   │   ├── IdleWarningModal.jsx        # Idle timeout warning
│   │   ├── Logout.jsx
│   │   ├── PageNotFound.jsx
│   │   ├── PlaceHolderPage.jsx
│   │   ├── protectedRoutes.jsx         # Route protection HOC
│   │   └── Sidebar.jsx                 # Main navigation
│   │
│   ├── contexts/                       # Global context providers
│   │   ├── authContext.jsx             # User auth state
│   │   ├── ConfirmationContext.jsx     # Modal confirmations
│   │   └── ToastContext.jsx            # Toast notifications
│   │
│   ├── hooks/                          # Custom React hooks
│   │   ├── useAuthorization.jsx        # Role checking utilities
│   │   └── useIdleTimer.js             # Idle session timeout
│   │
│   ├── models/
│   │   └── user.js                     # User class for type safety
│   │
│   ├── pages/
│   │   └── Dashboard.jsx               # Main dashboard page
│   │
│   ├── UI/                             # Reusable UI components
│   │   ├── Accordioan.jsx              # Accordion component
│   │   ├── customToast.jsx             # Toast styling
│   │   ├── Date.jsx                    # Date picker
│   │   ├── Dropdown.jsx                # Dropdown selector
│   │   ├── ManageUserView.jsx          # User management UI
│   │   ├── Markdown.jsx                # Markdown viewer
│   │   ├── Modal.jsx                   # Generic modal
│   │   ├── ReusableToolTip.jsx         # Tooltip wrapper
│   │   ├── SearchBar.jsx               # Search input
│   │   └── Time.jsx                    # Time picker
│   │
│   ├── modules/                        # Domain-specific modules
│   │   ├── payroll/
│   │   │   ├── api/                    # Payroll API calls
│   │   │   ├── components/             # Payroll components
│   │   │   ├── contexts/               # Payroll-specific context
│   │   │   ├── hooks/                  # Payroll hooks
│   │   │   ├── models/                 # Data models
│   │   │   ├── pages/                  # Pages (forms, dashboards)
│   │   │   └── utils/                  # Utilities
│   │   │
│   │   ├── preaward/
│   │   │   ├── api/
│   │   │   ├── components/
│   │   │   ├── contexts/
│   │   │   ├── pages/
│   │   │   └── utils/
│   │   │
│   │   └── accountpayable/
│   │       ├── api/
│   │       ├── components/
│   │       ├── pages/
│   │       └── utils/
│   │
│   └── utils/
│       ├── api.js                      # Generic API call wrappers
│       ├── Query.jsx                   # useQuery wrapper
│       └── [other utilities]
│
├── public/
│   ├── email-template.json             # Email templates
│   └── ap-email-template.json
│
├── package.json                        # NPM dependencies
├── vite.config.js                      # Vite configuration
├── eslint.config.js                    # ESLint rules
└── index.html                          # HTML entry point
```

### **Key Frontend Features**

#### **Authentication & Authorization**
- **Auth Context**: Manages current user, login/logout, token refresh
- **Protected Routes**: HOC that redirects unauthenticated users
- **Authorization Hook**: `useAuthorization()` provides role checking
- **Idle Session Timeout**: Auto-logout after 15 minutes of inactivity with warning at 14 minutes

#### **API Integration**
- **Axios Interceptors**: Auto-attach JWT tokens, handle 401 responses with token refresh
- **React Query**: Caching, refetching, stale-while-revalidate strategies
- **Error Handling**: Centralized error responses shown as Toast notifications
- **Loading States**: Components handle async statuses (loading, error, success)

#### **UI/UX Patterns**
- **Toast Notifications**: Non-intrusive feedback for user actions
- **Confirmation Modals**: Prevent accidental deletions with confirmation dialogs
- **Form Validation**: Pydantic backend validation errors displayed to users
- **Loading Spinners**: Visual feedback during async operations
- **Responsive Design**: Mobile-first approach with Bootstrap grid

#### **Module-Specific Components**

**Payroll**:
- RPR Form creation and submission
- My Requests page with filtering and search
- File upload with drag-and-drop
- Attachment download with JWT tokens
- Payroll Assistant dashboard with status updates

**Preaward**:
- Due Date Calculator with dynamic deadline computation
- Proposal list with sorting and filtering
- SPA Taskboard with color-coded task status
- Task details modal with edit capabilities
- User/role management interface

**Accounts Payable**:
- Invoice list with advanced filtering (status, collection, assigned_to)
- Invoice detail view with extracted data and validation results
- Event log viewer for audit trail
- Manual flagging interface for review

---

## **Backend Architecture**

### **Layered Architecture**

#### **1. API Layer (Routes)**
- **Purpose**: Define HTTP endpoints, validate requests, return responses
- **Implementation**: FastAPI routers with Pydantic models for serialization
- **Security**: All endpoints require authentication via `get_current_user` dependency
- **Error Handling**: Custom exception handlers convert business logic errors to HTTP responses

Example:
```python
from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/api/rpr_forms", tags=["Payroll"])

@router.get("/")
async def list_forms(
    status: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    # Delegate to service layer
    return rpr_form_services.get_rpr_forms(db, current_user, status)
```

#### **2. Service Layer (Business Logic)**
- **Purpose**: Implement domain rules, orchestrate database operations, integrate with external APIs
- **Implementation**: Standalone Python functions or classes with clear responsibilities
- **Validation**: Check permissions, validate input data, enforce business rules
- **Transactions**: Ensure data consistency across multiple operations

Example:
```python
def create_rpr_form(
    form_data: RPRFormCreate,
    db: Session,
    current_user: AuthUser
) -> RPRForm:
    # Validate permissions (must be employee or admin)
    if not is_authorized(current_user, form_data.employee_email):
        raise AuthorizationError("Cannot create RPR for other users")
    
    # Validate business rules
    if form_data.hours < 0 or form_data.rate < 0:
        raise ValidationError("Hours and rate must be non-negative")
    
    # Create record
    rpr_form = RPRForm(
        employee_name=form_data.employee_name,
        hours=form_data.hours,
        rate=form_data.rate,
        amount=form_data.hours * form_data.rate,
        status="pending",
        submitted_by=current_user.email
    )
    
    db.add(rpr_form)
    db.commit()
    db.refresh(rpr_form)
    
    return rpr_form
```

#### **3. Data Access Layer (Models & Queries)**
- **Purpose**: Abstract database operations using SQLAlchemy ORM
- **Implementation**: ORM models with relationships and constraints
- **Query Optimization**: Join paths, eager loading, indexes for common queries
- **Soft Deletes**: Records marked as deleted but not removed (for audit trails)

Example:
```python
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from app.modules.payroll.db import Base

class RPRForm(Base):
    __tablename__ = "rpr_form"
    __table_args__ = {"schema": "payroll"}
    
    id = Column(Integer, primary_key=True)
    employee_name = Column(String(100), nullable=False)
    hours = Column(Numeric(10, 2), nullable=False)
    rate = Column(Numeric(10, 2), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(20), default="pending")
    submitted_by = Column(String(100), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    attachments = relationship("Attachment", back_populates="rpr_form")
```

### **Database Design**

#### **PostgreSQL Schema Organization**

Nexus uses **multiple schemas** within a single PostgreSQL database for logical separation:

```
┌─ nexus (main database)
│
├─ public                          # auth module
│  ├─ auth_user (users)
│  ├─ refresh_token
│  └─ [auth tables]
│
├─ accounts_payable                # AP module
│  ├─ ap_invoice
│  ├─ ap_invoice_event
│  └─ [AP tables]
│
├─ payroll                         # Payroll module
│  ├─ rpr_form
│  ├─ attachment
│  ├─ payroll_user
│  └─ [Payroll tables]
│
└─ preaward                        # Preaward module
   ├─ proposal
   ├─ task
   ├─ preaward_user
   └─ [Preaward tables]
```

#### **Alembic Migrations**

Each module has an independent Alembic migration folder:

```
backend/app/modules/{module_name}/alembic/
├── env.py                              # Environment config
├── script.py.mako                      # Migration template
└── versions/
    ├── {hash}_{name}.py                # Initial schema
    └── {hash}_{name}.py                # Incremental changes
```

Migrations are executed during deployment to ensure schema consistency.

### **Cross-Module Services**

#### **Common Email Service**
- **Location**: `app/common/services/email_services.py`
- **Purpose**: Send transactional emails (notifications, approvals, resets)
- **Implementation**: Async SMTP using `aiosmtplib`
- **Features**:
  - Template rendering with Jinja2
  - Attachment support
  - HTML and plain text versions
  - Retry logic for failed sends

```python
async def send_email(
    subject: str,
    body: str,
    sender: EmailStr,
    recipients: List[EmailStr],
    mail_configuration: MailSettings,
    attachments: Optional[List[Attachment]] = None,
    template_name: Optional[str] = None,
) -> MessageResponse:
    # Render template if provided
    if template_name:
        body = render_template(template_name, context=body)
    
    # Send via SMTP
    async with aiosmtplib.SMTP(
        hostname=mail_configuration.MAIL_SERVER,
        port=mail_configuration.MAIL_PORT,
        use_tls=mail_configuration.MAIL_STARTTLS
    ) as smtp:
        message = create_email_message(subject, body, sender, recipients, attachments)
        await smtp.send_message(message)
    
    return MessageResponse(message="Email sent successfully")
```

#### **JWT & Token Services**
- **Location**: `app/common/services/jwt_services.py`
- **Purpose**: Generate and verify JWT tokens for authentication and file downloads
- **Features**:
  - HS256 symmetric algorithm (using API secret key)
  - Embedded role claims
  - Configurable expiration (access vs refresh tokens)

```python
def create_access_token(user: AuthUser, expires_delta: timedelta = None) -> str:
    to_encode = {
        "sub": str(user.id),
        "email": user.email,
        "roles": [role.role_name for role in user.roles],
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc) + (expires_delta or timedelta(hours=1))
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ExpiredOrInvalidTokenError("Invalid token")
```

---

## **Data Persistence Layer**

### **PostgreSQL (Primary Relational Database)**

**Role**: Main transactional data store for all business entities

**Connection Details**:
- **Host**: OCI Private VCN (not internet-accessible)
- **Port**: 5432
- **Database**: `nexus`
- **Authentication**: Username/password with TLS encryption

**Key Characteristics**:
- ACID-compliant transactions
- Connection pooling (configured in FastAPI dependencies)
- Automated backups (OCI native backup service)
- Read replicas for scaling (future enhancement)

**Modules' Tables**:
- **Auth Schema**: `auth_user`, `refresh_token`
- **AP Schema**: `ap_invoice`, `ap_invoice_event`
- **Payroll Schema**: `rpr_form`, `attachment` (metadata), `payroll_user`
- **Preaward Schema**: `proposal`, `task`, `preaward_user`

### **Redis (Cache & Task Queue)**

**Role**: In-memory cache and distributed task queue for background jobs

**Purpose**:
1. **Caching**: Reduces database queries for frequently accessed data (user roles, configuration)
2. **Task Queue**: Powered by RQ (Redis Queue) for async job processing
3. **Session Storage** (optional): Short-term session state

**Key Jobs**:
- **AP Invoice Processing**: Qwen2.5-VL extraction and Ethos API validation (long-running)
- **Email Notifications**: Async email sends triggered by business events
- **Report Generation**: Batch exports and analytics queries

**Configuration**:
```python
from redis import Redis

redis_client = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    password=os.getenv("REDIS_PASSWORD"),
    db=0
)

# RQ Worker
from rq import Worker

worker = Worker(['default'], connection=redis_client)
worker.work()
```

---

## **CI/CD & Deployment Pipeline**

### **Overview**

Nexus uses **Azure Pipelines** for continuous integration and deployment. The system is designed for zero-downtime deployments to Oracle Cloud Infrastructure (OCI) Kubernetes clusters.

### **Pipeline Structure**

#### **3 Independent Pipelines**

Each component has a separate pipeline for independent deployment:

1. **Backend Pipeline** (azure-pipelines-back.yaml)
2. **Frontend Pipeline** (azure-pipelines-front.yaml)
3. **Worker Pipeline** (azure-pipelines-worker.yaml)

#### **Trigger Strategy**

```yaml
trigger:
  branches:
    include:
    - sprint/*              # Feature/sprint branches
    - test                  # Testing branch
    - main                  # Production ready
    exclude:
    - story/*               # Story branches don't trigger
    - task/*                # Task branches don't trigger
    - bug/*                 # Bug branches don't trigger
    - hotfix/*              # Hotfix branches (manual)
```

### **Pipeline Stages**

Each pipeline follows this high-level flow:

```
┌────────────────────────────────────────────────┐
│ 1. TRIGGER: Branch push (sprint/*, test, main) │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 2. CHECKOUT: Pull code from git repo           │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 3. BUILD: Compile/bundle application           │
│   - Backend: Resolve Python deps, test         │
│   - Frontend: npm install, npm run build       │
│   - Worker: Python deps, test                  │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 4. TEST: Run automated tests                   │
│   - Unit tests                                 │
│   - Integration tests                          │
│   - Code coverage validation                   │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 5. DOCKER: Build OCI-compatible image          │
│   - Multi-stage builds for optimization        │
│   - Tag with commit SHA + version              │
│   - Scan for vulnerabilities                   │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 6. REGISTRY: Push to container registry        │
│   - OCI Container Registry (OCIR)              │
│   - Image signed and scanned                   │
└────────────────┬───────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 7. DEPLOY: Push to Kubernetes clusters         │
│   - Dev/Test cluster (auto)                    │
│   - Prod cluster (manual approval)             │
│   - Rolling updates (zero-downtime)            │
└────────────────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────┐
│ 8. VERIFY: Post-deployment health checks       │
│   - Pod readiness probes                       │
│   - Smoke tests                                │
│   - Monitoring alerts                          │
└────────────────────────────────────────────────┘
```

### **Docker Multi-Stage Builds**

#### **Backend Dockerfile** (Dockerfile.backend)

```dockerfile
# ════════════════════════════════════════════════════
# 🧱 BUILD STAGE
# ════════════════════════════════════════════════════
FROM ghcr.io/astral-sh/uv:python3.13-trixie AS builder

WORKDIR /app
COPY backend/pyproject.toml backend/uv.lock ./
RUN touch README.md
# Install only production dependencies
RUN uv sync --no-default-groups --group serve

# ════════════════════════════════════════════════════
# 🚀 RUNTIME STAGE
# ════════════════════════════════════════════════════
FROM python:3.13-slim-trixie AS runtime

WORKDIR /app

# Create non-root user (security best practice)
RUN addgroup --gid 1001 --system gunicorn && \
    adduser --uid 1001 --system gunicorn

# Copy virtual environment from builder
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Copy application code
COPY backend .

# Set permissions
RUN chown -R gunicorn:gunicorn /app

USER gunicorn

# Environment variables
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Run application
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app.main:app"]
```

**Key Optimizations**:
- **Two-stage build**: Final image only contains runtime dependencies, reducing size
- **Non-root user**: Gunicorn runs as unprivileged user (security hardening)
- **Minimal base image**: Python 3.13 slim saves ~200MB vs. full image
- **Layer caching**: Dependencies layer cached separately from code layer

#### **Frontend Dockerfile** (Dockerfile.frontend)

```dockerfile
# ════════════════════════════════════════════════════
# BUILD STAGE
# ════════════════════════════════════════════════════
FROM node:20-trixie AS builder

WORKDIR /app
COPY frontend/package.json package-lock.json ./
RUN npm ci

COPY frontend .
ENV NODE_ENV=production
RUN npm run build

# ════════════════════════════════════════════════════
# RUNTIME STAGE
# ════════════════════════════════════════════════════
FROM nginxinc/nginx-unprivileged:alpine

WORKDIR /app
COPY --from=builder /app/dist /usr/share/nginx/html
COPY frontend/server.conf /etc/nginx/conf.d/default.conf

EXPOSE 5173
```

**Key Features**:
- **Nginx unprivileged**: Runs as non-root (security)
- **Static assets only**: Final image contains only built artifacts (2-3MB)
- **Reverse proxy**: Nginx proxies /api/* requests to backend

### **Variables & Configuration**

Azure Pipeline variables are organized in template files:

**azure-vars-back.yml**:
```yaml
variables:
  imageName: 'nexus-backend'
  dockerfilePath: 'Dockerfile.backend'
  buildContext: 'backend/'
  
  # Registry
  registryServiceConnection: 'OCIR-Nexus'
  registry: 'phx.ocir.io/uidaho'
  
  # Deployment
  kubeClusterDev: 'OCI-Dev-Cluster'
  kubeClusterProd: 'OCI-Prod-Cluster'
```

### **Versioning & Tags**

Container images are tagged with:
- **Git commit SHA**: For traceability to exact code version
- **Version number**: From VERSION file (currently 1.3.4)
- **Branch name**: sprint/dev, test, main

Example:
```
phx.ocir.io/uidaho/nexus:backend-1.3.4-abc1234  # main branch build
phx.ocir.io/uidaho/nexus:backend-1.3.4-test     # test branch build
```

---

## **Observability & Monitoring**

### **OpenTelemetry Instrumentation**

Nexus uses OpenTelemetry to export distributed traces, metrics, and logs to Jaeger for real-time observability.

#### **Instrumentation Points**

1. **FastAPI**: Automatic HTTP request/response tracing
2. **SQLAlchemy**: Database query tracing with slow query detection
3. **Redis**: Cache and task queue operation tracing
4. **httpx**: Outbound HTTP calls (to Ethos API, Graph API, etc.)

#### **Configuration** (otel-collector-config.yaml)

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 10s
    send_batch_size: 512

exporters:
  jaeger:
    endpoint: http://jaeger:14250

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
```

#### **Backend Instrumentation** (`app/telemetry.py`)

```python
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor

def init_telemetry():
    # Set up trace provider
    otlp_exporter = OTLPSpanExporter(
        endpoint="http://otel-collector:4317"
    )
    trace.set_tracer_provider(TracerProvider())
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(otlp_exporter)
    )
    
    # Auto-instrument libraries
    FastAPIInstrumentor().instrument()
    SQLAlchemyInstrumentor().instrument(engine=engine)
    RedisInstrumentor().instrument()
```

### **Logging Strategy**

#### **Structured Logging** (`app/logger.py`)

```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(
    write_to_file: bool = True,
    logpath: str = LOG_PATH,
    filename: str = "backend.log",
    level=LOG_LEVEL
) -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    
    # Format: timestamp | level | module | message
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (rotating)
    if write_to_file:
        file_handler = RotatingFileHandler(
            filename=os.path.join(logpath, filename),
            maxBytes=10_000_000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
```

### **Local Development Stack** (docker-compose.yml)

For local development, developers can run the full Nexus stack locally:

```bash
# Start all services
docker compose up --build

# Services started:
# - PostgreSQL (5432)
# - Redis (6379)
# - OpenTelemetry Collector (4317, 4318)
# - Jaeger UI (16686)
# - Backend (8000)
# - Frontend (5173)
```

**Jaeger UI** (http://localhost:16686): Visualize distributed traces, search by service/operation, analyze latency.

---

## **Testing Strategy**

### **Backend Testing**

#### **Unit Tests** (tests)

Focus on individual functions and classes in isolation:

```python
# tests/test_entra_roles.py
def test_roles_are_included_in_access_token_and_can_be_decoded():
    jwt_services.SECRET_KEY = "test-secret"
    jwt_services.ALGORITHM = "HS256"
    
    user = SimpleNamespace(
        id=123, 
        email="user@example.com", 
        roles=["auth.admin", "payroll.viewer"]
    )
    token = jwt_services.create_access_token(user=user)
    
    payload = jwt_services.decode_token(token)
    assert payload["sub"] == "123"
    assert payload["email"] == "user@example.com"
    assert payload["roles"] == ["auth.admin", "payroll.viewer"]
```

#### **Integration Tests**

Test API endpoints against a real database (test database):

```python
# tests/test_payroll_api.py
@pytest.mark.asyncio
async def test_create_rpr_form(client, db_session, auth_headers):
    response = await client.post(
        "/api/payroll/rpr_forms",
        json={
            "employee_name": "John Doe",
            "hours": 10.0,
            "rate": 50.0,
            ...
        },
        headers=auth_headers
    )
    
    assert response.status_code == 201
    assert response.json()["status"] == "pending"
```

#### **Test Configuration**

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_entra_roles.py

# Run with verbose output
pytest -v
```

### **Frontend Testing**

#### **Component Tests** (payroll, `tests/preaward/`)

Test React components in isolation with mocked data:

```javascript
// tests/payroll/components/RPRForm.test.jsx
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import RPRForm from '../RPRForm';

test('submits RPR form with valid data', async () => {
  const mockNavigate = jest.fn();
  
  render(<RPRForm navigate={mockNavigate} />);
  
  const nameInput = screen.getByLabelText(/Employee Name/i);
  await userEvent.type(nameInput, 'John Doe');
  
  const submitButton = screen.getByRole('button', { name: /Submit/i });
  await userEvent.click(submitButton);
  
  await waitFor(() => {
    expect(mockNavigate).toHaveBeenCalledWith('/payroll/my-requests');
  });
});
```

#### **Integration Tests**

Test full user workflows with API mocking:

```javascript
// tests/payroll/integration/RPRWorkflow.test.jsx
jest.mock('../../api/payrollApi');

test('Employee can submit and view RPR request', async () => {
  // Setup
  const { getByRole, getByLabelText } = render(<PayrollModule />);
  
  // Create request
  const newButton = getByRole('button', { name: /New Request/i });
  fireEvent.click(newButton);
  
  // Fill form
  const employeeInput = getByLabelText(/Employee Name/i);
  fireEvent.change(employeeInput, { target: { value: 'Jane Doe' } });
  
  // Submit
  const submitButton = getByRole('button', { name: /Submit/i });
  fireEvent.click(submitButton);
  
  // Verify request appears in My Requests
  await waitFor(() => {
    expect(screen.getByText('Jane Doe')).toBeInTheDocument();
  });
});
```

#### **Test Runner Configuration** (jest.config.js)

```javascript
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setupTests.js'],
  testMatch: [
    '<rootDir>/tests/**/*.test.js',
    '<rootDir>/tests/**/*.test.jsx',
  ],
  collectCoverageFrom: [
    'frontend/src/modules/**/*.{js,jsx}',
  ],
  coverageThresholds: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

#### **Run Frontend Tests**

```bash
# Install dependencies
cd tests
npm install

# Run all tests
npm test

# Run in watch mode
npm run test:watch

# Run with coverage report
npm run test:coverage

# Run specific module tests
npm run test:payroll
npm run test:preaward
```

---

## **Development Workflow**

### **Local Setup**

#### **Prerequisites**
- Docker & Docker Compose
- Python 3.11+ (for backend development)
- Node.js 20+ (for frontend development)
- 1Password CLI (for secrets)

#### **Initial Setup**

```bash
# 1. Clone repository
git clone https://dev.azure.com/uidaho/AI4UI/_git/nexus
cd nexus

# 2. Generate .env from 1Password
op inject -i .env.template -o .env

# 3. Start Docker Compose stack
docker compose up --build

# Services available:
# - Backend: http://localhost:8000
# - Frontend: http://localhost:5173
# - PostgreSQL: localhost:5432
# - Redis: localhost:6379
# - Jaeger: http://localhost:16686
```

#### **Backend Development**

```bash
# Install dependencies
pip install -e backend/

# Run migrations
python -m alembic upgrade head

# Start development server (auto-reload)
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest tests/

# Run specific module tests
pytest tests/test_payroll*.py
```

#### **Frontend Development**

```bash
# Install dependencies
cd frontend
npm install

# Start Vite dev server (HMR enabled)
npm run dev

# Build for production
npm run build

# Lint code
npm run lint

# Run tests
cd ../tests
npm test
```

### **Git Workflow & Branch Strategy**

#### **Branch Naming Conventions**

```
sprint/{feature-name}        ← Feature development (auto-triggers CI)
test                         ← Testing/staging (auto-triggers CI)
main                         ← Production (auto-triggers CI, requires approval)

story/{story-id}             ← Story branches (no auto-trigger)
task/{task-id}               ← Task branches (no auto-trigger)
bug/{issue-id}               ← Bug branches (no auto-trigger)
hotfix/{issue-id}            ← Hotfix branches (manual approval needed)
```

#### **Commit & PR Guidelines**

```
commit message format:
[MODULE] DESCRIPTION

Examples:
[PAYROLL] Add retroactive pay form validation
[AP] Fix invoice extraction timeout issue
[AUTH] Implement token refresh interceptor
[PREAWARD] Calculate deadline based on agency rules
```

---

## **Key Design Patterns & Best Practices**

### **1. Dependency Injection (DI)**

FastAPI's `Depends()` enables clean, testable code:

```python
from fastapi import Depends

# Service layer
def get_current_user(
    token: Annotated[str, Depends(get_token_from_cookie)],
    db: Annotated[Session, Depends(get_db)]
) -> AuthUser:
    payload = decode_token(token)
    user = db.query(AuthUser).filter(AuthUser.id == payload["sub"]).first()
    return user

# Route handler
@router.get("/api/user")
async def get_user(current_user: AuthUser = Depends(get_current_user)):
    return current_user
```

### **2. Error Handling with Custom Exceptions**

Centralized error handling promotes consistency:

```python
# app/utils/custom_errors.py
class ServiceError(Exception):
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code

class ValidationError(ServiceError):
    def __init__(self, message: str):
        super().__init__(message, 422)

# app/main.py - Exception handlers
@app.exception_handler(ServiceError)
async def service_error_handler(request, exc: ServiceError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
```

### **3. Database Transaction Management**

Context managers ensure ACID properties:

```python
@router.post("/api/payroll/rpr_forms")
async def create_rpr_form(
    form_data: RPRFormCreate,
    db: Session = Depends(get_db),
    current_user: AuthUser = Depends(get_current_user)
):
    try:
        # Create form
        rpr_form = RPRForm(**form_data.dict())
        db.add(rpr_form)
        
        # Create audit log event
        event = RPRFormEvent(
            form_id=rpr_form.id,
            event="created",
            created_by=current_user.email
        )
        db.add(event)
        
        db.commit()  # All-or-nothing
    except Exception as e:
        db.rollback()
        raise ServiceError("Failed to create RPR form")
```

### **4. Asynchronous Processing for Long-Running Tasks**

RQ + Redis decouples long operations from HTTP request cycle:

```python
# Service layer - enqueue job
def process_invoice(invoice_id: int, db: Session):
    job = redis_queue.enqueue(
        'app.modules.accountspayable.tasks.extract_invoice_fields',
        invoice_id,
        job_timeout=300  # 5-minute timeout
    )
    return {"job_id": job.id, "status": "queued"}

# Worker process - run async
@worker.task
def extract_invoice_fields(invoice_id: int):
    invoice = db.query(ApInvoice).get(invoice_id)
    llm_response = call_qwen_api(invoice.email_data["attachments"])
    invoice.invoice_data = llm_response
    db.commit()
```

### **5. Role-Based Access Control (RBAC)**

Declarative permission checks at route level:

```python
from app.utils.dependencies import required_roles

@router.patch("/api/payroll/rpr_forms/{id}")
async def update_rpr_form(
    id: int,
    updates: RPRFormUpdate,
    db: Session = Depends(get_db),
    current_user: AuthUser = Depends(required_roles(["payroll.admin", "payroll.assistant"]))
):
    # Only users with specific roles can reach here
    form = db.query(RPRForm).get(id)
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(form, key, value)
    db.commit()
    return form
```

### **6. Pydantic Models for Serialization**

Type-safe API contracts:

```python
# Request model
class RPRFormCreate(BaseModel):
    employee_name: str
    hours: Decimal = Field(..., gt=0, decimal_places=2)
    rate: Decimal = Field(..., gt=0, decimal_places=2)
    reason: str = Field(..., min_length=10)

# Response model
class RPRFormResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # ORM mode

# API endpoint
@router.post("/api/payroll/rpr_forms", response_model=RPRFormResponse)
async def create_rpr_form(form_data: RPRFormCreate, ...):
    # Pydantic validates input automatically
    # Response serialized via model
    ...
```

### **7. Database Connection Pooling**

Efficient resource management:

```python
# app/modules/payroll/db.py
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,           # Min connections in pool
    max_overflow=20,        # Additional connections if needed
    pool_recycle=3600,      # Recycle connections hourly (cloud DBs)
    pool_pre_ping=True      # Verify connection before use
)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### **8. Frontend State Management (Context + Hooks)**

Avoid prop drilling with Context API:

```javascript
// authContext.jsx
const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  
  const login = async (email, password) => {
    const response = await apiClient.post('/auth/login', { email, password });
    setUser(response.data);
  };
  
  const logout = async () => {
    await apiClient.post('/auth/logout');
    setUser(null);
  };
  
  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);

// Usage in components
function Dashboard() {
  const { user } = useAuth();  // No prop drilling!
  return <h1>Welcome, {user.name}</h1>;
}
```

### **9. API Interceptors for Token Refresh**

Automatic token refresh without user awareness:

```javascript
// apiClient.js
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        // Request new access token
        await apiClient.post('/api/auth/token');
        // Retry original request
        return apiClient(originalRequest);
      } catch (refreshError) {
        // Refresh failed, logout user
        window.location.href = '/login';
      }
    }
    
    return Promise.reject(error);
  }
);
```

---

## **Summary & Key Takeaways**

**Nexus** is a production-grade, full-stack university administration platform demonstrating:

✅ **Modern Architecture**: Modular design with independent deployable services  
✅ **Security**: Enterprise SSO (Entra ID), MFA (Duo), RBAC, encrypted connections  
✅ **Scalability**: Async task processing, connection pooling, Kubernetes orchestration  
✅ **Observability**: OpenTelemetry tracing, structured logging, Jaeger visualization  
✅ **CI/CD Excellence**: Automated testing, multi-stage Docker builds, zero-downtime deployments  
✅ **Best Practices**: Dependency injection, error handling, transaction management, TypeSafe APIs  
✅ **Developer Experience**: Hot module reloading, comprehensive documentation, local Docker stack  

**Technology Highlights**:
- Python FastAPI (async ASGI framework)
- React 18 + Vite (modern frontend tooling)
- PostgreSQL + Redis (data + cache/queue)
- Azure Pipelines + Kubernetes (DevOps)
- OpenTelemetry + Jaeger (observability)
- JWT + OAuth2 + MFA (security)

---

**Version**: 1.3.4  
**Last Updated**: April 2026  
**Maintained By**: University of Idaho IT/Application Development Team

Similar code found with 1 license type