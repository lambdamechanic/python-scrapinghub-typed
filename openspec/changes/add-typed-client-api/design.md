## Context
The documented scrapinghub client API exposes many public methods with **params and untyped returns. FastMCP requires concrete signatures and return annotations to generate tight JSON schemas. The scope is limited to modules documented in docs/client/apidocs.rst.

## Goals / Non-Goals
- Goals: replace **params with explicit, typed parameters; add precise return types and structured result models; add Literal constraints where authoritative values exist.
- Non-Goals: change runtime behavior, modify scrapinghub.legacy or scrapinghub.hubstorage internals, or fully type undocumented APIs.

## Decisions
- Use TypedDict for simple structured payloads; use dataclass/Pydantic only when necessary for validation or nested union clarity.
- Source constraints from code first, then docs. If neither is explicit, keep the field as a basic type without Literal constraints.
- Preserve backwards compatibility by routing legacy kwargs through internal helpers when needed; public signatures stay explicit and typed.

## Risks / Trade-offs
- Risk: signature changes could break callers relying on **params. Mitigation: maintain internal helpers for legacy kwargs and document replacements.
- Risk: incomplete constraints could mislead schema consumers. Mitigation: only apply Literal constraints when authoritative sources exist.

## Migration Plan
- Update public signatures incrementally by module.
- Keep behavior identical; add type shims only where needed for compatibility.

## Open Questions
- None.
