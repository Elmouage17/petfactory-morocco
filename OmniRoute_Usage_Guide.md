# OmniRoute Usage Guide

An open-source AI gateway that routes requests across 290+ providers and 500+ models through a single OpenAI-compatible endpoint. MIT-licensed, local-first, with intelligent fallback and token compression.

---

## What is OmniRoute

OmniRoute sits between your AI-powered tools (Claude Code, Cursor, Codex, Cline) and the model providers (Anthropic, OpenAI, Google, etc.). Instead of integrating each provider individually, you point your tools at OmniRoute's local endpoint and let it handle provider selection, failover, quota tracking, and cost optimization.

**Key capabilities:**

- **Unified endpoint** — one `http://localhost:20128/v1` for everything
- **290+ providers** including 90+ free tiers, 500+ models
- **Intelligent routing** with 19 strategies: priority, weighted, cost-optimized, round-robin, and more
- **Automatic fallback** — quota-aware, circuit-breaker-protected
- **Token compression** (RTK + Caveman) reducing usage by 15–95%
- **Built-in MCP server** with 87+ tools across stdio, SSE, and HTTP transports
- **Dashboard** for visual management at `localhost:20128`

---

## Quick Start

### npm (recommended)

```bash
npx omniroute@latest
```

### Global install

```bash
npm install -g omniroute
omniroute
```

### pnpm

```bash
pnpm add -g omniroute@latest \
  --allow-build=better-sqlite3 \
  --allow-build=@swc/core
omniroute
```

### Docker

```bash
docker run -p 20128:20128 diegosouzapw/omniroute
```

### From source

```bash
git clone https://github.com/diegosouzapw/OmniRoute.git
cd OmniRoute && npm install && npm run dev
```

> **Default ports:** Dashboard and API both run on `localhost:20128`. The API lives at `/v1`. You can split them with `PORT=20128 DASHBOARD_PORT=20129 omniroute`.

---

## First Steps in the Dashboard

Open `http://localhost:20128` after starting the server.

1. **Connect a provider.** Go to Dashboard → Providers. Connect at least one provider using OAuth or an API key.
2. **Create an API key.** Go to Dashboard → Endpoints. Generate an API key — your tools will use this to authenticate with OmniRoute.
3. **Configure your tool.** Point your AI tool's base URL to `http://localhost:20128/v1` and paste in the API key. Model names use `provider/model` format, e.g. `cc/claude-opus-4-7`.

OmniRoute also ships auto-configuration commands for common tools:

```bash
omniroute setup-claude    # Claude Code
omniroute setup-cursor    # Cursor IDE
omniroute setup-codex     # Codex CLI
omniroute setup-cline     # Cline
omniroute setup-continue  # Continue
omniroute setup-aider     # Aider
```

---

## Adding Providers

Providers are the upstream services OmniRoute routes to. They fall into three tiers:

### Subscription providers (OAuth)

| Provider | Prefix | Models | Quota |
|----------|--------|--------|-------|
| Claude Code | `cc/` | claude-opus-4-7, claude-sonnet-4-6, claude-haiku-4-5 | 5-hour + weekly |
| OpenAI Codex | `cx/` | gpt-5.5, gpt-5.4, gpt-5.3-codex | 5-hour + weekly |
| GitHub Copilot | `gh/` | gpt-5.5, claude-sonnet-4.6, gemini-3.1-pro | Monthly (1st) |

### Budget-friendly providers (API key)

| Provider | Prefix | Cost | Reset |
|----------|--------|------|-------|
| GLM-4.7 | `glm/` | $0.60/1M tokens | Daily at 10:00 AM |
| MiniMax M2.1 | `minimax/` | $0.20/1M tokens | 5-hour rolling |
| Kimi K2 | `kimi/` | $9/mo flat (10M tokens) | Monthly |

### Free providers

| Provider | Prefix | Notes |
|----------|--------|-------|
| Qoder | `if/` | 9 free models, rate-limited |
| Kiro | `kr/` | ~50 credits/month, Claude free tier |

### Adding a provider via API

```bash
curl -X POST http://localhost:20128/api/providers \
  -H "Authorization: Bearer $OMNIROUTE_MANAGE_KEY" \
  -H "Content-Type: application/json" \
  -d '{"provider": "openai", "apiKey": "sk-...", "name": "main"}'
```

---

## Creating Combos

A **combo** groups multiple models under one name with a routing strategy and fallback order. When your primary model hits a quota limit or goes down, OmniRoute automatically falls to the next model in the combo.

