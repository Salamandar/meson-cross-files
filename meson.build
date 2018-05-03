
project('meson-cross-files',
  meson_version: '>=0.44.0'
)



custom_target('generate',
  depend_files: [
    'cross_definitions.py',
    'all.py',
    'arm.py',
    'misc.py',
    'mingw.py',
  ],
  command: [ find_program('all.py'), ],
  output: [
    'arm',
    'iphone',
    'mingw',
  ],
  install: true,
  install_dir: join_paths(get_option('datadir'), 'meson', 'cross')
)
