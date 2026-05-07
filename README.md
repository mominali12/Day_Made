# 🏠 Day Made
Household AI Calendar Sync

> A privacy-first, self-hosted AI-powered household calendar assistant that automatically organizes schedules from chat conversations.

The system listens to household chats, extracts events, synchronizes calendars, detects conflicts, and generates intelligent summaries — while keeping all data local and secure using open-source software and local LLMs through Ollama.

---

# ✨ Features

## 📩 Smart Event Extraction

Automatically extracts:
- Appointments
- Meetings
- School activities
- Schedule changes
- Reminders

From chat platforms such as:
- Matrix
- Slack
- Mattermost

### Example

```text
John:
“I have a dentist appointment tomorrow at 3 PM.”
```

Becomes:

```yaml
title: Dentist Appointment
owner: John
date: 2026-05-08
time: 15:00
```

---

# 🧠 Hybrid AI Architecture

The system uses:

## ✅ Deterministic Scheduling Engine

Handles:
- Calendar synchronization
- Conflict detection
- Availability checks
- Notifications
- Permissions

## ✅ Local LLMs via Ollama

Handles:
- Ambiguous language
- Intent understanding
- Smart summaries
- Natural conversation
- Suggestion generation

This provides:
- Reliability
- Privacy
- Predictable scheduling
- AI-enhanced UX

---

# 🔒 Privacy-First Design

## All AI Runs Locally

No cloud AI APIs required.

Your:
- Messages
- Calendar data
- Family schedules
- Personal routines

Never leave your infrastructure.

---

# 🏠 Self-Hosted

Deploy on:
- **MacBook Pro**
- Raspberry Pi
- Intel NUC
- NAS
- Home server
- VPS
- Kubernetes cluster

---

# 🔄 Household Calendar Synchronization

Each household member has:
- Their own calendar
- Shared visibility rules
- Availability preferences
- Notification settings

Supported calendars:
- **Google Calendar**
- Apple Calendar (optional)
---

# ⚠️ Conflict Detection & Smart Suggestions

The system automatically:
- Detects overlapping events
- Identifies household conflicts
- Suggests alternatives

### Example

```text
⚠️ Conflict detected

Ali has football practice at 17:00
while both parents are unavailable.

Suggestions:
- Move practice
- Ask grandparents
- Reschedule meeting
```

---

# 🌙 Daily AI Summaries

Every evening at a configurable time:

The system generates:
- Tomorrow’s schedule
- Important reminders
- Travel/preparation alerts
- Conflict warnings

### Example

```text
📅 Tomorrow Summary

John
- 09:00 Team Meeting
- 15:00 Dentist Appointment

Emma
- School Trip
- Bring signed permission slip

⚠️ Warning:
No available pickup at 17:00
```

---

# 🏗️ System Architecture

```text
               ┌───────────────────┐
               │       Slack       │
               └─────────┬─────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Message Ingestion   │
              └─────────┬───────────┘
                        │
                        ▼
              ┌─────────────────────┐
              │ Rule-Based Parser   │
              └─────────┬───────────┘
                        │
        High Confidence │ Low Confidence
                        ▼
                  ┌────────────────┐
                  │ Ollama + LLM   │
                  └────────┬───────┘
                           ▼
                ┌──────────────────┐
                │ Scheduling Engine│
                └────────┬─────────┘
                         ▼
               ┌───────────────────┐
               │ Calendar Sync     │
               └────────┬──────────┘
                        ▼
               ┌───────────────────┐
               │ Notifications     │
               └───────────────────┘
```

---

# 🛠️ Open Source Tech Stack

## Backend

| Component | Technology |
|---|---|
| API Framework | FastAPI |
| Database | PostgreSQL |
| Cache / Queue | Redis |
| Background Tasks | Celery |
| Reverse Proxy | Traefik |

---

## 🤖 AI Stack

| Component | Technology |
|---|---|
| Local LLM Runtime | Ollama |
| LLM Orchestration | LangChain |
| Embeddings | sentence-transformers |
| Vector Database | ChromaDB |

