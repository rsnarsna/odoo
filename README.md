# Odoo Community Edition with Third-Party & OCA Enterprise Alternatives (Docker Stack)

[![Odoo Version](https://img.shields.io/badge/Odoo-18.0%20Community-875A7B?logo=odoo&logoColor=white)](https://www.odoo.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16--alpine-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![OCA](https://img.shields.io/badge/Addons-OCA%20Ready-00A09D)](https://github.com/OCA)
[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3.0-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

A ready-to-deploy, containerized **Odoo Community Edition** stack configured to run paid Enterprise features through **Odoo Community Association (OCA)** modules, third-party apps, and custom extensions—all managed cleanly via Docker Compose and secured using environment variables.

---

## 📑 Table of Contents
1. [Overview & Strategy](#1-overall-strategy)
2. [Feature-by-Feature Enterprise Replacement Plan](#2-feature-by-feature-plan)
3. [Repository Directory Structure](#3-directory-structure)
4. [Secure Credential Architecture](#4-secure-credential-architecture)
5. [Quick Start & Docker Deployment](#5-quick-start--docker-deployment)
6. [Managing Third-Party & OCA Modules](#6-managing-third-party--oca-modules)
7. [Evaluation & Licensing Guidelines](#7-evaluation--licensing-guidelines)
8. [Maintenance, Backup & Rollout Phases](#8-maintenance--rollout-phases)

---

## 1. Overall Strategy

- **Base Engine:** Run **Odoo Community Edition** (100% free and open source) as the solid foundation.
- **Bridging the Enterprise Gap:** Fill each Odoo Enterprise gap with one of three approaches:
  1. **Use an OCA module (Free & Open Source):** Maintained by the community, battle-tested, standard compliance.
  2. **Third-Party App (Paid single purchase):** From the Odoo Apps Store without monthly per-user licensing fees.
  3. **Build your own module (In-House):** Tailored specifically to your business workflows.
- **Cost Comparison:** Enterprise pricing starts around **$19.90 - $24.90/user/month**. For growing teams, Community + OCA/Third-Party apps delivers the same functional capabilities while eliminating recurring user license fees.

---

## 2. Feature-by-Feature Plan

| Paid / Enterprise Feature | Recommended Third-Party / OCA Route | Decision & Notes |
|---|---|---|
| **Full Accounting & Reports** | OCA `account-financial-reporting`, `account-financial-tools` + bank connector | Use OCA; add local bank feed module |
| **Helpdesk** | OCA `helpdesk` | Use OCA (Tickets, stages, teams, SLA tracking) |
| **Subscriptions & Recurring**| OCA `contract` | Use OCA (Recurring invoices, contracts) |
| **Field Service** | OCA `field-service` | Use OCA (Territories, technicians, dispatching) |
| **Documents (DMS)** | OCA `dms` | Use OCA (Folders, tags, storage directory) |
| **Marketing Automation** | OCA `marketing-automation` | Use OCA (Campaign triggers, automation flows) |
| **Payroll** | OCA `payroll` + country localisation | Use OCA; verify local statutory compliance |
| **Barcode / Shipping** | OCA `stock-logistics-barcode`, `delivery-carrier` | Use OCA (Hardware scanners, mobile scanning) |
| **VoIP Telephony** | OCA `connector-telephony` | Use OCA (Asterisk / SIP integration) |
| **Social Marketing** | Odoo Apps store module or custom integration | Buy from App Store or build lightweight connector |
| **Sign (e-Signatures)** | Apps store module or custom integration with `pyHanko` | Buy or build with standard PDF signatures |
| **Studio** | Developer mode (`Settings -> Technical`) + custom modules | Configure via standard views or code |
| **PLM, MPS, Planning** | Partial OCA modules or custom models | Build / configure specific to manufacturing needs |
| **AI Features** | Custom lightweight module via OpenAI / Gemini / Anthropic APIs | Build custom REST integration |
| **Mobile App** | Responsive Web UI (PWA) or Flutter/React Native wrapper | Responsive browser or custom app |

---

## 3. Directory Structure

```text
odoo/
├── .env.example              # Template environment variables (committed to Git)
├── .env                      # Real credentials & secrets (ignored by Git)
├── .gitignore                # Security rules ignoring credentials & heavy data
├── docker-compose.yml        # Multi-container orchestration (Odoo 18 + PostgreSQL 16)
├── README.md                 # Complete documentation & strategy guide
├── config/
│   └── odoo.conf             # Odoo daemon configuration (addons_path, workers, logging)
├── oca/                      # OCA modules (mounted to /mnt/extra-addons/oca)
│   └── README.md
├── thirdparty/               # Commercial / store apps (mounted to /mnt/extra-addons/thirdparty)
│   └── README.md
├── custom/                   # In-house custom modules (mounted to /mnt/extra-addons/custom)
│   └── README.md
├── scripts/
│   ├── clone_oca_modules.sh  # Bash automation script to fetch OCA modules
│   └── clone_oca_modules.ps1 # PowerShell automation script to fetch OCA modules
└── odoo/                     # Official Odoo Community upstream repository (local copy)
```

---

## 4. Secure Credential Architecture

All sensitive credentials and variables are kept in **`.env`** and isolated from version control:

1. **Master Database Password (`ODOO_ADMIN_PASSWORD`):** Used to create, drop, backup, or duplicate databases.
2. **PostgreSQL Credentials (`POSTGRES_USER`, `POSTGRES_PASSWORD`):** Database credentials passed securely to both the PostgreSQL service and Odoo service.
3. **Ports & Service Tags:** Fully configurable without modifying `docker-compose.yml`.

> [!IMPORTANT]
> The `.env` file is excluded in `.gitignore`. Never commit actual passwords or database tokens to a public repository!

---

## 5. Quick Start & Docker Deployment

### Prerequisites
- [Docker Desktop](https://www.docker.com/) or Docker Engine with Docker Compose v2.

### Step 1: Clone the Repository
```bash
git clone https://github.com/rsnarsna/odoo.git
cd odoo
```

### Step 2: Configure Environment Variables
Copy `.env.example` to `.env` and set your secure passwords:
```bash
# On Linux / macOS
cp .env.example .env

# On Windows PowerShell
Copy-Item .env.example .env
```

### Step 3: Start the Docker Stack
```bash
docker compose up -d
```

### Step 4: Access Odoo
Open your browser and navigate to:
```
http://localhost:8069
```
1. Create your database (enter Master Password from `.env`, Database Name, Email/Login, and Password).
2. Choose whether to install demo data.
3. Log in to your new Odoo Community instance!

---

## 6. Managing Third-Party & OCA Modules

### Installing OCA Modules
Run the automated script to clone the recommended OCA modules for your version:
```bash
# On Linux / macOS:
chmod +x scripts/clone_oca_modules.sh
./scripts/clone_oca_modules.sh 18.0

# On Windows PowerShell:
.\scripts\clone_oca_modules.ps1 -OdooVersion 18.0
```

### Installing Third-Party Store Modules
1. Download the module ZIP from the Odoo Apps Store (verify Community edition compatibility).
2. Extract the module folder into `thirdparty/`.

### Activating Modules in Odoo UI
1. Restart the container:
   ```bash
   docker compose restart web
   ```
2. Navigate to **Settings** -> Scroll to the bottom and click **Activate the developer mode**.
3. Go to the **Apps** menu.
4. Click **Update Apps List** in the top navigation bar.
5. Search for your module name, remove the default "Apps" filter if necessary, and click **Activate**.

---

## 7. Evaluation & Licensing Guidelines

When adding third-party apps:
- **Version Compatibility:** Verify the app supports your exact version (e.g. 18.0).
- **No Enterprise Dependency:** Confirm the app does **not** declare `web_enterprise` in its `depends` list in `__manifest__.py`.
- **License Compliance:**
  - Odoo Community is licensed under **LGPL-3**.
  - OCA modules are typically licensed under **LGPL-3** or **AGPL-3**.
  - Commercial App Store modules typically use **OPL-1** (Odoo Proprietary License v1).
  - Never copy proprietary Enterprise source code into Community modules.

---

## 8. Maintenance, Backup & Rollout Phases

### Recommended Rollout Phases
- **Phase 1:** Core ERP apps (CRM, Sales, Purchase, Inventory, Invoicing) + OCA Helpdesk, Contracts, DMS, Barcode.
- **Phase 2:** OCA Full Accounting & Reports, Payroll, and local statutory taxation/bank feeds.
- **Phase 3:** Social marketing and e-Sign connectors.
- **Phase 4:** Custom manufacturing workflows, AI extensions, and specialized automations.

### Backups
Always backup both the database and the filestore before testing new modules:
```bash
# Backup PostgreSQL database
docker compose exec db pg_dump -U odoo -d postgres -F c -b -v -f /var/lib/postgresql/data/backup_$(date +%Y%m%d).dump
```
Or access `http://localhost:8069/web/database/manager` to download a complete zip containing both database SQL and filestore attachments.
