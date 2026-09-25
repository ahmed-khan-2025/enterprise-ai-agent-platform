# Enterprise AI Agent Platform

A multi-agent enterprise AI platform built with **Python, FastAPI, LangGraph, Ollama, HTTP microservices, and PostgreSQL**.

The platform uses AI agents to investigate enterprise business problems by collecting information from multiple backend services, reasoning over the collected evidence, and generating a final actionable response.

---

## 🚀 Project Overview

The goal of this project is to demonstrate how an AI agent can operate across multiple enterprise backend services instead of acting as a simple standalone chatbot.

A user can ask a natural-language question such as:

> Why did order 10452 fail?

The system then:

1. Receives the user question.
2. Starts a LangGraph workflow.
3. Investigates the order.
4. Retrieves order information.
5. Retrieves customer information.
6. Retrieves payment information.
7. Retrieves operational logs.
8. Analyzes the collected evidence.
9. Makes a decision.
10. Generates a final response using an LLM.

### Core concept

```text
Natural Language Question
          ↓
     LangGraph
          ↓
 Investigation Agent
          ↓
 ┌────────┼─────────┐
 ↓        ↓         ↓
Order  Customer  Payment
Service Service  Service
 :8001   :8002     :8003
          │
          ↓
     Logging Service
          :8004
          ↓
     Decision Agent
          ↓
     Response Agent
          ↓
        Ollama
          ↓
     Final Response
```

---

# 🏗️ Architecture

The platform follows a multi-service, agent-based architecture.

```text
                         ┌──────────────────────┐
                         │        User          │
                         │   Natural Language   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      LangGraph       │
                         │       Workflow       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Investigation Agent  │
                         └──────────┬───────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              │                     │                     │
              ▼                     ▼                     ▼
     ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
     │ Order Service  │    │Customer Service│    │ Payment Service│
     │     :8001      │    │     :8002      │    │     :8003      │
     └────────────────┘    └────────────────┘    └────────────────┘
              │
              │
              ▼
     ┌────────────────┐
     │ Logging Service│
     │     :8004      │
     └───────┬────────┘
             │
             ▼
     ┌────────────────────┐
     │   Decision Agent   │
     └──────────┬─────────┘
                │
                ▼
     ┌────────────────────┐
     │   Response Agent   │
     └──────────┬─────────┘
                │
                ▼
     ┌────────────────────┐
     │      Ollama        │
     │      Llama 3.2     │
     └──────────┬─────────┘
                │
                ▼
        ┌───────────────┐
        │ Final Answer  │
        └───────────────┘
```

---

# 🤖 Agents

## 1. Investigation Agent

The Investigation Agent gathers information required to understand an enterprise problem.

It communicates with backend services through dedicated tools.

For an order investigation, it can retrieve:

* Order information
* Customer information
* Payment information
* Operational logs

The agent creates the evidence required by the next stage of the workflow.

---

## 2. Decision Agent

The Decision Agent analyzes the information collected during the investigation.

It determines the likely reason for the business event based on the available evidence.

For example:

```text
Payment authorization failed
        ↓
Payment retries failed
        ↓
Order marked FAILED
        ↓
Diagnosis:
Payment authorization was declined
```

---

## 3. Response Agent

The Response Agent converts the investigation and decision into a clear response for the user.

The response contains:

* Investigation status
* Diagnosis
* Recommended action

Example:

```text
Order #10452 investigation complete.

Diagnosis: The order failed because the payment authorization was declined.

Recommended action: Ask the customer to update their payment method and retry the order.
```

---

# 🔄 LangGraph Workflow

The agent workflow is implemented using **LangGraph**.

The current workflow is intentionally simple and deterministic:

```text
START
  │
  ▼
Investigation
  │
  ▼
Decision
  │
  ▼
Response
  │
  ▼
END
```

This provides a clear separation between:

* Data collection
* Reasoning/decision making
* Response generation

---

# 🧩 Microservices

The project contains independent backend services.

