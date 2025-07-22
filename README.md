# Second Brain - OpenHands Microagents

This repository contains microagents for OpenHands AI assistant.

## Available Microagents

### Tell Me a Joke
- **File**: `.openhands/microagents/tell-me-a-joke.md`
- **Description**: Tells a random joke when triggered
- **Trigger**: `tell-me-a-joke`

### Funny Story
- **File**: `.openhands/microagents/funny-story.md`
- **Description**: Tells a funny story when triggered
- **Trigger**: `funny-story`

## How to Use

To use a microagent, simply use its trigger phrase when talking to OpenHands.

Examples:
```
tell-me-a-joke
funny-story
```

## Adding New Microagents

1. Create a new markdown file in the `.openhands/microagents` directory
2. Include appropriate documentation and content in the markdown file
3. Create a symbolic link in the root directory if needed
4. Update this README with information about the new microagent

## Repository Structure

```
.
├── .openhands/
│   └── microagents/
│       ├── tell-me-a-joke.md
│       └── funny-story.md
├── README.md
├── tell-me-a-joke -> .openhands/microagents/tell-me-a-joke.md
└── funny-story -> .openhands/microagents/funny-story.md
```