## ADDED Requirements
### Requirement: Typed client core API
The system SHALL provide explicit, typed parameters and return annotations for the documented public API in scrapinghub.client and SHALL avoid **params in public signatures.

#### Scenario: Generate schema from client core
- **WHEN** a schema generator inspects documented scrapinghub.client public methods
- **THEN** each method exposes explicit typed parameters and a concrete return annotation suitable for JSON schema generation.