| Service          |    Port | Responsibility         |
| ---------------- | ------: | ---------------------- |
| Order Service    |  `8001` | Order information      |
| Customer Service |  `8002` | Customer information   |
| Payment Service  |  `8003` | Payment information    |
| Logging Service  |  `8004` | Operational event logs |
| Ollama           | `11434` | Local LLM              |

The AI agent communicates with the services using HTTP requests.

---

# 🛠️ Technology Stack

## Backend

* Python
* FastAPI
* Uvicorn
* HTTPX

## AI / Agent

* LangGraph
* LangChain
* Ollama
* Llama 3.2

## Configuration

* Pydantic Settings
* `.env`

## Database

* PostgreSQL
* SQLAlchemy / PostgreSQL integration

## Development

* Git
* Docker
* Docker Compose
* Pytest

---

# 📁 Project Structure

```text
enterprise-ai-agent-platform/
│
├── app/
│   ├── __init__.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── investigation_agent.py
│   │   ├── decision_agent.py
│   │   └── response_agent.py
│   │
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── state.py
│   │   └── workflow.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── order_tools.py
│   │   ├── customer_tools.py
│   │   ├── payment_tools.py
│   │   └── logging_tools.py
│   │
│   └── config.py
│
├── services/
│   ├── __init__.py
│   │
│   ├── order_service/
│   │   ├── __init__.py
│   │   └── app.py
│   │
│   ├── customer_service/
│   │   ├── __init__.py
│   │   └── app.py
│   │
│   ├── payment_service/
│   │   ├── __init__.py
│   │   └── app.py
│   │
│   └── logging_service/
│       ├── __init__.py
│       └── app.py
│
├── scripts/
│   ├── __init__.py
│   └── test_agent.py
│
├── .env
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Configuration

Create a `.env` file in the project root.

Example:

```env
APP_NAME=Enterprise AI Agent Platform
ENVIRONMENT=development

DATABASE_URL=postgresql+psycopg://aiagent:aiagent@localhost:5433/aiagent

JWT_SECRET_KEY=change-this-secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

OPENAI_API_KEY=

ORDER_SERVICE_URL=http://localhost:8001
CUSTOMER_SERVICE_URL=http://localhost:8002
PAYMENT_SERVICE_URL=http://localhost:8003
LOGGING_SERVICE_URL=http://localhost:8004
```

Do not commit real API keys, passwords, or production secrets to GitHub.

---

# 🐍 Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd enterprise-ai-agent-platform
```

## 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

# 🦙 Ollama

Install and run Ollama locally.

Verify that the model is available:

```powershell
ollama list
```

The project is configured to use:

```text
llama3.2
```

Make sure Ollama is available at:

```text
http://localhost:11434
```

---

# ▶️ Running the Microservices

Each service runs independently.

## Order Service

```powershell
python -m uvicorn services.order_service.app:app --host 127.0.0.1 --port 8001
```

## Customer Service

```powershell
python -m uvicorn services.customer_service.app:app --host 127.0.0.1 --port 8002
```

## Payment Service

```powershell
python -m uvicorn services.payment_service.app:app --host 127.0.0.1 --port 8003
```

## Logging Service

```powershell
python -m uvicorn services.logging_service.app:app --host 127.0.0.1 --port 8004
```

Keep the services running while testing the AI agent.

---

# 🧪 Running the AI Agent

From the project root:

```powershell
python -m scripts.test_agent
```

The test script invokes the LangGraph workflow with:

```text
User Query:
Why did order 10452 fail?

Order ID:
10452
```

---

# ✅ Example Result

A successful execution produces:

```text
FINAL RESPONSE
============================================================

Order #10452 investigation complete.

Diagnosis: The order failed because the payment authorization was declined.

Recommended action: Ask the customer to update their payment method and retry the order.
```

---

# 🔍 Example Investigation

For order `10452`, the Logging Service provides evidence similar to:

```json
{
  "order_id": "10452",
  "logs": [
    "Order created",
    "Payment authorization started",
    "Payment authorization failed",
    "Payment authorization retry 1 failed",
    "Payment authorization retry 2 failed",
    "Payment authorization retry 3 failed",
    "Order marked as FAILED"
  ]
}
```

