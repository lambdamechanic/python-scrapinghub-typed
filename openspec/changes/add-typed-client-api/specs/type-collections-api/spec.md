## ADDED Requirements
### Requirement: Typed collections API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.collections public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed collection access
- **WHEN** a caller uses documented collections APIs
- **THEN** inputs and outputs are explicitly typed and structured for schema generation.
