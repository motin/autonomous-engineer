# Autonomous Engineer

An experiment to see how well a LLM-powered assistant is able to support software engineers in their day-to-day work.

The assistant is designed for interactive pair programming with a human, but the long term goal is for ti to be able to work autonomously as a productive member of a software engineering team.

## What makes this different from other Open Source AI-related projects?

* **No over-promising and under-delivering**
  * This is not a framework or platform that promises to solve all (or any if) the problems of a software engineer.
  * If anything, Autonomous Engineer promises to be clear about what it is and what it can and cannot do, so that you can make an informed decision about whether it's worth your time to use and contribute to it.
* **Built upon emerging standards of the LLM ecosystem**
  * Many other projects started before the LLM ecosystem was mature enough to support them, resulting in a lot of code that is now better served by the ecosystem.
  * Autonomous Engineer is built upon the emerging standards of the LLM ecosystem, so that it can be easily extended and maintained.
* **Full control over the assistant**
  * Autonomous Engineer is fully open source and runs locally by default, so that you have full control over your data.
  * Commands that run on your machine are executed in a shared tmux session, so that you can see what the assistant is doing at all times (and even hit Ctrl-C to stop it if you want to).
* **Honest and pragmatic division of labor between the human and the assistant**
  * There is no AGI today, and while LLMs are very capable, they are also associated with latency, monetary costs and require a lot of context to do a good job.
  * Autonomous Engineer is designed to be useful in the real world, providing real value, while also being mindful of the limitations and costs of LLMs.
  * This is achieved by having the assistant focus on the tasks that it can do well, and leaving the rest to the human.

## Current status

Currently, Autonomous Engineer doesn't do much. It's an early work in progress. There is only one engineer ([@motin](https://github.com/motin)) working part-time on the project. There is no docs, no website, no stars, no discord, no community and hopefully no hybris.

The goal is to eventually be able to perform all the tasks listed under "What does a software engineer do?" below for a variety of software engineering projects, but right now it can't do much more than run a few commands and respond to a few prompts.

This readme gets updated as the project progresses to reflect the current state of the project.

## Short-term Roadmap

* [x] Project boilerplate to run an assistant locally
* [x] Be able to chat with the assistant via a chat interface
* [ ] Connect an LLM so that the assistant can understand and respond to natural language
* [ ] Set up token/cost monitoring to always stay on top of the assistant's costs
* [ ] Give the assistant a set of primitive abilities necessary to run commands and understand the effects of those commands
  * [ ] Ability to understand the current state of the project (a new/existing project, the project's goals, requirements, architecture, dependencies, tests, etc)
  * [ ] Ability to run commands on the local machine (e.g. `ls`, `git status`) via a shared tmux session (for control)
  * [ ] Ability to interpret the results of commands that it or the user runs (e.g. `git status` -> "You have 3 uncommitted changes")
  * [ ] Ability to see and contextualize the source code of the current project (e.g. find the path to the current project's `package.json` file, or to a specific file mentioned in a stack trace)
* [ ] Give the assistant a set of abilities necessary to contribute to a software engineering project
  * [ ] Ability to modify the source code of the project
  * [ ] Ability to run tests and interpret the results
  * [ ] Ability to commit and push changes to the project's git repository
  * [ ] Ability to create and merge pull requests
* [ ] Try out the assistant on various real projects and see what it can and cannot do when faced with real-world scenarios
* [ ] Give the assistant more advanced and better performing abilities as necessary to be a productive member of a software engineering team

## Overview

This repository contains:

* `chatbot` - Rasa-boilerplate and configuration for the assistant's chat ability
* `abilities` - Actuators/tools that the assistant needs to interact with its environment
* `ui` - A hybrid traditional ui & chat interface with which the human can interact with and pair program with the assistant

This repository will contain:

* `prompts` - A set of prompts and chains used with LLMs to perform the above tasks
* `docs` - Instructions on how to configure, extend and monitor the assistant

The assistant runs locally and interacts with existing engineering tooling.

## Getting started

_Note:_ The assistant is being developed using macOS. It may work on other Linux/Unix systems, but it has not been tested.

### Prerequisites

Make sure these are installed and available in your `$PATH`:

* Python 3.9
* [poetry](https://python-poetry.org/docs/#installation)
* [tmux](https://github.com/tmux/tmux/wiki/Installing)
* [ttyd](https://github.com/tsl0922/ttyd)
* [Node.js](https://nodejs.org/en/download/)
* [yarn](https://classic.yarnpkg.com/en/docs/install/)

Install dependencies:

```shell
poetry install
```

## Launching the assistant

```shell
npx mprocs
```

http://localhost:1337 opens up with a UI for pair programming with the assistant (a chat interface and a terminal that both you and the assistant have access to).

To use iTerm2 instead of the browser-based terminal, run:

```shell
tmux -CC attach -t autonomous-engineer
```

Source: https://iterm2.com/documentation-tmux-integration.html

## What does a software engineer do?

To clarify what the Autonomous Engineer is aiming to do, here's a list of tasks that a software engineer might perform on a day-to-day basis:

1. **Design Software:** Develop plans for creating software applications and systems, specifying which programming languages, algorithms, and data structures to use.
2. **Write Code:** Write and implement efficient code in various computer languages, capable of working individually or as part of a team, depending on the project's size and complexity.
3. **Test Software:** Test the software for bugs, issues, and usability, performing both automated and manual testing.
4. **Debug:** After testing, identify and fix issues found during testing.
5. **Maintain Software:** After the software is released, update it, improve its performance, and make any necessary changes.
6. **Document:** Write documentation for the software code, explaining how the software works. This documentation is often used for user manuals and guides.
7. **Problem-Solve:** Understand complex systems and solve problems on a day-to-day basis.
8. **Collaborate:** Work with other professionals like business analysts, project managers, and testers, to achieve a common goal.
9. **Understand User Needs:** Understand the requirements of the end-user, and design software that meets these needs.