### Example: subscription + cheap backup

```
Combo name: premium-coding
Strategy:   priority

  1. cc/claude-opus-4-7      # primary (subscription)
  2. glm/glm-4.7             # $0.60/1M backup
  3. minimax/MiniMax-M2.7    # $0.30/1M emergency
```

### Example: zero-cost

```
Combo name: free-combo
Strategy:   priority

  1. if/kimi-k2.7-code       # free (rate-limited)
  2. kr/qwen3-coder-next     # Kiro fallback
```

### Example: always-on with five layers

```
Combo name: always-on
Strategy:   priority

  1. cc/claude-opus-4-7      # best quality
  2. cx/gpt-5.5              # secondary subscription
  3. glm/glm-4.7             # daily reset
  4. minimax/MiniMax-M2.1    # 5-hour reset
  5. if/deepseek-v4-flash    # free tier
```

Create combos visually in Dashboard → Combos, or via API:

```bash
curl -X POST http://localhost:20128/api/combos \
  -H "Authorization: Bearer $OMNIROUTE_MANAGE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "premium",
    "strategy": "priority",
    "models": [
      {"model": "cc/claude-opus-4-7"},
      {"model": "glm/glm-5.1"}
    ]
  }'
```

---

## Routing Strategies

Configured in Dashboard → Settings → Routing, or per-combo.

### Primary strategies

| Strategy | Behavior | Best for |
|----------|----------|----------|
| `fill-first` | Primary handles all traffic until unavailable | Maximizing one subscription |
| `round-robin` | Cycles through accounts (configurable sticky limit) | Spreading quota evenly |
| `p2c` | Picks 2 random accounts, routes to healthier one | Balanced load |
| `random` | Fisher-Yates shuffle per request | Even distribution |
| `least-used` | Routes to account with oldest `lastUsedAt` | Cold-start avoidance |
| `cost-optimized` | Routes to lowest-cost available provider | Budget control |

### Advanced combo strategies

| Strategy | Behavior |
|----------|----------|
| `priority` | Strict order, never round-robins — always tries #1 first |
| `weighted` | Proportional traffic by assigned weights |
| `lkgp` | Sticky to last successful model per session |
| `context-optimized` | Picks the model with the largest free context window |
| `auto` | Score-driven across all candidates |

### Session stickiness

Pass `X-Session-Id: your-session-key` in the request header to keep a session on the same provider.

### Wildcard model aliases

```
claude-sonnet-*  →  cc/claude-sonnet-4-6
gpt-*            →  gh/gpt-5.3-codex
```

---

## Auto-Routing

Send requests with `auto/*` model prefixes for zero-config intelligent routing:

| Model prefix | Optimizes for | Use case |
|-------------|---------------|----------|
| `auto` | Balanced (latency × cost × success) | General purpose |
| `auto/coding` | Coding quality | Development tasks |
| `auto/cheap` | Lowest $/token | Budget-conscious |
| `auto/fast` | Lowest latency | Real-time interaction |
| `auto/smart` | Reasoning quality | Complex analysis |
| `auto/lkgp` | Last Known Good Provider | Session consistency |
| `auto/offline` | Local-only providers | Air-gapped setups |

```bash
curl -X POST http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer $OMNIROUTE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "auto/coding",
    "messages": [{"role": "user", "content": "Refactor this function"}],
    "stream": true
  }'
```

> **Caveat:** Auto-routing does not guarantee identical behavior across models. Tool-call formats, context windows, and reasoning styles vary. For critical tasks, fix the model or constrain the candidate set.

---

## Tool Integration

### Claude Code

Edit `~/.claude/settings.json`:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:20128",
    "ANTHROPIC_AUTH_TOKEN": "your-omniroute-api-key"
  }
}
```

> **Note:** Do *not* append `/v1` to `ANTHROPIC_BASE_URL` for Claude Code.

### Cursor IDE

Settings → Models → Advanced:

```
OpenAI API Base URL: http://localhost:20128/v1
OpenAI API Key:      [from OmniRoute dashboard]
Model:               cc/claude-opus-4-7
```

### Codex CLI

```bash
export OPENAI_BASE_URL="http://localhost:20128"
export OPENAI_API_KEY="your-omniroute-api-key"
codex "your prompt"
```

### Cline / Continue / RooCode

```
Provider:  OpenAI Compatible
Base URL:  http://localhost:20128/v1
API Key:   [from OmniRoute dashboard]
Model:     cc/claude-opus-4-7
```

### MCP integration

```bash
# stdio (for Claude Desktop, Claude Code)
omniroute --mcp

