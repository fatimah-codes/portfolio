# Fatima Hamayyun — AXON Portfolio Website

An interactive, high-performance personal portfolio website built with **Streamlit** and **Three.js (0.150.1 UMD)**, recreating the futuristic dark aesthetic, monospace typographic hierarchy, and GPU-accelerated particle/fluid dynamics from the **AXON Motion Research Hub** specification.

---

## 🌟 Key Highlights & Architecture

- **Streamlit Shell (`app.py`)**: Seamless single-page application shell rendering a single full-screen, self-contained iframe via `st.components.v1.html()`. All default Streamlit navigation, headers, footers, toolbars, and paddings are completely eliminated using custom CSS overrides.
- **Data-Driven Decoupling (`data/portfolio.json`)**: All resume content, skills, projects, and contact data are externalized in JSON.
- **Official Profiles Integrated**:
  - **LinkedIn**: [linkedin.com/in/fatima-95b55722a](https://www.linkedin.com/in/fatima-95b55722a)
  - **GitHub**: [github.com/fatimah-codes](https://github.com/fatimah-codes)
  - **Email**: [mailto:fatimaah2310@gmail.com](mailto:fatimaah2310@gmail.com)
- **Interactive Animations & Popups**:
  - **Interactive Project Detail Modal**: Clicking any project card pops open a high-tech modal dialog with detailed engineering specifications, live procedural canvas animation, problem/solution overview, and direct GitHub links. Accessible with `[✕ CLOSE / ESC]`, backdrop click, or keyboard `ESC`.
  - **Interactive Skill Application Popups**: Clicking any skill badge in `[SKILLS & PROFICIENCIES]` triggers an animated HUD toast popup describing the exact real-world context and projects where that skill was applied.
  - **Hero Metrics Banner**: Live statistical summary highlighting degree CGPA (`3.41`), completed projects (`04`), institutional internships (`02`), and organic Google SERP rankings (`TOP 1`).
  - **Top Bar Quick Navigation**: One-click pills directly opening GitHub and LinkedIn, plus the round project counter and particle shape switch.
- **GPU Ping-Pong Particle Simulation (Section 7)**:
  - **262,144 particles** on desktop ($512 \times 512$ FBO simulation grid) and **16,384 particles** on mobile ($128 \times 128$).
  - Mathematical 3D **incompressible Curl Noise** vector field.
  - Attraction to a 3D **Signed Distance Field (SDF)** surface (3D Tilted Torus Ring at $35^\circ / 25^\circ$).
  - Additive point sprite blending with an embedded radial glow matcap sprite data URI and delicate starry falloff.
  - Smooth **gaze camera parallax** gently tracking pointer coordinates with damping.
  - **Stretch Feature**: Instant toggle between the Sculpted Torus Ring and Fatima's Initials monogram (**"FH"**).
- **GPU Fluid Cursor Interaction (Section 8)**:
  - 2D GPU velocity grid advection and Gaussian cursor splat impulse.
  - Viscous exponential decay ($0.955$ per frame) ensures the cloud blooms and **settles back within ~2 seconds**.
- **Graceful Fallbacks & Guardrails**:
  - Automatic detection of WebGL2 and float render targets (`EXT_color_buffer_float`); seamlessly falls back to a dark ambient CSS particle gradient if unsupported.
  - Automatic frame pausing when the browser tab is hidden via `document.hidden`.
  - Device pixel ratio capped at `2.0` to preserve GPU efficiency on high-DPI displays.
  - Interactive project filter chips (`ALL`, `IOT`, `PYTHON`, `WEB DEV`, `FIREBASE`, `E-COMMERCE`, `CONTENT`, `DATA & AI`).
  - One-click CV download directly decoding `assets/Fatima_Hamayyun_CV.pdf` as a standalone blob.

---

## 📁 Project Directory Structure

```text
fatima_portfolio/
├── app.py                      # Streamlit application entry point & CSS injector
├── requirements.txt            # Python dependencies (streamlit)
├── README.md                   # Setup guide and documentation
├── data/
│   └── portfolio.json          # Extracted resume content & project metadata
├── templates/
│   └── index.html              # AXON UI, Three.js shaders, & particle/fluid simulation
└── assets/
    └── Fatima_Hamayyun_CV.pdf  # Downloadable resume document
```

---

## 🚀 Quickstart & Local Setup

### 1. Installation
Open a terminal in the project directory:

```bash
cd c:\Users\dell\OneDrive\Desktop\fatima_portfolio
pip install -r requirements.txt
```

### 2. Run the Streamlit Portfolio
```bash
streamlit run app.py
```

The portfolio will launch at `http://localhost:8501`. If already running, refresh the page (`Ctrl + R`).
