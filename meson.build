
project('meson-cross-files',
  meson_version: '>=0.44.0'
)



parts = [
  [ 'arm', 'arm.py' ],
]

foreach part: parts
  subdir = part[0]
  script = part[1]

  custom_target(subdir,
    depend_files: [ 'cross_definitions.py', script, ],
    command: [ find_program(script), ],
    output: subdir,
    install: true,
    install_dir: join_paths(get_option('datadir'), 'meson', 'cross')
  )

endforeach
