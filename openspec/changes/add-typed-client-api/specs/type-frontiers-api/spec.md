## ADDED Requirements
### Requirement: Typed frontiers API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.frontiers public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed frontier queries
- **WHEN** a caller uses documented frontiers APIs
- **THEN** inputs and outputs are explicitly typed and structured for schema generation.
