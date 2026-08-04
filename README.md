<!-- ============================================================ -->
<!--                         HEADER                                -->
<!-- ============================================================ -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,2,30&height=220&section=header&text=Kau%C3%A3%20Vilas%20Boas&fontSize=58&fontAlignY=38&fontColor=ffffff&animation=fadeIn&desc=Backend%20Engineer%20%C2%B7%20.NET%20%2F%20C%23&descSize=22&descAlignY=60" alt="header"/>
</p>

<p align="center">
  <i>Building regulated, high-availability systems for the Brazilian public health sector —<br/>and shipping the reusable pieces to NuGet.</i>
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

Three years of production experience in the .NET ecosystem. My day-to-day is designing modular monoliths that serve health-surveillance regulatory workflows for state government — systems where domain correctness, traceability, and auditability matter more than novelty.

Outside of work I maintain **[Lumen](https://github.com/KauaVilasBoas/Lumen)**, a family of authorization and identity libraries for ASP.NET Core published on NuGet. It isn't a demo repository: it's versioned independently, documented with ADRs, and consumed in production by a multi-tenant laboratory system serving a real pharmacology lab. Having a real consumer is what keeps it honest — every generic API in it was paid for by a concrete requirement, not invented in a vacuum.

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

## Engineering Principles

> *Architecture is the set of constraints I impose now to make change easier later.*

- **Dependency direction matters more than folder structure.** Layers are a side effect; the real rule is that the Domain depends on nothing — everything else is consequence.
- **If a boundary isn't tested, it doesn't exist.** Module isolation and dependency rules are asserted by NetArchTest/ArchUnit suites that fail the build. Documentation drifts; a red test doesn't.
- **A library earns its abstractions from a real consumer.** Generic APIs invented in a vacuum are guesses. Every extension point in Lumen exists because a shipping system needed it — and I wrote down *why* in an ADR.
- **Adding a package must never change existing behaviour.** A library that silently enforces something on install is a library you can't adopt incrementally.
- **Misconfiguration in production is silent until it isn't.** I validate options at startup. The app either boots correctly, or it crashes loudly. There is no third state.
- **A modular monolith ships faster than a half-baked microservice.** Distribution is a cost, not a feature. I make it a deliberate choice, never a default.
- **Logs are an API for your future self under stress.** Structure them, name them, treat breaking changes seriously.

---

## Currently Building

### [Lumen](https://github.com/KauaVilasBoas/Lumen) &nbsp;·&nbsp; <sub>Plug-in authorization & identity for ASP.NET Core</sub>

<p>
  <a href="https://www.nuget.org/packages/Lumen.Authorization"><img src="https://img.shields.io/nuget/v/Lumen.Authorization?logo=nuget&label=Lumen.Authorization&color=004880" alt="Lumen.Authorization"/></a>
  &nbsp;
  <a href="https://www.nuget.org/packages/Lumen.Identity"><img src="https://img.shields.io/nuget/v/Lumen.Identity?logo=nuget&label=Lumen.Identity&color=004880" alt="Lumen.Identity"/></a>
  &nbsp;
  <a href="https://www.nuget.org/profiles/kauavilasboas"><img src="https://img.shields.io/badge/11%20packages-5.3k%2B%20downloads-43B581?logo=nuget&logoColor=white" alt="11 packages · 5.3k downloads"/></a>
  &nbsp;
  <a href="https://github.com/KauaVilasBoas/Lumen/actions/workflows/ci.yml"><img src="https://github.com/KauaVilasBoas/Lumen/actions/workflows/ci.yml/badge.svg" alt="CI"/></a>
</p>

> Every ASP.NET Core app ends up hand-rolling the same thing: a permissions table, a join to roles, an `[Authorize]` policy per endpoint, and a half-finished admin screen nobody wants to own. Lumen packages that. Decorate an action with `[RequirePermission]`, mount an admin console at `/lumen`, and keep full ownership of your permission catalog.
>
> **11 packages across three families — 5,000+ downloads in the first two weeks after launch.** SQL Server and PostgreSQL, Redis or in-memory caching, and a consumer in production keeping the API honest.

### How it plugs in

```mermaid
flowchart LR
    subgraph APP["🧩 Your ASP.NET Core app"]
        EP["Endpoints<br/><sub>[RequirePermission]</sub>"]
        SEED["Your EF migration<br/><sub>SeedLumenPermission*</sub>"]
        BO["/lumen<br/><sub>mounted backoffice</sub>"]
    end

    subgraph LIB["📦 Lumen.Authorization"]
        ENF["AspNetCore<br/><sub>policy provider · enforcement</sub>"]
        CORE["Core<br/><sub>profiles · permissions · CQRS</sub>"]
        MIG["Migrations<br/><sub>Lumen schema · auto-apply</sub>"]
    end

    IDN["📦 Lumen.Identity<br/><sub>JWT · refresh tokens (optional)</sub>"]
    DB[("SQL Server /<br/>PostgreSQL")]
    CACHE[("Redis /<br/>MemoryCache")]

    EP --> ENF --> CORE
    BO --> CORE
    CORE --> DB
    CORE --> CACHE
    MIG --> DB
    SEED --> DB
    IDN -. "authenticates the claim<br/>the library reads userId from" .-> ENF

    classDef app  fill:#0b1220,stroke:#3b82f6,color:#dbeafe
    classDef lib  fill:#0b1220,stroke:#f59e0b,color:#fde68a
    classDef idn  fill:#0b1220,stroke:#10b981,color:#d1fae5
    classDef data fill:#020617,stroke:#64748b,color:#cbd5e1

    class EP,SEED,BO app
    class ENF,CORE,MIG lib
    class IDN idn
    class DB,CACHE data
```

The library owns the `Lumen` schema and the enforcement pipeline. **You** own the catalog, the identity provider, and every enforcement point.

<p align="center">
  <b>For more information</b> — the four inviolable principles, the full package matrix,<br/>the ADRs behind each decision and a copy-paste quick start:
  <br><br>
  <a href="https://github.com/KauaVilasBoas/Lumen"><img src="https://img.shields.io/badge/Read%20the%20docs-KauaVilasBoas%2FLumen-512BD4?style=for-the-badge&logo=github&logoColor=white" alt="Read the docs"/></a>
</p>

---

## Dashboard

<!-- Todos os cards tematizados no roxo .NET (#512BD4 / #A78BFA sobre #0D1117)
     para dar identidade de marca em vez de tema genérico. -->

<p align="center">
  <img height="170" src="https://github-readme-stats.vercel.app/api?username=KauaVilasBoas&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&hide_rank=false&bg_color=0D1117&title_color=A78BFA&icon_color=512BD4&text_color=c9d1d9&ring_color=A78BFA" alt="GitHub stats"/>
  &nbsp;
  <img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=KauaVilasBoas&layout=compact&hide_border=true&langs_count=8&hide=html,css,tex&bg_color=0D1117&title_color=A78BFA&text_color=c9d1d9" alt="Top languages"/>
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=KauaVilasBoas&hide_border=true&background=0D1117&stroke=30363d&ring=512BD4&fire=A78BFA&currStreakNum=c9d1d9&currStreakLabel=A78BFA&sideNums=c9d1d9&sideLabels=8b949e&dates=8b949e" alt="GitHub streak"/>
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=KauaVilasBoas&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Activity&bg_color=0D1117&color=A78BFA&line=512BD4&point=A78BFA" alt="Contribution activity graph" width="100%"/>
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
