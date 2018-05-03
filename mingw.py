#!/bin/env python3
from cross_definitions import CrossDefinitions


# Base definitions for MinGW
def mingw_base(bitsize):
    if bitsize == 32:
        cpu = 'i686'
        mingw = 'mingw32'
        prefix = 'i686-w64-mingw32'
    if bitsize == 64:
        cpu = 'x86_64'
        mingw = 'mingw64'
        prefix = 'x86_64-w64-mingw64'

    return CrossDefinitions(
        'mingw/' + mingw + '_base',
        'Base for MinGW builds with prefix ' + prefix,
        binaries={
            'c':          prefix + '-gcc',
            'cpp':        prefix + '-g++',
            'ar':         prefix + '-ar',
            'strip':      prefix + '-strip',
            'pkgconfig':  mingw + '-pkg-config',
            'exe_wrapper': 'wine',
        },
        properties={
            'root': '/usr/' + prefix,
        },
        host_machine={
            'system': 'windows',
            'cpu_family': 'x86',
            'cpu': cpu,
            'endian': 'little',
        },
    )


mingw_base(32).write_to_file()
mingw_base(64).write_to_file()


mingw_cross_osx = CrossDefinitions(
    'mingw/mingw64_cross_osx',
    'Something crazy: compiling on Linux a crosscompiler that\n'
    'runs on Windows and generates code for OSX.',
    based_on=mingw_base(64),
    target_machine={
     'system': 'darwin',
     'cpu_family': 'arm',
     'cpu': 'armv7h',
     'endian': 'little',
    },
)
mingw_cross_osx.write_to_file()
