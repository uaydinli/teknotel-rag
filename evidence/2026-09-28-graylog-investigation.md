# Graylog Investigation — Evidence Log

Date: 2026-09-28
Status: discovery in progress

## Scope
Read-only MongoDB discovery was prepared for the Graylog database.

## Requested evidence sets
- streamrules
- pipeline_processor_pipelines
- pipeline_processor_pipelines_streams
- pipeline_processor_rules
- index_sets
- index_ranges

## Evidence status
The discovery command was prepared, but the resulting MongoDB output is not available in the current message context. Therefore no specific stream ID, pipeline name, rule condition, index-set value, retention value, or active index range is asserted here.

## Next evidence requirement
When the MongoDB command output is obtained, preserve the raw output or an appropriately redacted copy and add a structured interpretation distinguishing observed facts from inference.