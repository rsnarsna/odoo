# Custom Addons Directory

Place your in-house developed custom Odoo modules in this directory.

This directory is mounted directly into the Odoo container at:
`/mnt/extra-addons/custom`

### Best Practices
- Every custom module should contain `__manifest__.py`, `__init__.py`, `models/`, `views/`, and `security/ir.model.access.csv`.
- Keep in-house code version controlled under this repository.
