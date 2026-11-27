<!-- ============================================================ -->
<!--                         HEADER                                -->
<!-- ============================================================ -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=220&section=header&text=Kau%C3%A3%20Vilas%20Boas&fontSize=58&fontAlignY=38&fontColor=ffffff&animation=fadeIn&desc=Backend%20Engineer%20%C2%B7%20.NET%20%2F%20C%23&descSize=22&descAlignY=60" alt="header"/>
</p>

<p align="center">
  <i>Building regulated, high-availability systems for the Brazilian public health sector.<br/>Shipping the reusable pieces to NuGet.</i>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/kau%C3%A3-vilas-boas-375357225/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  &nbsp;
  <a href="mailto:kauacaldeira@hotmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  &nbsp;
  <a href="https://www.nuget.org/profiles/kauavilasboas"><img src="https://img.shields.io/badge/NuGet-004880?style=for-the-badge&logo=nuget&logoColor=white" alt="NuGet"/></a>
  &nbsp;
  <img src="https://img.shields.io/badge/Salvador%2C%20BR-UTC%E2%88%923-512BD4?style=for-the-badge" alt="Location"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Open%20to%20Remote-43B581?style=for-the-badge" alt="Remote"/>
</p>

<br>

---

## About

I have three years of production experience with .NET. At work I design modular monoliths for state-government health-surveillance workflows, where the domain has to be correct, traceable, and auditable.

