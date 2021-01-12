#!/usr/bin/env python3

import argparse
#from ..cracker import HCAttacks, JTRAttacks


def main():
    parser = argparse.ArgumentParser(description="Hash attack manager", prog='mattack')

    parser.add_argument('hashFile',
                            help='Hash file to crack')

    parser.add_argument('-m', '--masks',
                        help='Mask File to perform Mask Attack')

    parser.add_argument('-ht', '--type',
                        help='Hash type (john or hashcat hash type)')

    # HPC parameters
    hpc_parser = parser.add_argument_group('HPC arguments',
                                        'Options to submit a parallel task in slurm')
    hpc_parser.add_argument('-g', '--gpu', type=int, default=0,
                        help='Number of GPU nodes')

    hpc_parser.add_argument('-N', '--nodes', type=int, default=1,
                        help='Number of nodes')

    hpc_parser.add_argument('-n', '--ntasks', type=int, default=1,
                        help='Number of tasks(MPI process)')

    hpc_parser.add_argument('-p', '--partition', type=str, default=None,
                        help='Slurm Partition')

    hpc_parser.add_argument('-c', '--cpusPerTask', type=int, default=1,
                    help='Number of tasks per CPU(OMP Threads)')

    hpc_parser.add_argument('-mc', '--memPerCpu', type=str, default="4GB",
                help='Memory per CPU(node)')

    hpc_parser.add_argument('-j', '--jobname', type=str, default="maskattack",
                        help='Slurm Job Name')

    hpc_parser.add_argument('-o', '--output', type=str, default=None,
                        help='Slurm Output File Name')

    hpc_parser.add_argument('-e', '--error', type=str, default=None,
                        help='Slurm Error File Name')

    hpc_parser.add_argument('-s', '--slurm', type=str, default="mattack.slurm",
                        help='Slurm Submit Script Name')

    hpc_parser.add_argument('-t', '--time', type=str, default=None,
                        help='Maximum time to perform the attack(HH:MM:SS)')


    args = parser.parse_args()
    masksFile = args.masks
    hashType = args.format
    hashFile = args.hashFile
    mattack = MaskAttack(masksFile, hashType, hashFile)

    # parameters to perform a parallel mask attack
    gpus        = args.gpu
    nodes       = args.nodes
    ntasks      = args.ntasks
    partition   = args.partition
    cpusPerTask = args.cpusPerTask
    memPerCpu   = args.memPerCpu
    jobName     = args.jobname
    output      = args.output
    error       = args.error
    slurmScript = args.slurm
    time        = args.time

    # performing a parallel mask attack
    #mattack.run(gpus, nodes, ntasks, partition, cpusPerTask, memPerCpu,
    #           jobName, output, error, slurmScript, time)


if __name__ == "__main__":
    main()
