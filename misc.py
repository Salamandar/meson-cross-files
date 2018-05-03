#!/bin/env python3
from cross_definitions import CrossDefinitions

# Misc cross definitions, inspired from the meson repository

iphone_root = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer'
iphone_cargs = [
    '-arch=armv7',
    '-miphoneos-version-min=8.0',
    '-isysroot=' + iphone_root + '/SDKs/iPhoneOS8.4.sdk',
]
iphone = CrossDefinitions(
    'iphone/iphone',
    'This is a cross compilation file from OSX Yosemite to iPhone\n'
    'Apple keeps changing the location and names of files so\n'
    'these might not work for you. Use the googels and xcrun.',
    binaries={
        'c': 'clang',
        'cpp': 'clang++',
        'ar': 'ar',
        'strip': 'strip',
    },
    properties={
        'c_args': iphone_cargs,
        'cpp_args': iphone_cargs,
        'c_link_args': iphone_cargs,
        'cpp_link_args': iphone_cargs,

        'root': iphone_root,
        'has_function_printf': True,
        'has_function_hfkerhisadf': False,
    },

    host_machine={
        'system': 'darwin',
        'cpu_family': 'arm',
        'cpu': 'armv7',
        'endian': 'little',
    }
)

iphone.write_to_file()
