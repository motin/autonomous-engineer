# The Gen AI Engineer

An experiment to see how well a LLM-powered assistant is able to perform tasks of a software engineer:

1. **Design Software:** Develop plans for creating software applications and systems, specifying which programming languages, algorithms, and data structures to use.
2. **Write Code:** Write and implement efficient code in various computer languages, capable of working individually or as part of a team, depending on the project's size and complexity.
3. **Test Software:** Test the software for bugs, issues, and usability, performing both automated and manual testing.
4. **Debug:** After testing, identify and fix issues found during testing.
5. **Maintain Software:** After the software is released, update it, improve its performance, and make any necessary changes.
6. **Document:** Write documentation for the software code, explaining how the software works. This documentation is often used for user manuals and guides.
7. **Problem-Solve:** Understand complex systems and solve problems on a day-to-day basis.
8. **Collaborate:** Work with other professionals like business analysts, project managers, and testers, to achieve a common goal.
9. **Understand User Needs:** Understand the requirements of the end-user, and design software that meets these needs.

## Overview

This repository will contain:

* `assistant` - Rasa-boilerplate and configuration for the assistant
* `prompts` - A set of prompts and chains used with LLMs to perform the above tasks
* `abilities` - Actuators/tools that the Gen AI Engineer needs to interact with its environment
* `chat` - A chat interface with which the human can interact with the assistant
* `docs` - Instructions on how to configure, extend and monitor the assistant regarding performance and costs

The assistant runs locally and interacts with existing engineering tooling.