"""
Example ESBMC-AI Verifier

This is a template for creating custom verifiers for the ESBMC-AI framework.
Verifiers are used to verify and validate code or verification results.
"""

from typing import override
from esbmc_ai import BaseComponentConfig
from esbmc_ai import BaseSourceVerifier
from esbmc_ai.verifier_output import VerifierOutput
from esbmc_ai.verifiers.base_source_verifier import Solution


class MyVerifierOutput(VerifierOutput):
    @property
    @override
    def successful(self) -> bool:
        # TEMPLATE: Create your verifier output class here.
        return False


class MyVerifierConfig(BaseComponentConfig):
    """
    Configuration for your custom verifier.

    Add any configuration parameters your verifier needs here.
    These can be loaded from config.toml.

    Example:
        timeout: int = 60
        verify_mode: str = "strict"
    """

    # TEMPLATE: Add your verifier configuration here.

    pass


class MyVerifier(BaseSourceVerifier):
    """
    Template verifier for ESBMC-AI addons.

    This verifier demonstrates the basic structure of an ESBMC-AI verifier.
    Customize the verifier_name and implement your verification logic.
    """

    def __init__(self) -> None:
        super().__init__(
            verifier_name="my_verifier",  # TEMPLATE: Change to your verifier name
            authors="Your Name",  # TEMPLATE: Change to your name
        )
        self._config: MyVerifierConfig = MyVerifierConfig()

    @property
    @override
    def config(self) -> BaseComponentConfig:
        """Returns the verifier configuration."""
        return self._config

    @config.setter
    def config(self, value: BaseComponentConfig) -> None:
        """Sets the verifier configuration."""
        from typing import cast

        self._config = cast(MyVerifierConfig, value)

    @override
    def verify_source(self, *, solution: Solution) -> VerifierOutput:
        """
        Main verification method.

        This is where you implement your verification logic.

        Args:
            source_code: The source code to verify

        Returns:
            dict: Verification results

        Example implementation:
            return {
                "status": "success",
                "verified": True,
                "message": "Code verification passed",
                "details": {...}
            }
        """
        # TEMPLATE: Implement your verification logic here
        print(f"Verifying code with {self.verifier_name}...")

        return MyVerifierOutput(
            return_code=1,
            output="TEMPLATE VERIFIER OUTPUT",
            issues=[],
            duration=10,
        )
