# Product glossary

Where the exact expansion was not explicitly provided, I’m keeping the abbreviation rather than inventing one.

| Name / Abbreviation                    | Meaning / Context                                                                                                                               |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **VoC / VOC**                          | Voice of Customer. Survey creation, targeting, responses, builder, campaigns/surveys, Email Digest, Export API, multilingual surveys, etc.      |
| **VoS / VOS**                          | Voice of the Silent. Session/survey-related analytics, similarity reasoning, Qualtrics processing, Spark jobs.                                  |
| **AJM**                                | Journey-related module (Journey Map / Page Journey). Deals with journey graphs, flows, steps, page groups, processing and drilldowns.           |
| **Anomalies / Anomaly Detection**      | Anomaly detection functionality, including anomaly widgets, sleeves, significance scores, drilldowns and Anodot integration.                    |
| **Anodot**                             | External/alternative anomaly detection engine being introduced to replace or complement the legacy Glassbox anomaly engine.                     |
| **Alerts**                             | Alert creation, configuration, widgets, notifications, email templates, thresholds and anomaly-based alerts.                                    |
| **TM**                                 | Tenant Management. Tenant configuration, licensing, quotas, retention, SSO and related administration.                                          |
| **UGM**                                | User and Group Management. Users, groups, roles, permissions and SSO-related user management.                                                   |
| **Session Replay / Recorded Sessions** | Session playback and session-level analysis, including VoC/VoS data and drilldowns.                                                             |
| **User Timeline**                      | User/session timeline functionality and related drilldowns.                                                                                     |
| **Self-Service**                       | Integration configuration functionality, including APM and GB-to-Splunk integrations.                                                           |
| **GB-to-Splunk**                       | Integration for sending/connecting Glassbox data with Splunk.                                                                                   |
| **APM**                                | Application Performance Monitoring integrations, including Splunk, Dynatrace, AppDynamics and New Relic.                                        |
| **GIA**                                | AI/insights functionality used particularly with VoC responses and session similarity/reasoning. Exact expansion was not stated in the reports. |
| **Clara**                              | Service/component involved in Alerts/Anomalies processing and queries, with Elasticsearch/Postgres stability considerations.                    |
| **Clingine**                           | Backend/service involved in configuration and processing, including VoC cooldown and Self-Service proxy functionality.                          |
| **clister-node**                       | Node-based backend service used particularly for Tenant Management, authentication/authorization, static assets and configuration.              |
| **glassvox.js**                        | Client-side VoC JavaScript component responsible for survey behavior, triggering, rendering, preview/debugging, etc.                            |
| **glassvox-api**                       | VoC backend API service. Has undergone Spring Boot and Spring Data/JPA modernization.                                                           |
| **glassvox-processor**                 | VoC processing backend, including mobile/web response processing and data flows.                                                                |
| **glassvox-integration-processor**     | VoC integration-processing service, including integration and automated test work.                                                              |
| **WebUI / webui**                      | Main frontend/web application layer.                                                                                                            |
| **WebUI Tools / webuitools**           | Internal/admin configuration tooling.                                                                                                           |
| **FE**                                 | Frontend.                                                                                                                                       |
| **BE**                                 | Backend.                                                                                                                                        |
| **QA**                                 | Quality Assurance/testing.                                                                                                                      |
| **UI**                                 | User Interface.                                                                                                                                 |
| **API**                                | Application Programming Interface.                                                                                                              |
| **E2E**                                | End-to-end testing.                                                                                                                             |
| **KT**                                 | Knowledge Transfer / handover.                                                                                                                  |
| **CS**                                 | Customer Support issue/ticket in the sprint-report context.                                                                                     |
| **FR**                                 | Feature Request in ticket naming/context.                                                                                                       |
| **CF**                                 | Code Freeze, based on references such as fixes found/delivered around CF.                                                                       |
| **MT**                                 | Multi-Tenant / multi-tenancy context.                                                                                                           |
| **CX-BI**                              | Product/solution context used mainly around Alerts and MT environments; exact expansion was not provided.                                       |
| **PG**                                 | PostgreSQL in infrastructure/database contexts.                                                                                                 |
| **CH**                                 | ClickHouse.                                                                                                                                     |
| **JPA**                                | Java Persistence API, used in the glassvox-api persistence migration.                                                                           |
| **SSO**                                | Single Sign-On.                                                                                                                                 |
| **SMTP**                               | Email transport used by VoC Email Digest.                                                                                                       |
| **RTL**                                | Right-to-left language/layout support.                                                                                                          |
| **SPA**                                | Single Page Application.                                                                                                                        |
| **NPS**                                | Net Promoter Score.                                                                                                                             |
| **CSAT**                               | Customer Satisfaction score.                                                                                                                    |
| **DAG / Airflow**                      | Data pipeline orchestration, particularly around VoS/Spark processing.                                                                          |
| **Spark**                              | Data-processing jobs used in VoS and similarity-related flows.                                                                                  |
| **Cassandra**                          | Database used for session/journey/VoC-related data.                                                                                             |
| **Elasticsearch / OpenSearch**         | Search/data infrastructure used by several backend flows, including Clara.                                                                      |
| **Playwright / Cypress**               | UI automation frameworks. The team has been progressively migrating tests from Cypress to Playwright.                                           |
| **CodeAgent**                          | Used for several bug-fix activities in later sprints; appears to refer to an AI/code-assisted bug-fixing workflow.                              |
| **Guardians**                          | The squad covered by these sprint reports.                                                                                                      |
| **Goonies**                            | Another squad, appearing mainly in cross-squad knowledge transfers such as VoS/Spark handover.                                                  |

A useful high-level grouping for future sprint summaries is: **[VoC] [VoS] [AJM] [Anomalies] [Alerts] [TM] [UGM] [Session Replay] [Self-Service/Integrations] [Tech] [QA]**.
