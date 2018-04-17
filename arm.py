#!/bin/env python3

from cross_definitions import CrossDefinitions

# Some examples of use
# NB : for "virtual" definitions like openocd or arm_none_eabi, writing to file
# is **not** necessary!

###############################################################################
# Architectures


def ARM(cpu):
    return CrossDefinitions(
        'arm/arm-base-' + cpu,
        '',
        host_machine={
            'cpu_family': 'arm',
            'endian':     'little',
            'system':     'none',
            'cpu':        cpu,
        }
    )


# Possible extensions: m a f d q c
def RISCV(base='rv32i', extensions=''):
    return CrossDefinitions(
        'riscv/riscv-base-' + base + '-[' + extensions + ']',
        '',
        host_machine={
            'cpu_family': 'riscv',
            'endian':     'little',
            'system':     'none',
            'cpu':        base,
        }
    )


###############################################################################
# Toolchains


arm_none_eabi_gcc = CrossDefinitions(
    'arm/arm-none-eabi-gcc-base',
    'Base of arm-none-eabi defs',
    binaries={
        'c':        'arm-none-eabi-gcc',
        'cpp':      'arm-none-eabi-g++',
        'ld':       'arm-none-eabi-ld',
        'ar':       'arm-none-eabi-ar',
        'as':       'arm-none-eabi-as',
        'size':     'arm-none-eabi-size',
        'objdump':  'arm-none-eabi-objdump',
        'objcopy':  'arm-none-eabi-objcopy',
        'strip':    'arm-none-eabi-strip',
        'gdb':      'arm-none-eabi-gdb',
    },
)


arm_none_eabi_clang = CrossDefinitions(
    'arm/arm-none-eabi-clang-base',
    'Base of arm-none-eabi defs',
    binaries={
        'c':        'clang',
        'cpp':      'clang++',
        'ld':       'llvm-link',
        'ar':       'llvm-ar',
        'as':       'llvm-as',
        'size':     'llvm-size',
        'objdump':  'llvm-objdump',
        'objcopy':  'arm-none-eabi-objcopy',
        'strip':    'arm-none-eabi-strip',
        'gdb':      'arm-none-eabi-gdb',
    },
    properties={
        'c_args': [
            '--target=arm-none-eabi',
            '-mthumb'
        ],
        'c_link_args': [
            '--target=arm-none-eabi',
            '-nostdlib',
        ],
    },
)

# arm_none_eabi.write_to_file()


openocd = CrossDefinitions('openocd', '', {'openocd': 'openocd', })
# openocd.write_to_file()

# Stm32F*

stm32f0 = CrossDefinitions('arm/stm32/stm32f0', 'Definitions for stm32f0')
stm32f0.based_on(ARM('cortex-m0'))
stm32f0.based_on(arm_none_eabi_gcc)
stm32f0.based_on(openocd)
stm32f0.write_to_file()


stm32f1 = CrossDefinitions('arm/stm32/stm32f1', 'Definitions for stm32f1')
stm32f1.based_on(ARM('cortex-m3'))
stm32f1.based_on(arm_none_eabi_gcc)
stm32f1.based_on(openocd)
stm32f1.write_to_file()


stm32f2 = CrossDefinitions('arm/stm32/stm32f2', 'Definitions for stm32f2')
stm32f2.based_on(ARM('cortex-m3'))
stm32f2.based_on(arm_none_eabi_gcc)
stm32f2.based_on(openocd)
stm32f2.write_to_file()


stm32f3 = CrossDefinitions('arm/stm32/stm32f3', 'Definitions for stm32f3')
stm32f3.based_on(ARM('cortex-m4f'))
stm32f3.based_on(arm_none_eabi_gcc)
stm32f3.based_on(openocd)
stm32f3.write_to_file()


stm32f4 = CrossDefinitions('arm/stm32/stm32f4', 'Definitions for stm32f4')
stm32f4.based_on(ARM('cortex-m4f'))
stm32f4.based_on(arm_none_eabi_gcc)
stm32f4.based_on(openocd)
stm32f4.write_to_file()


stm32f7 = CrossDefinitions('arm/stm32/stm32f7', 'Definitions for stm32f7')
stm32f7.based_on(ARM('cortex-m7f'))
stm32f7.based_on(arm_none_eabi_gcc)
stm32f7.based_on(openocd)
stm32f7.write_to_file()

# Stm32L*

stm32l0 = CrossDefinitions('arm/stm32/stm32l0', 'Definitions for stm32l0')
stm32l0.based_on(ARM('cortex-m0+'))
stm32l0.based_on(arm_none_eabi_gcc)
stm32l0.based_on(openocd)
stm32l0.write_to_file()


stm32l1 = CrossDefinitions('arm/stm32/stm32l1', 'Definitions for stm32l1')
stm32l1.based_on(ARM('cortex-m3'))
stm32l1.based_on(arm_none_eabi_gcc)
stm32l1.based_on(openocd)
stm32l1.write_to_file()


stm32l4 = CrossDefinitions('arm/stm32/stm32l4', 'Definitions for stm32l4')
stm32l4.based_on(ARM('cortex-m3'))
stm32l4.based_on(arm_none_eabi_gcc)
stm32l4.based_on(openocd)
stm32l4.write_to_file()
