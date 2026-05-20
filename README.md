<!-- ============================================================ -->
<!--                         HEADER                                -->
<!-- ============================================================ -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=220&section=header&text=Kau%C3%A3%20Vilas%20Boas&fontSize=58&fontAlignY=38&fontColor=ffffff&animation=fadeIn&desc=Backend%20Engineer%20%C2%B7%20.NET%20%2F%20C%23&descSize=22&descAlignY=60" alt="header"/>
</p>

<p align="center">
  <i>Building regulated, high-availability systems for the Brazilian public health sector.</i>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/kau%C3%A3-vilas-boas-375357225/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  &nbsp;
  <a href="mailto:kauacaldeira@hotmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  &nbsp;
  <img src="https://img.shields.io/badge/Salvador%2C%20BR-UTC%E2%88%923-512BD4?style=for-the-badge" alt="Location"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Open%20to%20Remote-43B581?style=for-the-badge" alt="Remote"/>
</p>

<br>

---

## About

Three years of production experience in the .NET ecosystem. My day-to-day is designing modular monoliths that serve health-surveillance regulatory workflows for state government — systems where domain correctness, traceability, and auditability matter more than novelty.

I default to **Clean Architecture**, **Domain-Driven Design**, and **CQRS** where they earn their place. Unit and integration tests are part of *done*, not an afterthought.

Open to remote backend roles aligned with **EU**, **UK**, or **US Eastern** time zones.

---

## Core Expertise

<table align="center">
  <tr>
    <td align="center" valign="top" width="240">
      <b>Core</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="44" alt="C#"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/dotnetcore/dotnetcore-original.svg" width="44" alt=".NET"/>
      <br><br>
      <sub>C# · .NET 8 · ASP.NET Core · EF Core</sub>
    </td>
    <td align="center" valign="top" width="240">
      <b>Data</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg" width="44" alt="SQL Server"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="44" alt="PostgreSQL"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" width="44" alt="MongoDB"/>
      <br><br>
      <sub>SQL Server · PostgreSQL · MongoDB</sub>
    </td>
    <td align="center" valign="top" width="240">
      <b>Infra</b>
      <br><br>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="44" alt="Docker"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jenkins/jenkins-original.svg" width="44" alt="Jenkins"/>
      &nbsp;&nbsp;
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="44" alt="Git"/>
      <br><br>
      <sub>Docker · Jenkins · Git · IIS / Windows Server</sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub><b>Practices</b> &nbsp;·&nbsp; Clean Architecture &nbsp;·&nbsp; DDD &nbsp;·&nbsp; CQRS &nbsp;·&nbsp; SOLID &nbsp;·&nbsp; xUnit &nbsp;·&nbsp; integration testing</sub>
  <br>
  <sub><b>Currently exploring</b> &nbsp;·&nbsp; distributed systems &nbsp;·&nbsp; system design at scale &nbsp;·&nbsp; observability patterns</sub>
</p>

---

## Engineering Principles

> *Architecture is the set of constraints I impose now to make change easier later.*

- **Dependency direction matters more than folder structure.** Layers are a side effect; the real rule is that the Domain depends on nothing — everything else is consequence.
- **Misconfiguration in production is silent until it isn't.** I validate options at startup. The app either boots correctly, or it crashes loudly. There is no third state.
- **Tests aren't a quality gate. They are a contract with future-me** — the engineer who has forgotten how this works six months from now.
- **A modular monolith ships faster than a half-baked microservice.** Distribution is a cost, not a feature. I make it a deliberate choice, never a default.
- **Logs are an API for your future self under stress.** Structure them, name them, treat breaking changes seriously.

---

## Currently Building

### [AegisIdentity](https://github.com/KauaVilasBoas/AegisIdentity) &nbsp;·&nbsp; <sub>Identity & Authentication service in .NET 8</sub>

> A portfolio piece built to demonstrate end-to-end architectural decisions on a non-trivial domain — not just "another auth API".

```mermaid
flowchart LR
    API["<b>API</b><br/><sub>HTTP · routes</sub>"]
    APP["<b>Application</b><br/><sub>Use cases · DTOs</sub>"]
    DOM["<b>Domain</b><br/><sub>Entities · rules</sub>"]
    INF["<b>Infrastructure</b><br/><sub>MongoDB · JWT</sub>"]

    API --> APP
    APP --> DOM
    INF --> DOM

    style DOM fill:#512BD4,stroke:#A78BFA,color:#fff,stroke-width:2px
    style API fill:#1f2937,stroke:#374151,color:#fff
    style APP fill:#1f2937,stroke:#374151,color:#fff
    style INF fill:#1f2937,stroke:#374151,color:#fff
```

| Decision | Rationale |
|---|---|
| **Clean Architecture, strict layer rules** | `Api → Application → Domain ← Infrastructure`. Domain has zero external dependencies. |
| **Central Package Management** | Single source of truth for versions across the entire solution. |
| **`TreatWarningsAsErrors` enabled** | Compiler-enforced quality bar. No "we'll clean it up later". |
| **Startup-time options validation** | `ValidateDataAnnotations().ValidateOnStart()` — misconfigurations crash on boot, never silently in production. |
| **JWT + MongoDB + Razor Pages backoffice** | Real authentication flow plus administrative UI — not a textbook example. |
| **xUnit + integration tests** | Tests as a first-class deliverable. |

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active%20Development-43B581?style=flat-square" alt="Active"/>
  &nbsp;
  <img src="https://img.shields.io/badge/.NET-8-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt=".NET 8"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Architecture-Clean-A78BFA?style=flat-square" alt="Clean Architecture"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Auth-JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Tested-xUnit-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="xUnit"/>
</p>

---

## Dashboard

<p align="center">
  <img height="172" src="https://github-readme-stats.vercel.app/api?username=KauaVilasBoas&show_icons=true&hide_border=true&bg_color=0D1117&title_color=A78BFA&text_color=ffffff&icon_color=512BD4&count_private=true&include_all_commits=true&card_width=440" alt="GitHub stats"/>
  &nbsp;
  <img height="172" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KauaVilasBoas&layout=compact&hide_border=true&bg_color=0D1117&title_color=A78BFA&text_color=ffffff&langs_count=8&card_width=340" alt="Top languages"/>
</p>

<p align="center">
  <img height="172" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=KauaVilasBoas&theme=github_dark&utcOffset=-3" alt="Productive time"/>
  &nbsp;
  <img height="172" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=KauaVilasBoas&theme=github_dark" alt="Most committed languages this year"/>
</p>

---

## Connect

<p align="center">
  <a href="https://www.linkedin.com/in/kau%C3%A3-vilas-boas-375357225/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  &nbsp;
  <a href="mailto:kauacaldeira@hotmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  &nbsp;
  <a href="https://github.com/KauaVilasBoas"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=100&section=footer" alt="footer"/>
</p>
