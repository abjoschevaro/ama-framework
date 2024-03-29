#!/usr/bin/env python3
#
# wordlist attack using john
#
# date: Feb 22 2021
# Maintainer: glozanoa <glozanoa@uni.pe>

import os
from typing import Any

from ama.core.files import Path

# base  imports
from ama.core.modules.base import (
    Attack,
    Argument
)
from ama.core.modules.base.auxiliary import Auxiliary

# cracker imports
from ama.core.plugins.cracker import John

# slurm import
from ama.core.slurm import Slurm

#fineprint status
from fineprint.status import (
    print_failure,
    print_status
)

# pre attack import
## auxiliary/hashes
from ama.core.modules.auxiliary.hashes import (
    HashID,
    Nth
)
## auxiliary/wordlist
from ama.core.modules.auxiliary.wordlists import (
    CuppInteractive
)

# post attack import
## auxiliary/hashes
from ama.core.modules.auxiliary.hashes import (
    HashesStatus
)

class JohnWordlist(Attack):
    """
    Wordlist Attack using john cracker
    """

    DESCRIPTION = "Wordlist attack using John The Ripper"
    MNAME = "attack/hashes/john_wordlist"
    MTYPE, MSUBTYPE, NAME = MNAME.split("/")
    AUTHOR = [
        "glozanoa <glozanoa@uni.pe>"
    ]
    FULLDESCRIPTION = (
        """
        Perform wordlists attacks against hashes
        with john submiting parallel tasks in a cluster using Slurm
        """
    )

    REFERENCES = [
        "https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1/",
        "https://www.hackingarticles.in/beginners-guide-for-john-the-ripper-part-2/",
        "https://github.com/openwall/john"
    ]

    CRACKER = John.MAINNAME
    # {PRE_ATTACK_MNAME: PRE_ATTACK_CLASS, ...}
    PRE_ATTACKS = {
        # auxiliary/hashes
        f"{Nth.MNAME}": Nth,
        f"{HashID.MNAME}": HashID,

        ## auxiliary/wordlist
        f"{CuppInteractive.MNAME}": CuppInteractive
    }

    # {POST_ATTACK_MNAME: POST_ATTACK_CLASS, ...}
    POST_ATTACKS = {
        # auxiliary/hashes
        f"{HashesStatus.MNAME}": HashesStatus,
    }

    def __init__(self, *,
                 hash_type: str = None, hashes_file: str = None,
                 wordlist: str = None, slurm: Slurm=None,
                 pre_attack: Auxiliary = None, post_attack: Auxiliary = None):
        """
        Initialization of John  wordlist attack

        Args:
        hashType (str): Jonh's hash type
        hashesFile (str): Hashes file to attack
        wordlist (str): wordlist to attack
        slurm (Slurm): Instance of Slurm class

        pre_attack (Auxiliary): Instance of a pre attack (auxiliary module)
        post_attack (Auxiliary): Instance of a post attack (auxiliary module)
        """

        attack_options = {
            'wordlist': Argument(wordlist, True, "wordlists file(split by commas)"),
            'hash_type': Argument(hash_type, True, "John hash types (split by commas)"),
            'hashes_file': Argument(hashes_file, True, "hashes file"),
        }

        if slurm is None:
            slurm_options = {
                "account": Argument(None, False, "Cluster account to submit the job"),
                "array": Argument(None, False, "Number of array jobs"),
                "dependency": Argument(None, False, "Defer the start of this job until the specified dependencies have been satisfied completed"),
                "chdir" : Argument(os.getcwd(), True, "Working directory path"),
                "error": Argument(None, False, "Error file"),
                "job_name" : Argument('attack', False, "Name for the job allocation"),
                "cluster" : Argument(None, False, "Cluster Name"),
                "distribution": Argument('block', True, "Distribution methods for remote processes (<block|cyclic|plane|arbitrary>)"),
                "mail_type": Argument(None, False, "Event types to notify user by email(<BEGIN|END|FAIL|REQUEUE|ALL|TIME_LIMIT_PP>)"),
                "mail_user": Argument(None, False, "User email"),
                "mem": Argument(None, False, "Memory per node (<size[units]>)"),
                "mem_per_cpu": Argument(None, False, "Minimum memory required per allocated CPU (<size[units]>)"),
                "cpus_per_task": Argument(1, True, "Number of processors per task"),
                "nodes": Argument(1, True, "Number of nodes(<minnodes[-maxnodes]>)"),
                "ntasks": Argument(1, True, "Number of tasks"),
                "nice": Argument(None, False, "Run the job with an adjusted scheduling"),
                "output": Argument('slurm-%j.out', True, "Output file name"),
                "open_mode": Argument('truncate', True, "Output open mode (<append|truncate>)"),
                "partition": Argument(None, True, "Partition to submit job"),
                "reservation": Argument(None, False, "Resource reservation name"),
                "time": Argument(None, False, "Limit of time (format: DD-HH:MM:SS)"),
                "test_only": Argument(False, True, "Validate the batch script and return an estimate of when a job would be scheduled to run. No job is actually submitted"),
                "verbose": Argument(False, True, "Increase the verbosity of sbatch's informational messages"),
                "nodelist": Argument(None, False, "Nodelist"),
                "wait": Argument(False, True, "Do not exit until the submitted job terminates"),
                "exclude": Argument(None, False, "Do not exit until the submitted job terminates"),
                'batch_script': Argument('attack.sh', True, "Name for the generated batch script"),
                'pmix': Argument('pmix_v3', True, "MPI type")
            }

            slurm = Slurm(**slurm_options)

        init_options = {
            'mname' : JohnWordlist.MNAME,
            'author': JohnWordlist.AUTHOR,
            'description': JohnWordlist.DESCRIPTION,
            'fulldescription':  JohnWordlist.FULLDESCRIPTION,
            'references': JohnWordlist.REFERENCES,
            'pre_attack': pre_attack,
            'attack_options': attack_options,
            'post_attack': post_attack,
            'slurm': slurm
        }

        super().__init__(**init_options)

    # def get_init_options(self):
    #     init_options = {
    #         "hash_type": self.options['hash_type'].value,
    #         "hashes_file": self.options['hashes_file'].value,
    #         "wordlist": self.options['wordlist'].value,
    #         "slurm": self.slurm,
    #         "pre_attack": self.selected_pre_attack,
    #         "post_attack": self.selected_post_attack
    #     }
    #    return init_options

    def attack(self, *,
               local:bool = False, pre_attack_output: Any = None,
               db_status:bool = False, workspace:str = None, db_credential_file: Path = None,
               cracker_main_exec:Path = None, slurm_conf = None):
        """
        Wordlist attack using John the Ripper

        Args:
           local (bool): if local is True run attack localy otherwise
                         submiting parallel tasks in a cluster using slurm
        """

        #import pdb; pdb.set_trace()
        try:
            self.no_empty_required_options(local)

            if slurm_conf:
                self.slurm.config = slurm_conf

            if cracker_main_exec:
                jtr = John(john_exec=cracker_main_exec)
            else:
                jtr = John()

            hash_types = self.options['hash_type'].value.split(',')
            wordlists = self.options['wordlist'].value.split(',')

            jtr.wordlist_attack(hash_types = hash_types,
                                hashes_file = self.options['hashes_file'].value,
                                wordlists = wordlists,
                                slurm = self.slurm,
                                local = local,
                                db_status= db_status,
                                workspace= workspace,
                                db_credential_file=db_credential_file)

        except Exception as error:
            print_failure(error)


    def setv(self, option, value, *, pre_attack: bool = False, post_attack: bool = False):
        #import pdb; pdb.set_trace()
        super().setv(option, value, pre_attack = pre_attack, post_attack = post_attack)

        option = option.lower()
        # attack ->  atack
        if option == "array":
            super().setv('output', 'slurm-%A_%a.out', pre_attack=False, post_attack=False)
