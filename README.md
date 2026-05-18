# 🌌 Nitin Kumar's UX Design & AI Engineering Workspace

Welcome to your primary professional development workspace! This unified repository contains your core flagship products, beautifully organized and structured for local execution and production deployment.

---

## 📂 Repository Structure

Below is the clean, organized structure of the workspace, showing where each project resides:

```
.
├── 🎨 Portfolio Website/        # The DesignLab Portfolio Website (Served on Port 8000)
│   ├── FIPA/                   # Case Study: FIPA Intelligence System
│   ├── HRMS/                   # Case Study: Careline HRMS Employee Experience
│   ├── HealthCare/             # Case Study: HealthCare Telehealth Platform
│   ├── RoundMart/              # Case Study: RoundMart E-Commerce Ecosystem
│   ├── VirtualExpo/            # Case Study: Virtual Expo 3D Event Platform
│   ├── assets/                 # CSS styling, Google Fonts, and high-fidelity 3D assets
│   ├── index.html              # Main Portfolio Landing Page
│   └── style-guide.html        # Central Design System tokens and buttons
│
├── 🧠 UXAuditAi/                # The UX Heuristic Audit AI Engine (Served on Port 5051)
│   ├── scripts/                # AI evaluates, sync scripts, and Playwright orchestrators
│   │   ├── ai_evaluator.py     # Core heuristic vision analyzer (LiteLLM)
│   │   └── sync_ux_audits.py   # Synchronizes evaluations to Google Sheets
│   ├── static/                 # Sleek dark-mode CSS (Boardroom Obsidian Design System)
│   ├── templates/              # Flask Jinja2 UI templates (Audit cards, interactive spreadsheet)
│   ├── .tasks/                 # Active audit progress files (LocalStorage fallback)
│   ├── reports/                # Local cache of generated JSON audit reports
│   ├── shared_reports/         # Shared public reports for client invitations
│   └── app.py                  # Primary Flask backend server
│
├── 📝 CaseStudyBuilder/         # Automated Case Study builder tool (Served on Port 8080)
├── 🤖 LinkedIn Post Automation/  # Marketing and post outreach utilities
├── 📄 requirements.txt         # Core dependencies for the local python virtual environment
└── 🐳 Dockerfile               # Production Docker runner config
```

---

## 🎨 Project 1: DesignLab Portfolio Website

A state-of-the-art, high-density professional portfolio displaying interactive UX case studies in a unified **Boardroom Obsidian** aesthetic (curated HSL colors, smooth grid containment, and glassmorphic micro-interactions).

### 🚀 Local Execution
Start a lightweight web server inside the portfolio directory to view the website locally:
```bash
cd "Portfolio Website"
python3 -m http.server 8000
```
Then open: **[http://localhost:8000](http://localhost:8000)**

### 🌐 Live Production Deployments
* **Primary Hosting (Vercel):** Connected directly to GitHub.
  👉 **[design-lab-zeta.vercel.app](https://design-lab-zeta.vercel.app)**
* **Alternative Hosting (GitLab Pages):** Configured via automated GitLab CI pipelines (`.gitlab-ci.yml`).

---

## 🧠 Project 2: UX Heuristic Audit AI Engine

An advanced, enterprise-grade UX evaluator that automatically spins up a headless browser (Playwright) to capture screenshots of targeted web pages, runs deep vision evaluations against heuristic criteria (LiteLLM), formats attitudinal/cognitive load insights, and displays them in a high-performance interactive spreadsheet.

### ⚙️ Local Configuration
1. Make sure your local dependencies are installed:
   ```bash
   pip install -r UXAuditAi/requirements.txt
   playwright install
   ```
2. Set up your `.env` configuration file in `UXAuditAi/` with the necessary API keys:
   ```env
   GEMINI_API_KEY=your_key_here
   FLASK_PORT=5051
   FLASK_DEBUG=True
   ```

### 🚀 Running Local server
Run the main Flask application:
```bash
python3 UXAuditAi/app.py
```
Then open: **[http://localhost:5051](http://localhost:5051)**

### 🌐 Live Production Deployment
* **Render (Docker Service):** Fully pre-configured for Docker build and execution to safely handle headless browser binaries and long-running background multiprocessing pools.
  👉 **[uxauditai.onrender.com](https://uxauditai.onrender.com)**

---

## 🧹 Workspace Maintenance & Git Safety
* **Separate Remotes:** This parent repository tracks the DesignLab Portfolio to GitHub (`github`) and the UX Audit site to GitLab (`origin`).
* **Nested Sub-repositories:** `UXAuditAi/` operates as an independent child Git repository nested within the workspace, syncing directly to its dedicated backend on GitHub.
