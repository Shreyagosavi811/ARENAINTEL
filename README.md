# ARENAINTEL 🏟️🤖

## Arena Intelligence Platform

## 1. Problem and Solution
Stadium operations during mega-events such as the FIFA World Cup involve large volumes of people, multiple operational teams, and rapidly changing conditions. Delayed access to relevant operational context can make decision-making more difficult.

ARENAINTEL is a GenAI-powered decision-support platform designed to help stadium and tournament operations personnel analyze rapidly changing situations, retrieve relevant operational procedures, simulate hypothetical scenarios, and review structured AI recommendations through a human-supervised workflow.

## 2. Challenge Alignment
ARENAINTEL addresses the **Smart Stadiums & Tournament Operations** challenge by providing a GenAI-powered decision-support layer for matchday stadium staff.

The system supports:
- Operational situation analysis using GenAI and retrieved SOP context
- What-if scenario simulation without modifying live operational state
- AI-assisted incident response planning
- Human-supervised approval of AI recommendations
- Accessible operational interfaces for stadium personnel
- Structured decision support for tournament-day operations

*The application is designed as a demonstration platform using synthetic SOP data and simulated operational inputs. It does not claim to replace real stadium control systems, emergency services, or authorized human decision-makers.*

## 3. Key Features
- **Operations Copilot**: Context-aware risk assessment.
- **What-If Scenario Simulator**: Isolated predictive sandbox for hypothetical stress-testing.
- **Incident Response Copilot**: Transforms panicked, unstructured staff reports into structured emergency plans.

## 4. GenAI Pipeline
The primary application workflows use a configured Generative AI provider to analyze operational situations and generate structured recommendations.

The pipeline is:
```text
Operational Observation
        ↓
Input Validation
        ↓
TF-IDF Retrieval of Relevant SOP Context
        ↓
Generative AI Analysis
        ↓
Structured JSON Response
        ↓
Pydantic Validation
        ↓
Human Review
        ↓
Approve / Reject
```

No mock AI responses are used in the primary application workflows. The demonstration environment uses synthetic SOP knowledge and simulated operational inputs. The GenAI output is constrained to a structured schema, validated before being returned to the frontend, and presented as an advisory recommendation rather than an autonomous command.

## 5. What Makes ARENAINTEL Different
Instead of treating Generative AI as a standalone chatbot, ARENAINTEL places it inside a controlled operational workflow:
- Retrieval grounds the AI in relevant operational procedures.
- Structured schemas constrain the generated output.
- Domain rules enforce valid workflow transitions.
- Simulations are isolated from operational state.
- Human supervisors approve or reject recommendations.
- Audit records preserve decision history.

This creates a controlled AI decision-support loop rather than an autonomous AI control system.

## 6. RAG Approach
The system uses a native Python TF-IDF retrieval layer to ground the GenAI provider with relevant operational context, after which the provider generates a structured recommendation. This eliminates the overhead of heavy vector databases.

## 7. Human-in-the-Loop Model
The AI acts exclusively as an advisory intelligence. It cannot execute physical commands. Every generated operational plan enters a `PENDING_REVIEW` state, requiring explicit authorization from a human supervisor to transition to `APPROVED` or `REJECTED`.

## 8. Architecture
The backend strictly adheres to Clean Architecture. The dependency rule points inward: API and Infrastructure depend on Application abstractions, while Application depends on Domain logic. The Domain layer remains independent of frameworks, databases, FastAPI, and specific AI providers.

## 9. Security Approach
- **Prompt Injection Defense**: Untrusted inputs are XML-encapsulated (`<untrusted_user_input>`) and explicitly treated as data rather than instructions.
- **Resource Exhaustion**: Expensive AI endpoints are protected by `slowapi` rate limiting (5 requests/minute).
- **Secrets Management**: No API keys are committed to the repository. Provider credentials remain server-side and are never exposed to the frontend.
- **Error Sanitization**: Provider and backend errors are mapped to safe user-facing messages without exposing stack traces or secrets.

## 10. Tech Stack
- **Backend**: FastAPI, Pydantic V2, SQLModel/SQLite, Pytest.
- **Frontend**: React 18, Vite, TanStack Query, Vanilla CSS.

## 11. Project Structure
```text
stadiumops-ai/
├── backend/
│   ├── app/
│   │   ├── api/ (FastAPI Routers)
│   │   ├── application/ (Orchestration)
│   │   ├── domain/ (State Machine & Logic)
│   │   └── infrastructure/ (AI, DB, RAG)
│   └── tests/
└── frontend/
    ├── src/
    │   ├── features/ (Copilot, Scenarios, Approvals)
    │   └── components/ (Reusable UI States)
    └── tests/
```

## 12. Setup Instructions
**Prerequisites**: Node 18+, Python 3.11+
```bash
# 1. Backend Setup
cd backend
python -m venv venv
# Windows: .\\venv\\Scripts\\activate | Mac: source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env  # Add your AI Provider API Keys

# 2. Frontend Setup
cd ../frontend
npm install
```

## 13. Running Instructions
Run both servers simultaneously:
- **Backend**: `cd backend && uvicorn app.main:app --reload` (Runs on port 8000)
- **Frontend**: `cd frontend && npm run dev` (Runs on port 5173)

## 14. Testing Instructions
- **Backend Tests**: `cd backend && pytest tests/`
- **Frontend Tests**: `cd frontend && npm run test`

## 15. Assumptions
- Stadium telemetry (occupancy, turnstile speed) is currently simulated for demonstration.
- SOP documents form a localized operational knowledge base.
- AI recommendations are advisory and do not directly control physical infrastructure.
- Scenario simulations do not modify live state.
- Human supervisors remain ultimately responsible for operational decisions.
- AI output may contain uncertainties and requires human review.

## 16. Limitations
- Live sensor integrations (IoT) are simulated.
- The TF-IDF knowledge base is intentionally lightweight for the hackathon constraint.
- The SOP dataset is synthetic/demo data.
- The system is a decision-support tool and does not replace trained emergency personnel.

## 17. Repository-Size Compliance
The submitted repository has been verified to remain below the 10 MB repository-size limit. The project avoids committed virtual environments, `node_modules`, build artifacts, model weights, large media files, and heavy vector database dependencies.

The source code footprint is approximately 1 MB in the current development snapshot.
