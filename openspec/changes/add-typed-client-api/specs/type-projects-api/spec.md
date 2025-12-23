## ADDED Requirements
### Requirement: Typed projects API
The system SHALL provide explicit, typed parameters and return annotations for documented scrapinghub.client.projects public methods, including Projects, Project, and Settings APIs, and SHALL avoid **params in public signatures.

#### Scenario: Typed project summaries
- **WHEN** a caller uses Projects.summary in the documented API
- **THEN** the input parameters are explicitly typed and the return value is a structured typed model suitable for schema generation.
