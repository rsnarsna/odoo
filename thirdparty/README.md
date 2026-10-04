# Third-Party Addons Directory

Place downloaded third-party modules (from Odoo Apps store or independent vendors) into this directory.

This directory is mounted directly into the Odoo container at:
`/mnt/extra-addons/thirdparty`

### Instructions
1. Unpack downloaded zip packages into subfolders inside this directory.
2. Ensure the module is compatible with Odoo 18.0 Community and does not depend on `web_enterprise`.
3. Restart the container: `docker compose restart web`
4. In Odoo Web UI: Enable Developer Mode -> Go to `Apps` -> Click `Update Apps List`.