---

## 🧠 Recommended Models

| Use Case | Model |
|---|---|
| Event extraction | Mistral 7B |
| Summaries | Gemma |
| Conversation | Llama 3 |
| Lightweight deployment | Phi-3 Mini |
| Multilingual support | Qwen 2.5 |

---

## 📅 Scheduling & Calendars

| Component | Technology |
|---|---|
| Calendar Protocol | CalDAV |
| Scheduler | OR-Tools |
| Date Parsing | Duckling |

---

## 🔐 Authentication & Security

| Component | Technology |
|---|---|
| Authentication |
| Authorization |
| HTTPS | Traefik + Let's Encrypt |

---

## 💬 Messaging Integrations

| Platform | Status |
|---|---|
| Slack | ✅ |
---

# 📂 Project Structure

```bash
household-ai-calendar/
│
├── backend/
│   ├── api/
│   ├── auth/
│   ├── scheduling/
│   ├── parsers/
│   ├── ai/
│   ├── notifications/
│   └── integrations/
│
├── infrastructure/
│   ├── docker/
│   ├── traefik/
│   └── scripts/
│
├── frontend/
│
├── models/
│
├── tests/
│
└── docs/
```

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/household-ai-calendar.git

cd household-ai-calendar
```

---

## 2. Install Homebrew (macOS)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 3. Install Docker Desktop

Download:
https://www.docker.com/products/docker-desktop/

---

## 4. Install Ollama

```bash
brew install ollama
```

---

## 5. Pull AI Models

```bash
ollama pull mistral
ollama pull gemma
ollama pull llama3
```

---

## 6. Start Ollama

```bash
ollama serve
```

---

## 7. Configure Environment

Create `.env`

```env
POSTGRES_PASSWORD=
REDIS_URL=redis://redis:6379

KEYCLOAK_ADMIN=
KEYCLOAK_PASSWORD=

OLLAMA_HOST=http://ollama:11434
GOOGLE_CALENDAR_API=
```

---

## 8. Start Services

```bash
docker compose up -d
```

---

# 🔒 Security Model

## Authentication

Managed through:
- Keycloak
- OAuth2
- OpenID Connect
- MFA support

---

## Authorization

Role-based permissions:
- Parent
- Child
- Admin
- Guest

---

## Security Features

- Local-only LLM inference
- HTTPS everywhere
- JWT authentication
- Encrypted database connections
- VPN-compatible deployment (optional)
- No external AI providers required

---

# 🧠 AI Routing Strategy

The system avoids unnecessary LLM usage.

## Fast Path (No AI)

Simple events use:
- Regex
- Duckling
- Rule-based parsing

Example:

```text
“Dentist tomorrow at 3”
```

---

## AI Path (Ollama)

Complex/ambiguous messages use local LLMs.

Example:

```text
“Can someone else pick up Emma if we're still working late?”
```

---

# 📦 Deployment Options

## 🏠 Home Server

- MacBook Pro
- Raspberry Pi 5
- Intel NUC
- Synology NAS

---

## ☁️ VPS

- Hetzner
- OVH
- DigitalOcean

---

## ⚙️ Kubernetes

- k3s
- Talos Linux

---

# 📈 Roadmap

## Phase 1
- Chat ingestion
- Event extraction
- Calendar synchronization
- Conflict detection

## Phase 2
- AI summaries
- Smart suggestions
- Multi-calendar optimization

## Phase 3
- Voice assistant
- Mobile apps
- Smart home integration
- Wearable integration

---

# 🤝 Contributing

Contributions are welcome.

Areas needing help:
- Scheduling optimization
- Mobile applications
- Security hardening
- Kubernetes deployment
- Local LLM optimization

---

# 📜 License

CC BY Zero

---

# 🎯 Vision

Build a fully private, self-hosted AI household operating system that:
- Understands conversations
- Coordinates schedules
- Reduces mental overhead
- Protects family privacy
- Runs entirely on open-source infrastructure

Without relying on cloud AI providers or exposing personal household data.