Outside of work I maintain [Lumen](https://github.com/KauaVilasBoas/Lumen), a family of authorization and identity libraries for ASP.NET Core published on NuGet. Each package is versioned on its own, its decisions are recorded in ADRs, and a multi-tenant system for a pharmacology lab runs it in production. Every generic API in it started as a requirement from that system.

I default to Clean Architecture, Domain-Driven Design, and CQRS where they earn their place, and a change is done when its unit and integration tests are.

Open to remote backend roles in EU, UK, or US Eastern time zones.

---

## Core expertise

<table align="center">
  <tr>
    <td align="center" valign="top" width="240">
      <b>Core</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="44" alt="C#"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg" width="44" alt=".NET"/>
      <br><br>
      <sub>C# · .NET 8 · ASP.NET Core · EF Core · Dapper</sub>
    </td>
    <td align="center" valign="top" width="240">
      <b>Data</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" width="44" alt="SQL Server"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="44" alt="PostgreSQL"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" width="44" alt="Redis"/>
      <br><br>
      <sub>SQL Server · PostgreSQL · MongoDB · Redis</sub>
    </td>
    <td align="center" valign="top" width="240">
      <b>Infra</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="44" alt="Docker"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg" width="44" alt="Terraform"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" width="44" alt="AWS"/>
      <br><br>
      <sub>Docker · Terraform · AWS · Jenkins · GitHub Actions</sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub><b>Practices</b> &nbsp;·&nbsp; Clean Architecture &nbsp;·&nbsp; DDD &nbsp;·&nbsp; CQRS &nbsp;·&nbsp; Outbox &nbsp;·&nbsp; SOLID &nbsp;·&nbsp; xUnit &nbsp;·&nbsp; Testcontainers &nbsp;·&nbsp; architecture testing</sub>
  <br>
  <sub><b>Currently exploring</b> &nbsp;·&nbsp; distributed systems &nbsp;·&nbsp; system design at scale &nbsp;·&nbsp; observability patterns</sub>
</p>

---

## Engineering principles

> *Architecture is the set of constraints I impose now to make change easier later.*

- **Dependency direction matters more than folder structure.** The layers follow from one rule: the Domain depends on nothing.
- **If a boundary isn't tested, it doesn't exist.** NetArchTest and ArchUnit suites check module isolation and dependency rules, and they fail the build when one breaks. A rule written only in the docs drifts without anyone noticing.
- **A library earns its abstractions from a real consumer.** Every extension point in Lumen exists because a shipping system needed it, and an ADR records why.
- **A modular monolith ships faster than a half-baked microservice.** Splitting a service out adds network calls, deployments, and failure modes, so I do it only when a requirement asks for it.

---

## Currently building

### [Normetry](https://github.com/KauaVilasBoas/Normetry) &nbsp;·&nbsp; <sub>Multi-tenant compliance copilot for regulated establishments</sub>

<p>
  <a href="https://github.com/KauaVilasBoas/Normetry/actions/workflows/ci.yml"><img src="https://github.com/KauaVilasBoas/Normetry/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"/></a>
  &nbsp;
  <a href="https://github.com/KauaVilasBoas/Normetry/releases"><img src="https://img.shields.io/github/v/release/KauaVilasBoas/Normetry?label=release&color=3FB950" alt="Latest release"/></a>
  &nbsp;
  <img src="https://img.shields.io/badge/.NET-10-512BD4?logo=dotnet&logoColor=white" alt=".NET 10"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white" alt="Python 3.12+"/>
  &nbsp;
  <img src="https://img.shields.io/badge/PostgreSQL-pgvector%20%C2%B7%20RLS-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL with pgvector and RLS"/>
  &nbsp;
  <img src="https://img.shields.io/badge/LangGraph-agents-1C3C3C?logo=langchain&logoColor=white" alt="LangGraph"/>
</p>

> A restaurant manager has to follow a food-safety code that runs to hundreds of pages, and the evidence sits in a binder of SOPs, licenses, and temperature logs that nobody re-reads. Normetry reads the establishment's documents against the regulation. Every claim it makes cites an article and, when the claim is about the establishment, the passage of its document that backs the claim.
>
> **Three jurisdictions (FDA Food Code, EU 852/2004, Anvisa RDC 216/2004), questions in Portuguese or English, 131 inspection checklist items.** I build it in public, one phase at a time. The cited regulation chat and the simulated inspection work today, and the regulation change monitor comes next.

### How it's built

- A .NET 10 core (DDD, CQRS, EF Core, outbox, YARP, SignalR) owns the business logic and is the only public entry point. A Python service (FastAPI, LangGraph) owns the AI, and only the gateway can reach it.
- Retrieval is written by hand: pgvector and PostgreSQL full-text search, fused with Reciprocal Rank Fusion, then a multilingual re-ranker. The model answers in structured JSON, and a deterministic guard drops any claim whose quote isn't in a retrieved chunk.
- PostgreSQL Row-Level Security covers every tenant-owned table. The tenant comes from the validated JWT and is set per transaction, so even a buggy query can't return another tenant's rows.
- Every pull request that touches retrieval, ingestion, or the datasets runs the retrieval eval, and CI fails when recall or MRR drops below its floor.

```mermaid
flowchart LR
    WEB["🖥️ Web app<br/><sub>React · TypeScript</sub>"]

    subgraph CORE["🟣 Core · .NET 10"]
        API["API<br/><sub>DDD · CQRS · outbox</sub>"]
        YARP["YARP gateway<br/><sub>/ai/* routes</sub>"]
    end

    subgraph AI["🐍 AI service · Python"]
        CHAT["FastAPI<br/><sub>cited chat · SSE</sub>"]
        AGENT["LangGraph<br/><sub>simulated inspection</sub>"]
    end

    PG[("PostgreSQL<br/><sub>pgvector · full-text · RLS</sub>")]
    MQ[["RabbitMQ"]]
    LLM["Claude"]

    WEB -->|JWT| API
    WEB -->|SSE| YARP
    YARP -->|internal token| CHAT
    API --> PG
    API <-->|events| MQ
    MQ <--> AGENT
    CHAT --> PG
    AGENT --> PG
    CHAT --> LLM
    AGENT --> LLM

    classDef core fill:#0b1220,stroke:#8b5cf6,color:#ede9fe
    classDef ai   fill:#0b1220,stroke:#10b981,color:#d1fae5
    classDef edge fill:#0b1220,stroke:#3b82f6,color:#dbeafe
    classDef data fill:#020617,stroke:#64748b,color:#cbd5e1

    class API,YARP core
    class CHAT,AGENT ai
    class WEB,LLM edge
    class PG,MQ data
```

Only .NET writes the `core` schema and only Python writes the `ai` schema. AI results such as findings and document status reach the core as queue events.

<p align="center">
  The repository covers the architecture, the ADRs behind each decision,<br/>the eval reports, and how to run it locally:
  <br><br>
  <a href="https://github.com/KauaVilasBoas/Normetry"><img src="https://img.shields.io/badge/Read%20the%20docs-KauaVilasBoas%2FNormetry-512BD4?style=for-the-badge&logo=github&logoColor=white" alt="Read the docs"/></a>
</p>

---

## Dashboard

<p align="center">
  <img height="170" src="https://raw.githubusercontent.com/KauaVilasBoas/KauaVilasBoas/main/profile/stats.svg" alt="GitHub stats"/>
  &nbsp;
  <img height="170" src="https://raw.githubusercontent.com/KauaVilasBoas/KauaVilasBoas/main/profile/top-langs.svg" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/KauaVilasBoas/KauaVilasBoas/main/profile/streak.svg" alt="GitHub streak"/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/KauaVilasBoas/KauaVilasBoas/main/profile/isocalendar.svg" alt="Contribution calendar" width="62%"/>
</p>

---

## Connect

<p align="center">
  <a href="https://www.linkedin.com/in/kau%C3%A3-vilas-boas-375357225/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  &nbsp;
  <a href="mailto:kauacaldeira@hotmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  &nbsp;
  <a href="https://www.nuget.org/profiles/kauavilasboas"><img src="https://img.shields.io/badge/NuGet-004880?style=for-the-badge&logo=nuget&logoColor=white" alt="NuGet"/></a>
  &nbsp;
  <a href="https://github.com/KauaVilasBoas"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=100&section=footer" alt="footer"/>
</p>
