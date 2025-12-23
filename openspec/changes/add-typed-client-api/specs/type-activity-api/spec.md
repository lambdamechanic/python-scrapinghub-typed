## ADDED Requirements
### Requirement: Typed activity API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.activity public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed activity listing
- **WHEN** a caller uses documented activity APIs
- **THEN** inputs and outputs are explicitly typed and structured for schema generation.
