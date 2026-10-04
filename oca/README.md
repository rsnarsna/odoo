# OCA (Odoo Community Association) Addons Directory

Place or clone Odoo Community Association (OCA) modules in this directory.

This directory is mounted directly into the Odoo container at:
`/mnt/extra-addons/oca`

### Recommended OCA Repositories (Matching Odoo 18.0 / Community)
- **Helpdesk**: `git clone --depth 1 -b 18.0 https://github.com/OCA/helpdesk.git`
- **Contracts / Subscriptions**: `git clone --depth 1 -b 18.0 https://github.com/OCA/contract.git`
- **Field Service**: `git clone --depth 1 -b 18.0 https://github.com/OCA/field-service.git`
- **Document Management (DMS)**: `git clone --depth 1 -b 18.0 https://github.com/OCA/dms.git`
- **Financial Reporting**: `git clone --depth 1 -b 18.0 https://github.com/OCA/account-financial-reporting.git`
- **Financial Tools**: `git clone --depth 1 -b 18.0 https://github.com/OCA/account-financial-tools.git`
- **Marketing Automation**: `git clone --depth 1 -b 18.0 https://github.com/OCA/marketing-automation.git`
- **Payroll**: `git clone --depth 1 -b 18.0 https://github.com/OCA/payroll.git`
- **Barcode & Delivery**: `git clone --depth 1 -b 18.0 https://github.com/OCA/stock-logistics-barcode.git`

After cloning any repository into this folder:
1. Restart the container: `docker compose restart web`
2. Enable Developer Mode in Odoo settings (`Settings` -> `Activate developer mode`).
3. Navigate to `Apps` -> `Update Apps List`.
4. Search for and install the desired modules.
