# SheGuard AI — Cyber Forensic Platform

SheGuard AI is a cyber-forensic platform for analyzing suspicious images and filing incident reports.

## Render deployment

- Backend: `backend/` as a Python web service.
- Frontend: static site built with Vite and served from `dist/`.
- API traffic: `/api/*` is routed to the backend through Render.
- AI inference: backend loads the bundled `backend/forensic_ai` package first, then falls back to the classical pipeline if the package or checkpoints are unavailable.

## Local development

```powershell
npm install
npm run dev -- --host 0.0.0.0 --port 8080
```

```powershell
Set-Location backend
..\.venv311\Scripts\python.exe -m uvicorn main:app --reload --host 0.0.0.0 --port 7860
```
