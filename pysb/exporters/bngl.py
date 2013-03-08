"""
Module containing a class for exporting a PySB model to BNGL.

Serves as a wrapper around :py:class:`pysb.generator.bng.BngGenerator`.

For information on how to use the model exporters, see the documentation
for :py:mod:`pysb.export`.
"""

from pysb.generator.bng import BngGenerator
from pysb.export import Export

class ExportBngl(Export):
    """A class for returning the BNGL for a given PySB model.

    Inherits from :py:class:`pysb.export.Export`, which implements
    basic functionality for all exporters.
    """

    def export(self):
        """Generate the corresponding BNGL for the PySB model associated
        with the exporter. A wrapper around ``pysb.generator.bng.BngGenerator``.

        Returns
        -------
        string
            The BNGL output for the model.
        """
        gen = BngGenerator(self.model)
        return gen.get_content()
