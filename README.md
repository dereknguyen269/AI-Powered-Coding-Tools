# 🚀 AI-Powered Coding Tools: Best Practices & Mastery Guide

<div align="center">
    <img src="https://img.shields.io/badge/AI--Powered-blue?style=for-the-badge&logo=artificial-intelligence" />
    <img src="https://img.shields.io/badge/Developer--Productivity-green?style=for-the-badge&logo=speedtest" />
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</div>

---

## 📋 Table of Contents
- [🛡️ Universal Best Practices](#universal-best-practices)
- [🧰 Supported Tools & IDEs](#supported-tools--ides)
- [🔗 Best Practices & Learning Resources](#best-practices--learning-resources)

---

## 🛡️ Universal Best Practices

The following principles apply to **all AI-assisted coding tools**.  
They help you leverage AI effectively **without sacrificing code quality, security, or architectural consistency**.

### 1. 🎯 Effective Prompting (The Most Critical Skill)

* **Be specific and constrained**  
  Avoid vague prompts. Clearly describe *what* you want, *how* it should be done, and *within which constraints*.  
  > ❌ “Refactor this code”  
  > ✅ “Refactor this function to use async/await, add input validation, and apply TypeScript generics.”

* **Define the expected output**  
  Examples:
  - “Generate **unit tests using Jest**”
  - “Return a **Mermaid class diagram**”
  - “Output **only the code diff**, no explanation”

* **Iterate instead of over-prompting**  
  Start simple, review the output, then refine.  
  AI works best in short feedback loops, not one giant prompt.

---

### 2. 📚 Context Is Everything

AI can only produce high-quality results when it understands the **full context**.

* **Explicitly state technical constraints**
  - Frameworks (React Hooks, Spring Boot, FastAPI)
  - Libraries (Zod, Prisma, Pandas)
  - Internal conventions (naming, logging, error handling)

* **Reference related code**
  Do not expect the AI to infer your architecture.
  > *Example:*  
  > “This new endpoint must follow the same error handling pattern as `UserService.ts`.”

* **Explain intent and business logic**
  Tell the AI *why* the code exists, not just *what* to write.

---

### 3. 🛡️ Verification and Accountability (Non-Negotiable)

* **Never commit blindly**  
  AI output should be treated as a **draft**, not final production code.

* **Test everything**
  Especially for:
  - Authentication & authorization
  - Data validation
  - Performance-critical paths

* **AI accelerates — it does not replace expertise**  
  If you don’t fully understand the generated code, you shouldn’t ship it.

---

## 🧰 Supported Tools & IDEs

| Tool / IDE | Description |
|-----------|------------|
| Cursor | AI-first code editor with strong full-repo context |
| Claude Code | CLI-based AI coding assistant for large tasks |
| GitHub Copilot | Real-time AI pair programmer |
| Devin | Autonomous AI software engineer |
| Windsurf | AI-enhanced editor focused on workflow efficiency |
| Kiro | AI-powered development environment for rapid prototyping |
| Antigravity | Lightweight AI assistant for code generation and refactoring |
| Replit AI | Cloud-based IDE with built-in AI and deployment |
| Zed Editor | High-performance collaborative editor with AI support |
| Lovable | AI platform for building and deploying web applications |
| Bolt.new | Instant AI-driven web app generation |
| TRAE | AI-integrated editor for coding and debugging |
| v0 | AI-driven UI and full-stack prototyping tool (Vercel) |
| Manus | Autonomous AI agent for project-level execution |
| Qoder | AI-powered editor with intelligent suggestions |
| Tabnine | Privacy-focused AI code completion |
| JetBrains IDEs | Full IDE suite with AI plugins |
| Codeium | Free AI code completion and chat |
| Sider.AI | AI-powered code review and security analysis |
| Other AI Tools | Prompts, rules, agents, and templates |

---

## 🔗 Best Practices & Learning Resources

### General AI Coding & Agent Resources
- https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- https://github.com/botingw/rulebook-ai
- https://github.com/steipete/agent-rules
- https://github.com/filipecalegario/awesome-vibe-coding
- https://github.com/ai-for-developers/awesome-ai-coding-tools
- https://github.com/dontriskit/awesome-ai-system-prompts
- https://github.com/coleam00/context-engineering-intro
- https://github.com/ghuntley/how-to-build-a-coding-agent
- https://github.com/CyberSecurityUP/Offensive-AI-Agent-Prompts
- https://github.com/e2b-dev/awesome-ai-agents
- https://github.com/wsxiaoys/awesome-ai-coding
- https://github.com/business-science/awesome-generative-ai-data-scientist
- https://github.com/ifokeev/awesome-copilots
- https://github.com/inmve/awesome-ai-coding-techniques
- https://github.com/devtoolsd/awesome-devtools
- https://github.com/Cognitive-Stack/awesome-one-hit-vibe-code

---
### Cursor
- https://github.com/PatrickJS/awesome-cursorrules
- https://github.com/grapeot/devin.cursorrules
- https://github.com/sanjeed5/awesome-cursor-rules-mdc
- https://github.com/kleneway/awesome-cursor-mpc-server


---
### Claude Code
- https://github.com/anthropics/claude-cookbooks
- https://github.com/hesreallyhim/awesome-claude-code
- https://github.com/zebbern/claude-code-guide
- https://github.com/feiskyer/claude-code-settings
- https://github.com/diet103/claude-code-infrastructure-showcase
- https://github.com/gotalab/cc-sdd
- https://github.com/anthropics/claude-quickstarts
- https://github.com/anthropics/claude-code-security-review
- https://github.com/glittercowboy/taches-cc-resources
- https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know
- https://github.com/zilliztech/claude-context
- https://github.com/ruvnet/claude-flow
- https://github.com/steipete/agent-rules
- https://github.com/peterkrueck/Claude-Code-Development-Kit

**Templates:**
- https://github.com/davila7/claude-code-templates
- https://github.com/centminmod/my-claude-code-setup
- https://github.com/discus0434/python-template-for-claude-code

**Prompts:**
- https://github.com/langgptai/awesome-claude-prompts
- https://github.com/Piebald-AI/claude-code-system-prompts
- https://github.com/severity1/claude-code-prompt-improver
- https://github.com/JeremyMorgan/Claude-Code-Reviewing-Prompts
- https://github.com/mustafakendiguzel/claude-code-ui-agents

**Agents:**
- https://github.com/wshobson/agents
- https://github.com/vijaythecoder/awesome-claude-agents
- https://github.com/VoltAgent/awesome-claude-code-subagents
- https://github.com/davepoon/claude-code-subagents-collection
- https://github.com/iannuttall/claude-agents
- https://github.com/lst97/claude-code-sub-agents
- https://github.com/darcyegb/ClaudeCodeAgents
- https://github.com/hesreallyhim/a-list-of-claude-code-agents
- https://github.com/stretchcloud/claude-code-unified-agents
- https://github.com/Dicklesworthstone/claude_code_agent_farm
- https://github.com/IncomeStreamSurfer/claude-code-agents-wizard-v2
- https://github.com/zhsama/claude-sub-agent
- https://github.com/vanzan01/claude-code-sub-agent-collective

**Skills:**
- https://github.com/obra/superpowers
- https://github.com/travisvn/awesome-claude-skills
- https://github.com/simonw/claude-skills
- https://github.com/zxkane/aws-skills
- https://github.com/daymade/claude-code-skills
- https://github.com/jeremylongshore/claude-code-plugins-plus-skills
- https://github.com/alirezarezvani/claude-skills
- https://github.com/czlonkowski/n8n-skills
- https://github.com/obra/superpowers-skills
- https://github.com/abubakarsiddik31/claude-skills-collection

---
### GitHub Copilot
- https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming
- https://github.com/github/awesome-copilot
- https://github.com/Vishavjeet6/awesome-copilot-instructions
- https://github.com/dfinke/awesome-copilot-chatmodes
- https://github.com/Code-and-Sorts/awesome-copilot-agents

---
### Windsurf
- https://github.com/ichoosetoaccept/awesome-windsurf

---
### TRAE
- https://github.com/jojomensah89/awesome-trae

---

## Learning Resources

Articles, guides, and references for learning AI-assisted development.

- [How to Build a Coding Agent](https://github.com/ghuntley/how-to-build-a-coding-agent)
- [Awesome AI Coding Tools](https://github.com/ai-for-developers/awesome-ai-coding-tools)
- [Awesome Vibe Coding](https://github.com/filipecalegario/awesome-vibe-coding)
- [Mastering GitHub Copilot](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Spec-Driven Development with Claude Code](https://github.com/gotalab/cc-sdd)

---

## Contributing

Contributions are welcome!

Please ensure:
- Links are relevant and maintained
- Descriptions are concise and neutral
- No duplicate or promotional entries

Open an issue or submit a pull request.

---

## License

This list is licensed under the **MIT License**.
