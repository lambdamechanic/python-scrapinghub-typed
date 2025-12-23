## ADDED Requirements
### Requirement: Typed items/logs/requests/samples APIs
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client items, logs, requests, and samples public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed job I/O access
- **WHEN** a caller uses documented items, logs, requests, or samples APIs
- **THEN** inputs and outputs are explicitly typed and structured for schema generation.
