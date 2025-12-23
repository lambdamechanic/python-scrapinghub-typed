## ADDED Requirements
### Requirement: Typed spiders API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.spiders public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed spider retrieval
- **WHEN** a caller uses documented spider methods (get, list, iter)
- **THEN** the inputs and outputs are explicitly typed for schema generation.
