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

  > A portfolio piece built to demonstrate end-to-end architectural decisions on a non-trivial domain — not just "another auth API". Multi-solution Clean Architecture with CQRS, ports & adapters, a Razor backoffice     consuming its
   own JWT, and recurring jobs on Hangfire.

  ```mermaid
  flowchart TB
      CLIENT(["🌐 HTTP Client"])
      BROWSER(["👤 Admin Browser"])

      subgraph PRES["🎯 Presentation"]
          API["<b>AegisIdentity.Api</b><br/><sub>Controllers · IMediator</sub>"]
          BO["<b>AegisIdentity.Backoffice</b><br/><sub>ASP.NET MVC · cookie auth + JWT</sub>"]
      end

      subgraph APP["⚡  Application · CQRS via MediatR"]
          PIPE["<b>ValidationBehavior</b><br/><sub>FluentValidation pipeline · fail-fast</sub>"]
          CMD["<b>CommandHandlers</b><br/><sub>RegisterUser · LoginUser</sub>"]
          QRY["<b>ReadModels</b><br/><sub>Query handlers (scaffold)</sub>"]
          EVT["<b>EventHandlers</b><br/><sub>Notification handlers (scaffold)</sub>"]
      end

      subgraph DOM["💎 Domain · zero external dependencies"]
          ENT["<b>Entities & Value Objects</b><br/>User · RefreshToken<br/>EmailConfirmationToken"]
          PORT["<b>Ports (interfaces)</b><br/>IUserRepository · IJwtService<br/>IPasswordHasher · IEmailService"]
      end

      subgraph INFRA["🔧 Infrastructure · adapters"]
          SEC["<b>Infrastructure</b><br/><sub>JWT · BCrypt · PasswordValidator · Options</sub>"]
          DAL["<b>DataAccess</b><br/><sub>MongoDbContext · Repositories<br/>ClassMaps · Index initializer</sub>"]
          INT["<b>Integration</b><br/><sub>MailKit · PwnedPasswordsClient (HIBP)</sub>"]
      end

      subgraph JOB["⏰  Jobs · Hangfire + Hangfire.Mongo"]
          HF["<b>AegisIdentity.Jobs</b><br/><sub>Recurring scheduler</sub>"]
          CLEAN["<b>CleanupExpiredRefreshTokensJob</b><br/><sub>cron · 03:00 UTC daily</sub>"]
      end

      DB[("🗄️<b>MongoDB</b><br/>AegisIdentity_db<br/>AegisIdentity_hangfire")]
      SMTP[/"📧 SMTP server"/]
      HIBP[/"🛡️HaveIBeenPwned API<br/><sub>k-anonymity range query</sub>"/]

      CLIENT -- "POST /api/auth/register" --> API
      BROWSER -- "session cookie" --> BO
      BO -- "AuthApiClient · Bearer JWT" --> API
      BO -- "/hangfire dashboard" --> HF

      API -- "Command" --> PIPE
      PIPE -- "validated" --> CMD
      CMD --> ENT
      CMD -. "depends on" .-> PORT

      SEC -. "implements" .-> PORT
      DAL -. "implements" .-> PORT
      INT -. "implements" .-> PORT

      DAL ==> |"BSON · async I/O"| DB
      INT -. "SendAsync" .-> SMTP
      INT -. "range API" .-> HIBP

      HF --> CLEAN
      CLEAN -. "DeleteExpiredAsync" .-> DAL
      HF ==> |"job storage"| DB

      classDef domain     fill:#512BD4,stroke:#A78BFA,color:#fff,stroke-width:2px
      classDef pres       fill:#0b1220,stroke:#3b82f6,color:#dbeafe
      classDef app        fill:#0b1220,stroke:#10b981,color:#d1fae5
      classDef infra      fill:#0b1220,stroke:#f59e0b,color:#fde68a
      classDef jobs       fill:#0b1220,stroke:#ec4899,color:#fce7f3
      classDef external   fill:#020617,stroke:#64748b,color:#cbd5e1
      classDef db         fill:#13aa52,stroke:#00ed64,color:#ffffff,stroke-width:3px

      class ENT,PORT domain
      class API,BO pres
      class PIPE,CMD,QRY,EVT app
      class SEC,DAL,INT infra
      class HF,CLEAN jobs
      class CLIENT,BROWSER,SMTP,HIBP external
      class DB db

      linkStyle 0  stroke:#3b82f6,stroke-width:2px
      linkStyle 1  stroke:#3b82f6,stroke-width:2px
      linkStyle 2  stroke:#3b82f6,stroke-width:2px
      linkStyle 3  stroke:#ec4899,stroke-width:2px
      linkStyle 4  stroke:#10b981,stroke-width:2px
      linkStyle 5  stroke:#10b981,stroke-width:2px
      linkStyle 6  stroke:#a78bfa,stroke-width:2px
      linkStyle 7  stroke:#a78bfa,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 8  stroke:#a78bfa,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 9  stroke:#a78bfa,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 10 stroke:#a78bfa,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 11 stroke:#00ed64,stroke-width:3.5px
      linkStyle 12 stroke:#f59e0b,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 13 stroke:#f59e0b,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 14 stroke:#ec4899,stroke-width:2px
      linkStyle 15 stroke:#ec4899,stroke-width:2px,stroke-dasharray:4 4
      linkStyle 16 stroke:#00ed64,stroke-width:3.5px
  ```

  <sub>**Reading the diagram** — solid arrows = in-process synchronous flow · dashed arrows = port/adapter wiring & external I/O · thick green arrows = MongoDB read/write paths · Domain (purple) has zero outgoing dependencies;
  every other layer depends inward on it.</sub>

  | Decision | Rationale |
  |---|---|
  | **Multi-solution Clean Architecture** | Six layer solutions (`Domain` · `Application` · `Infrastructure` · `Presentation` · `Jobs` · `SharedKernel`) aggregated by a root `.sln`. Each layer can be opened, built and reasoned
  about in isolation. |
  | **CQRS via MediatR with nested types** | `Command`, `Result`, `Validator` are `sealed record`s nested inside the handler. One file = one use case, fully self-contained. No anemic DTO layer between Controller and Handler. |
  | **`ValidationBehavior<TRequest,TResponse>` pipeline** | FluentValidation runs *before* the handler. Cheap input checks fail fast; I/O-bound rules (uniqueness, HIBP) stay inside `Handle()`. |
  | **Ports & Adapters (Dependency Inversion)** | All infrastructure contracts (`IUserRepository`, `IJwtService`, `IEmailService`, `IPasswordHasher`…) live in **Domain**. Adapters in Infrastructure are wired by DI — Domain has
  zero external references, verified by the compiler. |
  | **Razor Backoffice consumes its own JWT** | The MVC backoffice authenticates against the public API via a typed `AuthApiClient`, stores the JWT inside an HttpOnly cookie session, and exposes the Hangfire dashboard guarded by
   cookie auth. |
  | **Hangfire + Hangfire.Mongo for recurring work** | API hosts the Hangfire server; jobs are scheduled on startup. `CleanupExpiredRefreshTokensJob` deletes expired refresh tokens daily at 03:00 UTC via the same
  `IRefreshTokenRepository` port. |
  | **Central Package Management** | `Directory.Packages.props` is the single source of truth for 29 NuGet versions across 13 projects. Zero orphans, zero drift. |
  | **`TreatWarningsAsErrors` + nullable enabled globally** | Quality bar enforced by the compiler from `Directory.Build.props`. No "we'll clean it up later". |
  | **Startup-time options validation** | `ValidateDataAnnotations().ValidateOnStart()` — misconfiguration crashes on boot, never silently in production. |
  | **Global `IExceptionHandler` → RFC 7807** | `ValidationException` → `ValidationProblemDetails` 400; `ConflictException` → 409. Consistent machine-readable errors. |
  | **xUnit + Testcontainers integration tests** | 222 unit tests; integration suite spins up real MongoDB via Testcontainers. Tests are a first-class deliverable, not an afterthought. |

  <p align="center">
    <img src="https://img.shields.io/badge/Status-Active%20Development-43B581?style=flat-square" alt="Active"/>
    &nbsp;
    <img src="https://img.shields.io/badge/.NET-8-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt=".NET 8"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Architecture-Clean%20%2B%20CQRS-A78BFA?style=flat-square" alt="Clean Architecture + CQRS"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Mediator-MediatR-blue?style=flat-square" alt="MediatR"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Database-MongoDB-13AA52?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Auth-JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Jobs-Hangfire-EC4899?style=flat-square" alt="Hangfire"/>
    &nbsp;
    <img src="https://img.shields.io/badge/Tested-xUnit-512BD4?style=flat-square&logo=dotnet&logoColor=white" alt="xUnit"/>
  </p>

  ---

## Dashboard

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=KauaVilasBoas&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Activity&bg_color=0D1117&color=A78BFA&line=512BD4&point=A78BFA" alt="Contribution activity graph" width="100%"/>
</p>
<p align="center">
  <img height="200" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=KauaVilasBoas&theme=tokyonight" alt="GitHub stats"/>
  &nbsp;
  <img height="200" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=KauaVilasBoas&theme=tokyonight&utcOffset=-3" alt="Productive time"/>
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
