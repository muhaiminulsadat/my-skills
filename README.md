# 🧠 My Skills

A curated monorepo of custom AI agent skills for **Antigravity**, **Claude Code**, **Cursor**, **Codex**, and other modern AI coding assistants.

---

## 🚀 Quick Install

### Option A: Interactive Picker (Choose 1, Multiple, or All)
Run this in any project directory to launch the interactive selection menu:
```bash
npx skills add muhaiminulsadat/my-skills
```
> Select the specific skills you want, or press `a` to install all skills at once.

---

### Option B: Install a Specific Skill Directly
To install a single skill immediately without the prompt:
```bash
npx skills add muhaiminulsadat/my-skills --skill <skill-name>
```

*(Add `-g` to install globally across your machine: `npx skills add muhaiminulsadat/my-skills --skill <skill-name> -g`)*

---

### Option C: Download Directly with `degit` (Zero-Dependency)
```bash
npx degit muhaiminulsadat/my-skills/skills/<skill-name> .agents/skills/<skill-name>
```

---

## 📦 Skills Catalog

| Skill Name | Description | Direct Install Command |
| :--- | :--- | :--- |
| **`create-homework-sheet`** | Generates print-ready A4 student homework practice worksheets and PDFs with diagrams for every question. | `npx skills add muhaiminulsadat/my-skills --skill create-homework-sheet` |
| **`learn-easier`** | Turns course materials into print-ready A4 exam-revision study notes and cheat sheets. | `npx skills add muhaiminulsadat/my-skills --skill learn-easier` |
| **`plan-mode`** | Senior technical co-founder & architect discovery interview skill before writing code. | `npx skills add muhaiminulsadat/my-skills --skill plan-mode` |
| **`exam-cram-bangla`** | Ultra-compact exam prep & study notes in easy Bangla with English technical keywords & mnemonics. | `npx skills add muhaiminulsadat/my-skills --skill exam-cram-bangla` |

---

## 🛠️ Repository Layout

```text
my-skills/
├── README.md
└── skills/
    ├── create-homework-sheet/
    ├── exam-cram-bangla/
    ├── learn-easier/
    └── plan-mode/
```

---

## 📄 License
MIT
