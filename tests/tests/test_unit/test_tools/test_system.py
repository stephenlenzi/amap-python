import random
import os


import amap.tools.system as system


def write_n_random_files(n, dir, min_size=32, max_size=2048):
    sizes = random.sample(range(min_size, max_size), n)
    for size in sizes:
        with open(os.path.join(dir, str(size)), "wb") as fout:
            fout.write(os.urandom(size))


def write_file_single_size(directory, file_size):
    with open(os.path.join(directory, str(file_size)), "wb") as fout:
        fout.write(os.urandom(file_size))


def check_get_num_processes():
    assert len(os.sched_getaffinity(0)) == system.get_num_processes()


def check_max_processes():
    max_proc = 5
    correct_n = min(len(os.sched_getaffinity(0)), max_proc)
    assert correct_n == system.get_num_processes(n_max_processes=max_proc)
