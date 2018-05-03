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
        },
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


arm_linux_gnueabi_gcc = CrossDefinitions(
    'arm/arm-linux-gnueabihf-gcc-base',
    'Base of arm-linux-gnueabihf defs',
    binaries={
        'c':        'arm-linux-gnueabihf-gcc',
        'cpp':      'arm-linux-gnueabihf-g++',
        'rust':     ['rustc', '--target', 'arm-unknown-linux-gnueabihf'],
                    # '-C', 'linker=/usr/bin/arm-linux-gnueabihf-gcc-7'
        'ld':       'arm-linux-gnueabihf-ld',
        'ar':       'arm-linux-gnueabihf-ar',
        'as':       'arm-linux-gnueabihf-as',
        'size':     'arm-linux-gnueabihf-size',
        'objdump':  'arm-linux-gnueabihf-objdump',
        'objcopy':  'arm-linux-gnueabihf-objcopy',
        'strip':    'arm-linux-gnueabihf-strip',
        'gdb':      'arm-linux-gnueabihf-gdb',
        'pkgconfig':'arm-linux-gnueabihf-pkg-config',
    },
    properties={
        'root': '/usr/arm-linux-gnueabihf',
        'c_args': [
        ],
        'has_function_printf': True,
        'has_function_hfkerhisadf': False,
    },
    host_machine={
        'system': 'linux',
        'cpu_family': 'arm',
    }
)


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
    properties={
        'c_args': [
        ],
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


###############################################################################
# Stm32

def stm32(cortex):
    stm32 = CrossDefinitions(
        'arm/stm32base',
        'Common definitions for STM32',
        properties={
            'c_args': [
                # # Code-optimization / deletion:
                '-fdata-sections',      # each variable to a seperate section
                '-ffunction-sections',  # each function to a seperate section

                '-fno-common',  # Really wanted ?
                '-mthumb',
                '-mcpu=' + cortex,
                '--static',
            ],
            'c_link_args': [
                '-Wl,--gc-sections',
                '-nostartfiles',
            ],
        },
        based_on=[
            ARM(cortex),
            arm_none_eabi_gcc,
            openocd,
        ],
    )
    return stm32


# STM32 Families
stm32f0 = CrossDefinitions(
    'arm/stm32/stm32f0', '',
    properties={
        'c_args': ['-mfloat-abi=soft'],
    },
    based_on=stm32('cortex-m0'),
)
# stm32f1 = CrossDefinitions(
#     'arm/stm32/stm32f1', '',
#     based_on=stm32('cortex-m3'),
# )
# stm32f2 = CrossDefinitions(
#     'arm/stm32/stm32f2', '',
#     based_on=stm32('cortex-m3'),
# )
stm32f3 = CrossDefinitions(
    'arm/stm32/stm32f3', '',
    properties={
        'c_args': ['-mfloat-abi=hard', '-mfpu=fpv4-sp-d16'],
    },
    based_on=stm32('cortex-m4f'),
)
stm32f4 = CrossDefinitions(
    'arm/stm32/stm32f4', '',
    properties={
        'c_args': ['-mfloat-abi=hard', '-mfpu=fpv4-sp-d16'],
    },
    based_on=stm32('cortex-m4f'),
)
# stm32f7 = CrossDefinitions(
#     'arm/stm32/stm32f7', '',
#     based_on=stm32('cortex-m7f'),
# )

# stm32l0 = CrossDefinitions(
#     'arm/stm32/stm32l0', '',
#     based_on=stm32('cortex-m0+'),
# )
# stm32l1 = CrossDefinitions(
#     'arm/stm32/stm32l1', '',
#     based_on=stm32('cortex-m3'),
# )
stm32l4 = CrossDefinitions(
    'arm/stm32/stm32l4', '',
    properties={
        'c_args': ['-mfloat-abi=hard', '-mfpu=fpv4-sp-d16'],
    },
    based_on=stm32('cortex-m3'),
)

for i in [
    stm32f0,
    # stm32f1,
    # stm32f2,
    stm32f3,
    stm32f4,
    # stm32f7,
    # stm32l0,
    # stm32l1,
    stm32l4,
]:
    i.write_to_file()

# STM32 specific mcus
