"""
Example ESBMC-AI Addon Command

This is a template for creating custom commands for the ESBMC-AI framework.
Replace 'my_addon' with your addon name and implement your command logic.
"""

from typing import cast, override
from esbmc_ai import BaseComponentConfig, ChatCommand
from esbmc_ai.chat_command import CommandResult


class MyAddonCommandConfig(BaseComponentConfig):
    """
    Configuration for your custom command.

    Add any configuration parameters your command needs here.
    These can be loaded from config.toml.

    Example:
        max_iterations: int = 10
        verbose: bool = False
    """

    pass


class MyAddonCommand(ChatCommand):
    """
    Template command for ESBMC-AI addons.

    This command demonstrates the basic structure of an ESBMC-AI addon.
    Customize the command_name, authors, and help_message, then implement
    your logic in the execute() method.
    """

    def __init__(self) -> None:
        super().__init__(
            command_name="my_addon",  # TEMPLATE: Change this to your command name
            authors="Your Name",  # TEMPLATE: Add your name
            help_message="Description of what your addon does.",  # TEMPLATE: Update help
        )
        self._config: MyAddonCommandConfig = MyAddonCommandConfig()

    @property
    @override
    def config(self) -> BaseComponentConfig:
        """Returns the command configuration."""
        return self._config

    @config.setter
    def config(self, value: BaseComponentConfig) -> None:
        """Sets the command configuration."""
        self._config = cast(MyAddonCommandConfig, value)

    @override
    def execute(self) -> CommandResult | None:
        """
        Main execution method for your command.

        This is where you implement your addon's functionality.

        Returns:
            CommandResult: Result of the command execution, or None

        Example implementation:
            print(f"Executing {self.command_name}...")
            # Your command logic here
            return CommandResult(success=True, message="Command completed")
        """
        # TEMPLATE: Implement your command logic here
        print(f"Hello from {self.command_name}!")
        return None
