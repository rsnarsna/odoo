# Contributing to Odoo Community + OCA Enterprise Stack

Thank you for your interest in contributing to this open-source project! We welcome contributions to expand OCA modules, improve configurations, documentation, and Docker orchestration.

---

## 🛠️ Code of Conduct

This project adheres to the Contributor Covenant. By participating, you are expected to uphold this code. Please report unacceptable behavior via GitHub Issues or to the repository owner.

---

## 🚀 How Can You Contribute?

### 1. Reporting Bugs
- Search existing issues to ensure the bug has not already been reported.
- Create a new issue describing the problem, reproduction steps, your OS, Docker version, and container logs.

### 2. Proposing OCA Modules
- If you find a great OCA module that replaces another Enterprise feature, open a Feature Request issue or submit a Pull Request.
- Verify that the module is available for **Odoo 19.0** and does not require `web_enterprise`.

### 3. Submitting Pull Requests
1. **Fork** the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/my-new-feature
   ```
2. **Test locally**:
   - Verify that your module starts without errors.
   - Run `docker compose exec web odoo -i <new_module> -d odoo --stop-after-init` to verify clean database loading.
   - Test web interface responses at `http://localhost:8069`.
3. **Commit cleanly**:
   - Follow conventional commit style: `feat:`, `fix:`, `docs:`, `refactor:`.
   - Never commit sensitive `.env` files or credentials.
4. **Push and create a Pull Request**.

---

## ☕ Support the Project

If this stack helps your company or personal project, please consider:
- ⭐ Giving the repository a star on GitHub!
- ☕ Buying us a coffee at: [https://www.buymeacoffee.com/rsnarsna](https://www.buymeacoffee.com/rsnarsna)
- 💖 Sponsoring through [GitHub Sponsors](https://github.com/sponsors/rsnarsna)