# SSE endpoint (for Cursor, Continue, VS Code)
http://localhost:20128/api/mcp/sse

# Streamable HTTP
http://localhost:20128/api/mcp/stream
```

---

## Resilience & Circuit Breakers

Configured in Dashboard → Settings → Resilience.

**Request pacing** — Per-account RPM, minimum time between requests, max concurrent requests.

**Connection cooldown** — Base cooldown window after retryable failures. Supports upstream `Retry-After` and exponential backoff.

**Circuit breaker** — Four states protecting against cascading failures:

```
CLOSED (healthy)
  ↓  failures ≥ degradation threshold
DEGRADED
  ↓  failures ≥ failure threshold
OPEN (all requests blocked)
  ↓  after reset timeout
HALF_OPEN (probe traffic)
  ↓  success → CLOSED  |  failure → OPEN
```

**Cooldown wait** — When all candidates are cooling down, OmniRoute retries automatically.

**Rate-limit auto-detection** — Honors explicit upstream wait windows.

Monitor in Dashboard → Health (auto-refreshes every 10 seconds).

---

## CLI Reference

| Command | Purpose |
|---------|---------|
| `omniroute` | Start server on default port (20128) |
| `omniroute setup` | Interactive guided onboarding |
| `omniroute setup --non-interactive` | CI-friendly headless setup |
| `omniroute doctor` | Health checks without starting the server |
| `omniroute --port 3000` | Start on alternate port |
| `omniroute --mcp` | Start as MCP server (stdio) |
| `omniroute providers available` | List all supported providers |
| `omniroute providers list` | List your configured providers |
| `omniroute providers test <id>` | Live-test a provider connection |
| `omniroute combos list` | List configured combos |
| `omniroute combos switch <name>` | Set default combo |
| `omniroute models` | List available models (`--json`, `--search`) |
| `omniroute keys add\|list\|remove` | Manage API keys |
| `omniroute backup` | Snapshot config + database |
| `omniroute restore [timestamp]` | Restore from snapshot |
| `omniroute health` | Detailed health report |
| `omniroute quota` | Show provider quota usage |
| `omniroute serve --tray` | Run in system tray |
| `omniroute autostart enable` | Launch at login |

---

## Advanced Features

### Token compression (RTK + Caveman)

Compresses prompts before sending upstream, reducing token usage by 15–95%. RTK preserves semantic meaning; Caveman is more aggressive. Enable in Dashboard → Settings → Compression.

### Budget management

Set daily, weekly, or monthly spending limits per API key in Dashboard → Costs:

```bash
curl -X POST http://localhost:20128/api/usage/budget \
  -H "Content-Type: application/json" \
  -d '{"keyId": "key-123", "limit": 50.00, "period": "monthly"}'
```

### Chaining OmniRoute peers

Another OmniRoute instance can serve as a provider:

```bash
OMNIROUTE_INSTANCE_ID=gateway-a
OMNIROUTE_PEER_URLS=http://gateway-b:20128/v1
OMNIROUTE_PEER_MAX_HOPS=4
```

### Webhooks

Subscribe to events in Dashboard → Webhooks: `request.completed`, `request.failed`, `provider.unavailable`, `budget.exceeded`, `combo.switched`, `circuit_breaker.opened`, `circuit_breaker.closed`. Payloads are signed with HMAC-SHA256.

### Key environment variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `JWT_SECRET` | omniroute-default-... | JWT signing secret (change in prod) |
| `INITIAL_PASSWORD` | CHANGEME | First login password |
| `DATA_DIR` | ~/.omniroute | Database, usage logs, config |
| `PORT` | 20128 | Server port |
| `REQUIRE_API_KEY` | false | Enforce Bearer on /v1/* |
| `REQUEST_TIMEOUT_MS` | 600000 | Shared request timeout |
| `OMNIROUTE_MEMORY_MB` | 512 | Node.js heap limit |

---

## Resources

- **GitHub:** [github.com/diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **Official site:** [omniroute.online](https://www.omniroute.online/)
- **Wiki:** [GitHub Wiki](https://github.com/diegosouzapw/OmniRoute/wiki)
- **Setup Guide:** [SETUP_GUIDE.md](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/guides/SETUP_GUIDE.md)
- **User Guide:** [USER_GUIDE.md](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/guides/USER_GUIDE.md)
- **API Reference:** [API_REFERENCE.md](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/reference/API_REFERENCE.md)
