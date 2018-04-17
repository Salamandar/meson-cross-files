#!/bin/env python3

from cross_definitions import CrossDefinitions


###############################################################################

# Some examples of use

# NB : for "virtual" definitions like openocd or arm_none_eabi, writing to file
# is **not** necessary!

def ARM(cpu):
    return CrossDefinitions(
        'arm/ARM architecture ' + cpu,
        '',
        host_machine={
            'cpu_family': 'arm',
            'endian':     'little',
            'system':     'none',
            'cpu':        cpu,
        }
    )



arm_none_eabi = CrossDefinitions(
    'arm/arm-none-eabi-base',
    'Base of arm-none-eabi defs',
    binaries={
        'c':        'arm-none-eabi-' + 'gcc',
        'cpp':      'arm-none-eabi-' + 'g++',
        'ld':       'arm-none-eabi-' + 'ld',
        'ar':       'arm-none-eabi-' + 'ar',
        'as':       'arm-none-eabi-' + 'as',
        'size':     'arm-none-eabi-' + 'size',
        'objdump':  'arm-none-eabi-' + 'objdump',
        'objcopy':  'arm-none-eabi-' + 'objcopy',
        'strip':    'arm-none-eabi-' + 'strip',
    }
)
arm_none_eabi.write_to_file()


openocd = CrossDefinitions('openocd', '', {'openocd': 'openocd', })
# openocd.write_to_file()


stm32f0 = CrossDefinitions('arm/stm32/stm32f0', 'Definitions for stm32f0')
stm32f0.based_on(ARM('cortex-m0'))
stm32f0.based_on(arm_none_eabi)
stm32f0.based_on(openocd)
stm32f0.write_to_file()