The agent uses this information together with the other enterprise service responses.

---

# 🔗 Service Communication

The agent uses HTTP-based service communication.

For example:

```text
Investigation Agent
       │
       ├── GET /orders/{order_id}
       │
       ├── GET /customers/{customer_id}
       │
       ├── GET /payments/{order_id}
       │
       └── GET /logs/{order_id}
```

This allows the AI layer to work with existing backend services rather than requiring all enterprise data to be placed inside the LLM.

---

# 🧠 Why LangGraph?

LangGraph provides an explicit workflow model for agent execution.

In this project it provides:

* State-based execution
* Multiple agent stages
* Clear workflow transitions
* Separation of investigation and decision logic
* Extensibility for future agent workflows

Current workflow:

```text
START
 ↓
Investigation Agent
 ↓
Decision Agent
 ↓
Response Agent
 ↓
END
```

---

# 🔐 Enterprise Considerations

The platform is structured with enterprise development practices in mind.

Important areas include:

* Service separation
* Environment-based configuration
* API boundaries
* Database integration
* Authentication configuration
* Local LLM deployment
* Automated testing
* Logging
* Containerization

The architecture can be extended toward production environments with additional security, observability, scalability, and deployment infrastructure.

---

# 🧪 Testing

The primary integration test can be executed with:

```powershell
python -m scripts.test_agent
```

The expected result is a complete investigation followed by a final response.

For Python test execution, the recommended command is:

```powershell
python -m pytest -v
```

---

# 🐳 Docker

The project also contains Docker-related configuration for containerized deployment.

The intended architecture allows individual services and supporting infrastructure to be containerized.

Typical components include:

```text
Application Services
        │
        ├── Order Service
        ├── Customer Service
        ├── Payment Service
        └── Logging Service
                │
                ▼
           PostgreSQL

AI Agent
   │
   ▼
Ollama
```

---

# 📊 Current Capabilities

The current implementation demonstrates:

* Multi-agent workflow orchestration
* LangGraph state-based execution
* FastAPI microservices
* HTTP service-to-service communication
* Enterprise investigation workflow
* Local LLM integration
* Evidence-based diagnosis
* Automated agent execution
* PostgreSQL configuration
* Docker-based infrastructure
* Modular Python architecture

---

# 🎯 Example Enterprise Use Cases

The same architecture can be adapted to investigate:

### Order failures

```text
Why did order 10452 fail?
```

### Payment problems

```text
Why was the customer's payment rejected?
```

### Customer issues

```text
Why can't this customer complete the order?
```

### Operational incidents

```text
What caused the order processing failure?
```

### Enterprise support

```text
Investigate this customer incident and recommend the next action.
```

---

# 🚀 Future Extensions

Possible future extensions include:

* Additional enterprise services
* More specialized AI agents
* Conditional LangGraph routing
* Authentication and authorization
* Persistent investigation history
* Advanced PostgreSQL integration
* Observability and tracing
* Prometheus/Grafana monitoring
* CI/CD pipelines
* Kubernetes deployment
* Human-in-the-loop approval
* Enterprise audit trails
* More sophisticated tool selection
* Production LLM providers

These can be added without changing the fundamental investigation workflow.

---

# 📌 Project Status

**Status: Working end-to-end**

The current implementation has been successfully tested with an order investigation scenario involving multiple backend services.

```text
Order Service       ✅
Customer Service    ✅
Payment Service     ✅
Logging Service     ✅
Investigation Agent ✅
Decision Agent      ✅
Response Agent      ✅
LangGraph           ✅
Ollama              ✅
End-to-End Flow     ✅
```

---

# 👨‍💻 Author

**Ahmed Khan**

Software Developer | Python | AI | Machine Learning | Backend Engineering

Based in Stockholm, Sweden.

---

# 📄 License

This project is intended for educational, portfolio, and demonstration purposes.
