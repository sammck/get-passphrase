#!/usr/bin/env python3

from typing import Optional, Sequence, List

from get_passphrase import resolve_passphrase, PassphraseContext, Passphrase

import sys

def main(argv: Optional[Sequence[str]]=None) -> int:
  import argparse

  parser = argparse.ArgumentParser(description="Resolve a passphrase in a number of ways.")
  parser.add_argument('passphrase', nargs='*',
                      help='A list of smart passphrase descriptors to be checked in order. The first one that produces a passphrase is used.')

  args = parser.parse_args(argv)

  descriptors: List[str] = args.passphrase
  passphrase = resolve_passphrase(descriptors)
  print(passphrase.get_cleartext())

if __name__ == "__main__":
  sys.exit(main())