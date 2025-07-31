---
triggers:
- cursorrule
---

# Cursor Rules Generator

This microagent generates a comprehensive .cursorrules file for this project to help with AI-assisted development.

## Task

Write a .cursorrules file that provides context and guidelines for AI assistants working on this Second Brain microagents repository.

## .cursorrules Content

The .cursorrules file should include:

1. **Project Overview**: Description of the Second Brain microagents repository
2. **Repository Structure**: Explanation of the file organization
3. **Microagent Format**: Guidelines for creating new microagents
4. **Development Guidelines**: Best practices for working with this repository
5. **File Naming Conventions**: Standards for naming files and directories
6. **Documentation Requirements**: What should be documented and how

## Implementation

When triggered, this microagent will:
1. Analyze the current repository structure
2. Generate appropriate .cursorrules content based on the project's needs
3. Write the content to the .cursorrules file in the root directory
4. Ensure the rules are comprehensive and helpful for AI-assisted development

## Example .cursorrules Structure

```
# Second Brain - OpenHands Microagents Repository

This repository contains microagents for OpenHands AI assistant.

## Project Structure
- `.openhands/microagents/` - Contains all microagent definitions
- Root directory - Contains symbolic links and main documentation

## Microagent Guidelines
- Each microagent should be a markdown file with YAML frontmatter
- Include triggers in the frontmatter
- Provide clear documentation and examples
- Follow consistent naming conventions

## Development Best Practices
- Keep microagents focused and single-purpose
- Update README.md when adding new microagents
- Use descriptive file names
- Include proper documentation
```