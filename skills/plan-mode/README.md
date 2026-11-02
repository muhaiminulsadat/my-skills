# 📐 Plan Mode (`plan-mode`)

> **Senior Technical Co-Founder & Product Architect Interview Skill**  
> Complete architectural and product alignment **before** writing a single line of code or implementation plan.

---

## 💡 Why Plan Mode?

Jumping straight into code or boilerplate scaffolding without answering high-leverage architectural questions leads to costly rewrites, misaligned data models, and broken auth/state patterns.

**Plan Mode** forces your AI agent to act as your **Senior Technical Co-founder and Product Architect**. Instead of writing code, it conducts a low-cognitive-load, iterative interview in small batches of 3–6 questions, proactively resolves ambiguity, flags conflicting constraints, tracks assumptions, and produces a crystal-clear aligned specification summary.

---

## ⚡ Multi-Agent Compatibility

This repository is ready to use across all modern AI coding tools and environments:

| Coding Agent / Platform | Integration Method | Configuration File |
| :--- | :--- | :--- |
| **Google Antigravity** | Global / Workspace Agent Skill | [`SKILL.md`](SKILL.md) |
| **Claude Code (CLI) / Anthropic** | Project Memory / System Prompt | [`CLAUDE.md`](CLAUDE.md) |
| **Cursor** | Workspace Rules | [`.cursorrules`](.cursorrules) |
| **Windsurf (Cascade)** | Workspace Rules | [`.windsurfrules`](.windsurfrules) |
| **GitHub Copilot** | Repository Instructions | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| **Codex / Devin / Generic Agents** | Standard Agent Instructions | [`AGENTS.md`](AGENTS.md) |
| **ChatGPT / OpenAI Custom GPT** | Agent Manifest & Actions | [`agents/openai.yaml`](agents/openai.yaml) |
| **Web UIs (Claude Web, ChatGPT, v0, Bolt)** | Copy-paste Universal Prompt | [`plan-mode-universal-prompt.md`](plan-mode-universal-prompt.md) |

---

## 🚀 Installation & Usage

### ⚡ 1-Line CLI Install (Recommended: `skills` CLI)
Install directly into your current project or globally across all agents without manual cloning:

```bash
# Add to current project (auto-detects Cursor, Claude, Antigravity, etc.)
npx skills add muhaiminulsadat/plan-mode

# Install globally for all agents on your machine
npx skills add muhaiminulsadat/plan-mode -g

# Or if you have the skills CLI installed (npm i -g skills):
skills add muhaiminulsadat/plan-mode
```

### 📦 Install via npm
You can also add it as a developer dependency in any Node project:
```bash
npm install -D github:muhaiminulsadat/plan-mode
# or
pnpm add -D github:muhaiminulsadat/plan-mode
```

---

### 1. In Google Antigravity
Clone or place this folder in your Antigravity skills directory:
```bash
# Windows
git clone https://github.com/muhaiminulsadat/plan-mode.git "$env:USERPROFILE\.gemini\config\skills\plan-mode"

# macOS / Linux
git clone https://github.com/muhaiminulsadat/plan-mode.git ~/.gemini/config/skills/plan-mode
```
Trigger anytime in chat with:
> `/plan-mode` or *"Let's use plan mode for a new web app"*

### 2. In Cursor / Windsurf / Claude Code
Copy the corresponding config file (`.cursorrules`, `.windsurfrules`, or `CLAUDE.md`) into your project root:
```bash
cp .cursorrules /path/to/your-project/
# or
cp CLAUDE.md /path/to/your-project/
```

### 3. In Web LLM Chats (Claude.ai, ChatGPT, Gemini, DeepSeek)
Copy the full contents of [`plan-mode-universal-prompt.md`](plan-mode-universal-prompt.md) and paste it into your initial message before describing your app idea.

---

## 🎯 Core Operating Principles

1. **Small Batches Only (3–6 Questions):** No wall of 30 questions. Questions are delivered in bite-sized, thematic batches.
2. **High Leverage First:** Tackles data ownership, auth boundaries, client vs server model, and rendering architecture before styling or superficial features.
3. **Reflect & Advance:** Reflects back its understanding in 1–2 sentences before presenting the next batch.
4. **Push Back on Vagueness:** If an answer is vague, offers 2–3 concrete options, recommends a sensible default, and explains the trade-offs.
5. **Detect & Flag Conflicts:** Proactively identifies and resolves contradictions with earlier answers.
6. **Track Assumptions:** Any unknown or skipped detail is marked with `[ASSUMPTION]` and logged.
7. **Respect Technology Choices:** Never silently swaps libraries or frameworks without explicit consent.
8. **Final Handoff:** Produces a structured Spec Summary, lists all Assumptions and Open Risks, and asks:
   > *"Ready for me to turn this into an implementation plan?"*

---

## 🧭 Topic Roadmap

- **Product & Users:** Problem solved, target personas, primary job-to-be-done, explicit non-goals for v1.
- **Core User Flows:** First-time visitor path, sign up/onboarding, core workspace, primary action, returning user experience.
- **Pages & Routing:** Public vs protected vs admin routes, layouts, dynamic parameters.
- **UI & Responsive Behavior:** Mobile/desktop priorities, component system (shadcn/ui, Tailwind), dark mode, key states (empty/loading/error).
- **Data Model:** Core entities, relationships, unique constraints, ownership hierarchy, cascade/soft deletion.
- **Auth & Authorization:** Auth methods (OAuth, passkeys, magic links), RBAC, session handling, account deletion.
- **Frontend/Backend Architecture:** Server vs client rendering (SSR/SSG/SPA/RSC), API style (Server Actions, REST, tRPC), caching & revalidation.
- **State & Data Flow:** Server state (TanStack Query/SWR), client UI state (Zustand), URL search params, real-time vs polling.
- **Forms & Uploads:** Validation (Zod, React Hook Form), file upload pipelines (presigned S3/R2 vs server proxy), file limits & MIME types.
- **External Services & Integrations:** DB, storage, email, payments (Stripe/LemonSqueezy), AI LLMs, Sentry, analytics.
- **Background Tasks:** Asynchronous queues (Inngest, BullMQ), email delivery, webhooks, idempotency, retries.
- **SEO & Web Standards:** Metadata, OpenGraph, sitemaps, JSON-LD, crawlability.
- **Security & Edge Cases:** Secret protection, rate limiting, CSRF, offline handling, duplicate submission prevention.
- **Monetization & Billing:** Free tier vs subscriptions vs usage credits, paywalls, cancellation flows.
- **Performance & Environments:** Traffic targets, CDN, hosting target (Vercel, Supabase, Cloudflare, AWS), CI/CD.
- **Observability & Testing:** Structured logging, error alerts, test boundaries (Playwright, unit), definition of "done".
- **Constraints & Future-Proofing:** Budget/deadline constraints, non-negotiable tech stack, future v2 considerations.

---

## 📄 License
MIT License. Free to use and adapt across all personal and commercial projects.
