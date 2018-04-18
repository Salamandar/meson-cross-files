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
        self.used = False
        self.name = name
        self.description = description

        self.sections_overlay = {
            'binaries':       binaries,
            'properties':     properties,
            'host_machine':   host_machine,
            'target_machine': target_machine,
        }
        self.sections_base = {
            'binaries':       None,
            'properties':     None,
            'host_machine':   None,
            'target_machine': None,
        }

    # Write to destdir/filename or filename
    def write_to_file(self, destdir=''):
        self.__apply_base()

        outfilepath = os.path.join(destdir, self.name + '.txt')
        os.makedirs(os.path.dirname(outfilepath) or '.', exist_ok=True)
        with open(outfilepath, 'w') as crossfile:

            # Write commented description
            crossfile.write(''.join([
                '# ' + i for i in self.description.splitlines(True)
            ]))
            crossfile.write('\n')

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

    def merge_to_base(self, baselay, overlay):
        for section in overlay.keys():
            if overlay[section] is not None:

                # Initialize as dict first…
                if section not in baselay or \
                   baselay[section] is None:
                    baselay[section] = dict()

                # Replace scalars, merge lists
                for it in overlay[section].keys():
                    if it in baselay[section] and \
                      (isinstance(overlay[section][it], list) or \
                       isinstance(baselay[section][it], list)):
                        baselay[section][it] = [
                            item for sublist in [
                                baselay[section][it], overlay[section][it],
                            ] for item in sublist
                        ]
                    else:
                        baselay[section][it] = overlay[section][it]

    # Update as an overlay to base
    def based_on(self, base):
        if self.used:
            raise RuntimeError('Definitions ' + self.name + ' already used!')
        base.__apply_base()
        self.description += '\nBased on \'{0}\''.format(base.name)
        self.merge_to_base(self.sections_base, base.sections_base)

    def __apply_base(self):
        self.used = True
        self.merge_to_base(self.sections_base, self.sections_overlay)
