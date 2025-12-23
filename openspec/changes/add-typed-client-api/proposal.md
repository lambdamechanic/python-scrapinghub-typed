# Change: Add tight typings for documented client API

## Why
The documented scrapinghub client API relies on **params and untyped returns, which prevents schema generation from signatures. Tight, explicit typing is required for FastMCP to produce accurate JSON schemas.

## What Changes
- Replace **params in documented scrapinghub.client.* methods with explicit, typed parameters or typed model inputs.
- Add precise return annotations and structured result models (TypedDict preferred, dataclass/Pydantic when needed).
- Introduce Literal constraints for known enum-like fields based on code and docs.
- Keep backwards compatibility via internal helpers when needed (public signatures remain explicit).

## Impact
- Affected specs: type-client-core, type-projects-api, type-jobs-api, type-spiders-api, type-collections-api, type-frontiers-api, type-activity-api, type-io-apis.
- Affected code: scrapinghub/client/*.py (documented modules only).
- Users: no behavior changes expected; typing and schema precision improve for documented API.
