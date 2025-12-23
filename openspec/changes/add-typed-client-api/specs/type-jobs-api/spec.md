## ADDED Requirements
### Requirement: Typed jobs API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.jobs public methods and SHALL avoid **params in public signatures.

#### Scenario: Typed job filters
- **WHEN** a caller filters jobs by state in documented jobs APIs
- **THEN** the state parameter uses an explicit constrained type when authoritative values are known.
