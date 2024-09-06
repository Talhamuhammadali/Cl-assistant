# AI CLI Assistant

AI CLI Assistant is an intelligent command-line tool that provides suggestions and completions for Linux, DevOps, and other essential developer commands. It uses advanced AI to understand partial commands and offer relevant completions, making your command-line experience more efficient and user-friendly.

## Features

- AI-powered command suggestions
- Interactive mode with double-tap completion
- Direct command suggestion mode
- Supports a wide range of Linux, DevOps, and development commands
- Easy to install and use
## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai_cli_assistant.git
   cd ai_cli_assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   poetry lock
   poetry install
   ```

4. Create a `.env` file in the project root and add your GROQ API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

5. Make the `ai` script executable:
   ```
   chmod +x ai
   ```

6. Add the project directory to your PATH. Add this line to your `~/.bashrc` or `~/.zshrc`:
   ```
   export PATH="/path/to/ai_cli_assistant:$PATH"
   ```
   Replace `/path/to/ai_cli_assistant` with the actual path to your project directory.

7. Reload your shell configuration:
   ```
   source ~/.bashrc  # or source ~/.zshrc if you use zsh
   ```

## Usage

You can use the AI CLI Assistant in two modes:

### Interactive Mode

1. Start the interactive mode by simply typing:
   ```
   ai
   ```
2. Enter partial commands at the prompt:
   ```
   $ kubectl
   ```
3. The assistant will display suggestions.
4. Use double-tap (quickly press Enter twice) to cycle through and complete suggestions.

### Direct Suggestion Mode

Get suggestions for a command directly by typing `ai` followed by your command:

```
ai kubectl get
```

This will immediately show suggestions for the given command.

