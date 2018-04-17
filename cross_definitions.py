#!/bin/env python3
import os

###############################################################################


class CrossDefinitions():
    def __init__(self,
                 name,
                 description,
                 binaries=None,
                 properties=None,
                 host_machine=None,
                 target_machine=None):
        self.name = name
        self.description = description

        self.sections_overlay = {
            'binaries':       binaries,
            'properties':     properties,
            'host_machine':   host_machine,
            'target_machine': target_machine,
        }
        self.sections_base = {}

    # Write to destdir/filename or filename
    def write_to_file(self, destdir=''):
        self.__apply_base()

        with open(os.path.join(destdir, self.name + '.txt'), 'w') as crossfile:

            # Write commented description
            crossfile.write(''.join([
                '# ' + i for i in self.description.splitlines(True)
            ]))

            # Write section and its variables
            def write_section(name, variables):
                crossfile.write('\n[{0}]\n'.format(name))
                maxnamelen = len(max(variables.keys(), key=len))
                for name, value in variables.items():
                    if value is not '':
                        crossfile.write('{0} = {1}\n'.format(
                            name.ljust(maxnamelen), repr(value)
                        ))

            # Write all sections, if not empty
            for name, values in self.sections_base.items():
                if values is not None:
                    write_section(name, values)

    def merge_to_base(self, base, overlay):
        for (ov_name, ov_values) in overlay.items():
            if ov_values is not None:
                if ov_name not in base or base[ov_name] is None:
                    base[ov_name] = dict()
                base[ov_name].update(ov_values)

    # Update as an overlay to base
    def based_on(self, base):
        self.description += '\nBased on \'{0}\''.format(base.name)
        self.merge_to_base(self.sections_base, base.sections_base)
        self.merge_to_base(self.sections_base, base.sections_overlay)

    def __apply_base(self):
        self.merge_to_base(self.sections_base, self.sections_overlay)


###############################################################################


arm_none_eabi = CrossDefinitions(
    'arm-none-eabi-base',
    'Base of arm-none-eabi defs',
    {
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
openocd.write_to_file()


stm32 = CrossDefinitions('stm32', 'Definitions for stm32')
stm32.based_on(openocd)
stm32.based_on(arm_none_eabi)
stm32.write_to_file()