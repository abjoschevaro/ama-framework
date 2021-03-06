#!/usr/bin/env python3
#
# Cupp - interactive mode
#
# date: Mar 3 2021
# Maintainer: glozanoa <glozanoa@uni.pe>

from fineprint.status import print_failure

# Cupp plugin
from ama.core.plugins.auxiliary import Cupp

# Auxliary base class
from ama.core.modules.base import Auxiliary

# debugged - date: Mar 4 2021
class CuppInteractive(Auxiliary):
    """
    Cupp - interactive mode
    """
    DESCRIPTION = "Cupp - interactive mode"
    MNAME = "auxiliary/wordlists/cupp_interactive"
    MTYPE, MSUBTYPE, NAME = MNAME.split("/")
    AUTHOR = [
        "glozanoa <glozanoa@uni.pe>"
    ]
    FULLDESCRIPTION = (
        """
        Interactive questions for user password profiling
        """
    )

    REFERENCES = [
        "https://www.hackingarticles.in/comprehensive-guide-on-cupp-a-wordlist-generating-tool/",
        "https://github.com/Mebus/cupp"
    ]

    def __init__(self):
        """
        Initialization of Cupp - interactive mode
        """

        auxiliary_options = {}
        init_options = {
            'mname': CuppInteractive.MNAME,
            'author': CuppInteractive.AUTHOR,
            'description': CuppInteractive.DESCRIPTION,
            'fulldescription': CuppInteractive.FULLDESCRIPTION,
            'references': CuppInteractive.REFERENCES,
            'auxiliary_options': auxiliary_options,
            'slurm': None
        }

        super().__init__(**init_options)

    def run(self):
        """
        Execution of Cupp interactive mode
        """

        try:
            self.no_empty_required_options()
            cupp = Cupp()
            cupp.interactive()

        except Exception as error:
            print_failure(error)