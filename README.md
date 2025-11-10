# ESBMC-AI Addon Template

This is a template repository for creating ESBMC-AI addons. Use this as a starting point for building custom commands and verifiers for the ESBMC-AI framework.

## What is ESBMC-AI?

ESBMC-AI is an AI-powered framework for program verification and analysis. It provides an extensible platform for creating custom commands, verifiers, and tools that leverage LLMs for code analysis, verification, and repair.

## Getting Started

### 1. Use This Template

Click the "Use this template" button on GitHub to create a new repository from this template, or clone it directly:

```bash
git clone https://github.com/esbmc/esbmc-ai-addon-template.git my-addon
cd my-addon
```

### 2. Search and Replace Template Markers

Throughout this template, you'll find comments and fields marked with `TEMPLATE:`. These indicate places where you need to customize the code for your addon. Use your editor's search function to find all instances of "TEMPLATE" and update them.

**Key files to update:**
- `pyproject.toml` - Project metadata, dependencies, and URLs
- `config.toml` - Addon module configuration
- `my_addon/__about__.py` - Version and author information
- `my_addon/__init__.py` - Package exports
- `my_addon/commands/__init__.py` - Command exports
- `my_addon/commands/my_addon.py` - Main command implementation
- `my_addon/verifiers/__init__.py` - Verifier exports (if applicable)
- `my_addon/verifiers/my_verifier.py` - Verifier implementation (if applicable)

### 3. Rename Your Module

The template uses `my_addon` as the default module name. Rename it to match your addon:

```bash
# Rename the module directory
mv my_addon your_addon_name

# Update all imports and references in the files listed above
# Search for "my_addon" and replace with "your_addon_name"
```

**Don't forget to update:**
- Module imports in Python files
- `pyproject.toml` - `name`, `[tool.hatch.version]`, and `[tool.hatch.build]` sections
- `config.toml` - `addon_modules` list

### 4. Implement Your Addon

#### Commands

Commands are the main way users interact with your addon. Implement your command logic in `my_addon/commands/my_addon.py`:

```python
class MyAddonCommand(ChatCommand):
    def execute(self) -> CommandResult | None:
        # Your implementation here
        pass
```

See the template file for detailed examples and documentation.

#### Verifiers (Optional)

If your addon needs custom verification logic, implement it in `my_addon/verifiers/my_verifier.py`:

```python
class MyVerifier(Verifier):
    def verify(self, source_code: str) -> dict:
        # Your verification logic here
        pass
```

### 5. Update Dependencies

Edit `pyproject.toml` to add any dependencies your addon needs:

```toml
dependencies = [
    "esbmc-ai>=0.6.0",  # Uncomment when ready
    "your-dependency",
]
```

### 6. Set Up Development Environment

This project uses Hatch for project management:

```bash
# Create and activate development environment
hatch shell

# Run tests (once you've added them)
hatch test

# Build the package
hatch build

# Run linter
pylint my_addon
```

**Environment Variables:**
- `ESBMCAI_CONFIG_FILE` - Path to config file (defaults to `./config.toml`)
- `ESBMCAI_EDITABLE` - Set to `true` to install esbmc-ai in editable mode from `../esbmc-ai`
- `CPU_ONLY` - Set to `true` to install CPU-only PyTorch version

## Project Structure

```
.
├── my_addon/                  # Main package directory
│   ├── __init__.py           # Package exports
│   ├── __about__.py          # Version and metadata
│   ├── commands/             # Command implementations
│   │   ├── __init__.py
│   │   └── my_addon.py       # Main command class
│   └── verifiers/            # Verifier implementations (optional)
│       ├── __init__.py
│       └── my_verifier.py    # Example verifier
├── tests/                    # Test files (add your own)
├── config.toml               # ESBMC-AI configuration
├── pyproject.toml            # Project metadata and dependencies
├── LICENSE                   # License file
├── CLA.md                    # Contributor License Agreement
└── README.md                 # This file
```

## Configuration

### config.toml

This file configures ESBMC-AI to load your addon:

```toml
dev_mode = true
addon_modules = ["my_addon"]  # Replace with your module name
```

You can also add custom configuration for your addon:

```toml
[my_addon]
max_iterations = 10
verbose = true
```

Access these settings in your code through the `config` property of your command or verifier.

## Testing

Add tests in the `tests/` directory and run them with:

```bash
hatch test

# With coverage
hatch test --cover
```

## Template Marker Convention

All template fields are marked with `TEMPLATE:` comments. To customize this template:

1. Search for "TEMPLATE" in your editor
2. Update each marked field according to the instructions
3. Remove or update the TEMPLATE comments once customized

Example:
```python
# Before:
command_name="my_addon",  # TEMPLATE: Change this to your command name

# After customization:
command_name="code_analyzer",  # Analyzes code for security issues
```

## Building and Publishing

### Build the Package

```bash
hatch build
```

This creates distribution files in the `dist/` directory.

### Check Before Publishing

```bash
twine check dist/*
```

### Publish to PyPI

```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

## Examples

### Example Command

See `my_addon/commands/my_addon.py` for a complete command template with documentation.

### Example Verifier

See `my_addon/verifiers/my_verifier.py` for a complete verifier template with documentation.

## Contributing

If you want to contribute to this template:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See `CLA.md` for contributor license agreement details.

## Resources

- [ESBMC-AI Documentation](https://github.com/esbmc/esbmc-ai/wiki)
- [ESBMC-AI Repository](https://github.com/esbmc/esbmc-ai)
- [Hatch Documentation](https://hatch.pypa.io/)

## License

See `LICENSE` file for details.

## Support

For questions or issues:
- Open an issue in your addon's repository
- Refer to [ESBMC-AI documentation](https://github.com/esbmc/esbmc-ai/wiki)
- Check [ESBMC-AI issues](https://github.com/esbmc/esbmc-ai/issues)
