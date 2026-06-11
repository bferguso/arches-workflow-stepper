# arches-workflow-components

A collection of reusable Vue components and composables for building guided Arches workflows using PrimeVue's Stepper component, `arches-vue-components`, and `arches-querysets`.

## Overview

`arches-workflow-components` provides a foundation for implementing multi-step workflows within Arches applications. It combines the presentation capabilities of PrimeVue Stepper with Arches-specific components and query abstractions to accelerate the development of data-entry and review experiences.

## Features

- Reusable workflow and step components
- Built on PrimeVue Stepper for guided navigation
- Integration with `arches-vue-components`
- Support for `arches-querysets` data retrieval and persistence
- Shared composables for workflow state management
- Validation hooks between workflow steps
- Framework for creating graph-specific workflows

## Installation

```bash
npm install arches-workflow-components
```

## Example Use Cases

- Resource creation workflows
- Resource editing wizards
- Guided review and approval processes
- Multi-step survey experiences
- Graph-specific data collection interfaces

## Design Goals

- Encourage consistency across workflows
- Minimize boilerplate code
- Promote composability and reuse
- Remain flexible enough for project-specific requirements

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).
