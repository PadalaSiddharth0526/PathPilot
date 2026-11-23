# PathPilot — AI-Powered Campus Placement Preparation

PathPilot is a React + Vite student career-readiness prototype. The original green PathPilot dashboard is the entry screen, with linked career roadmaps, Company Workspace sub-tabs and Campus Placement Prep.

## Features

- **Campus Placement Prep:** 900 original practice questions across **6 companies × 5 career pathways × 30 questions**. Includes Google, Amazon, TCS, Infosys, Accenture and Microsoft. Questions are *not* leaked interview questions or proof that these companies have open vacancies.
- **Company Workspace:** simulated company dashboard, sprint tickets, code studio, team chat, submissions, mentor reviews, readiness score, daily stand-ups and work portfolio.
- **Career Mentor:** 7-day practice planning and optional conversational local Ollama coaching.
- **Assignment Reviewer:** browser PDF text extraction, track/day selection, heuristic evidence scoring, optional local AI feedback. Scanned PDFs require OCR.
- **AI Mock Interviews:** camera preview, voice answer recording, transcription via optional local faster-whisper, practice feedback and follow-up questions.
- **Original PathPilot** layout remains accessible; workspace progress is browser-local.

## Run locally

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run dev
```

Visit the local Vite URL (normally http://localhost:5173). Build the frontend using `npm run build`.

## Optional free local AI backend

Requirements: Python 3.10+, [Ollama](https://ollama.com), and local model downloads. No paid API key needed.

```bash
ollama pull llama3.2:3b
pip install faster-whisper
python local_server.py
```

Vite proxies `/api/*` requests to `http://127.0.0.1:8000`. The first Whisper transcription can download a free model. Local AI is **not** automatically available to public website visitors and will not run inside a static GitHub Pages deployment. For hosted transcription or Ollama, provision a separate secure backend.

## Important limitations

This is a *portfolio prototype*, not a production learning platform. Student data is kept in localStorage; there is no authenticated student or teacher account system, persistent shared database, verified employer experience or real multi-user chat. Readiness and assignment scores are practice heuristics, not objective proof of correctness or placement eligibility. Camera is an optional local preview; recording/transcription require browser permissions and compatible devices. Audio transcription and model scoring have not been tested end-to-end on a physical microphone here.

The application is intended to be deployed to a static frontend host (such as Vercel) after a successful build. Pushing source to GitHub does **not** itself publish a running website.
