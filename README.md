# PathPilot 🚀
### AI-Assisted Campus Placement Preparation & Career Readiness

**PathPilot** is a student-focused placement preparation and simulated workplace learning platform built with **React and Vite**. It brings career roadmaps, company-specific practice, assignment reviews, mock interviews and a hands-on Company Workspace into one experience.

> **Project status:** Portfolio prototype. Some experiences are guided or simulated, and generative AI/transcription require an optional local backend.

## ✨ Key Features

| Module | What students can do |
| --- | --- |
| **Career Tracks & Roadmaps** | Explore role-based learning paths, follow a 10-week roadmap and track progress. |
| **Campus Placement Prep** | Practice **900 original prompts** across six companies and five roles per company, with 30 questions per role, topic search and progress tracking. |
| **AI Career Mentor** | Generate a seven-day practice plan, identify skill gaps and ask follow-up career questions. |
| **AI Assignment Reviewer** | Upload a PDF, choose a career track and roadmap day, and receive evidence-based practice feedback. |
| **AI Mock Interviews** | Practice interview answers with optional camera preview, microphone recording, transcription and follow-up coaching. |
| **Company Dashboard** | Explore a simulated company mission, work progress and linked sprint activity. |
| **Sprint Board & Code Studio** | Work through roadmap-linked tickets, document deliverables and experiment with code. |
| **Team Chat & Daily Work** | Practice stand-ups, blocker updates, workplace communication and daily reflections. |
| **Reviews & Portfolio** | Submit evidence, record demo mentor feedback, view a readiness breakdown and export work history. |
| **Earn & Explore / Internships** | Explore student earning ideas and employer internship listings included in the prototype. |

### 🎯 Campus Placement Prep

**6 companies × 5 role pathways × 30 questions = 900 practice questions**

| Company | Preparation pathways |
| --- | --- |
| **Google** | Software Engineer · ML Engineer · Data Scientist · Associate Product Manager · Cloud Engineer |
| **Amazon** | Software Development Engineer · Front-End Engineer · Data Engineer · Business Analyst · Cloud Support Engineer |
| **TCS** | Systems Engineer · Digital Software Engineer · Data Analyst · Cloud Engineer · Cybersecurity Analyst |
| **Infosys** | Systems Engineer · Specialist Programmer · Digital Specialist Engineer · Data Analyst · AI/ML Engineer |
| **Accenture** | Associate Software Engineer · Data & AI Analyst · Cloud Engineer · Security Analyst · Business Analyst |
| **Microsoft** | Software Engineer · Data Scientist · Applied Scientist · Product Manager · Cloud Support Engineer |

Questions are **original practice material**, not leaked or officially endorsed interview questions. Company names and role pathways do not imply current vacancies.

## 🧠 How the AI Features Work

PathPilot offers **free guided experiences** without a paid API subscription. For more adaptive responses, a local backend can use:

- **Ollama** with a locally downloaded model (for conversational coaching).
- **faster-whisper** for local audio transcription.
- **PDF.js** for browser-side extraction of text from supported PDFs.
- Rule-based rubrics for practice feedback, progress and readiness calculations.

**Important:** PDF and readiness scores are practice estimates, not verified measures of assignment correctness or placement eligibility. Scanned PDFs may need OCR. Microphone transcription and AI-generated interview feedback depend on the local backend, browser permissions and model availability.

## 🛠️ Tech Stack

- **Frontend:** React 18, Vite 6, JavaScript, CSS, Lucide React
- **PDF processing:** pdfjs-dist
- **Local AI services:** Python, Ollama (optional), faster-whisper (optional)
- **Prototype persistence:** Browser localStorage

## 🚀 Getting Started

### Prerequisites

- Node.js **20+** and npm
- Python **3.10+** for the optional local AI backend
- A microphone and compatible browser for voice-based practice

### 1. Clone the repository

```bash
git clone https://github.com/PadalaSiddharth0526/PathPilot.git
cd PathPilot
```

### 2. Start the React app

```bash
npm install
npm run dev
```

Open the local address shown by Vite, usually **http://localhost:5173**.

### 3. Optional: Enable local AI and transcription

Install [Ollama](https://ollama.com), then download a free model:

```bash
ollama pull llama3.2:3b
```

In another terminal, install the transcription dependency and start the Python service:

```bash
pip install faster-whisper
python local_server.py
```

The Vite development server proxies `/api/*` requests to `http://127.0.0.1:8000`. The first transcription request may download a model. Local model inference consumes your computer's CPU/GPU, memory and storage.

### 4. Build for production

```bash
npm run build
npm run preview
```

## 📁 Project Structure

```text
PathPilot/
├── src/
│   ├── main.jsx              # React application and student-facing modules
│   ├── Workspace.jsx         # Company Workspace
│   ├── questions.json        # Practice question data
│   ├── placement-bank.json   # Company/role placement bank
│   ├── style.css
│   └── upgrade.css
├── api/
│   └── coach.py              # Local coaching/transcription endpoints
├── local_server.py           # Local Python API server
├── index.html
├── package.json
└── README.md
```

## 📸 Screenshots

Screenshots of the dashboard, placement prep, mentor, reviewer and mock interview can be added here as the UI is finalized.

## 🔐 Prototype Limitations

- Student progress is stored in the browser; clearing localStorage can remove it.
- There is no production authentication, shared database, authenticated mentor review or real multi-user team chat.
- Company Workspace activities simulate professional work; they are **not employer-verified experience**.
- AI interview transcription requires a working local backend; camera preview does not itself record video.
- Local Ollama and faster-whisper are **not automatically available** to visitors on a static deployed website.
- Internship listings and practice role names should be checked against employers' official career sites before applying.

## 🗺️ Roadmap

- [ ] Verify the complete voice recording → transcription → review → next-question flow in real browsers.
- [ ] Connect assignment scoring to role/day-specific evaluation rubrics.
- [ ] Add authenticated student and mentor accounts with persistent storage.
- [ ] Add stronger tests for the 900-question practice bank and accessibility.
- [ ] Deploy a production frontend and, if needed, a separately hosted secure AI backend.
- [ ] Conduct student usability testing and measure preparation outcomes.

## 🎓 Why PathPilot?

Students often juggle separate resources for career planning, coding practice, interview preparation and project portfolios. PathPilot explores how these workflows can be connected: **learn a skill → complete a realistic task → receive feedback → reflect → prepare for interviews**.

Built as a hands-on **product, engineering and AI-assisted learning portfolio project**.

---

**Repository:** [github.com/PadalaSiddharth0526/PathPilot](https://github.com/PadalaSiddharth0526/PathPilot)

*PathPilot is an independent educational prototype and is not affiliated with or endorsed by the companies named in its practice content.*
