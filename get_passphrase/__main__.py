#!/usr/bin/env python3

# Main module, intended to run with -m.  do not use relative imports

from typing import Optional, Sequence, List

import sys

from get_passphrase import resolve_passphrase, PassphraseContext, Passphrase, __version__ as pkg_version

def run(argv: Optional[Sequence[str]]=None) -> int:
  import argparse

  parser = argparse.ArgumentParser(description="Resolve a passphrase in a number of ways.")
  parser.add_argument('passphrase', nargs='*',
                      help='A list of smart passphrase descriptors to be checked in order. The first one that produces a passphrase is used.')
  parser.add_argument('--version', action='store_true', default=False,
                      help='Display version')
  args = parser.parse_args(argv)

  if args.version:
    print(pkg_version)
    return 0

  descriptors: List[str] = args.passphrase
  passphrase = resolve_passphrase(descriptors)
  print(passphrase.get_cleartext())
  return 0

if __name__ == "__main__":
  sys.exit(run())
