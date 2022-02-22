# get-passphrase

Extensible passphrase resolver, supporting prompting as well as passphrases stored in environment variables, files or keyrings

Some examples of smart passphrase descriptors:

- `pass:<passphrase>`  to directly provide a passphrase inline
- `env:<env-var-name>` to get the passphrase from an environment variable. The application may configure a custom environment dictionary, or `os.osenviron()` is used
- `file:<file-name>` to get the passphrase from the file at location pathname. The application may configure a base directory for relative paths, or the current working directory is used.
- `fd:<file-descriptor-number>` read the passphrase from the provided file descriptor number
- `stdin:` to read from standard input
- `prompt:` to prompt the user with "Password: " and read from console with typed characters hidden (uses [getpass](https://docs.python.org/3/library/getpass.html))
- `prompt:<prompt-string>` to prompt the user with a custom prompt string and read from console with typed characters hidden (uses [getpass](https://docs.python.org/3/library/getpass.html))
- `keyring:<service-name>,<key-name>` to load the passphrase from [keyring](https://pypi.org/project/keyring/). The application may configure a prefix that will be prepended to either the service-name or the key-name or both, to define a unique namespace for the application.
- `keyring:<key-name>` to load the passphrase from [keyring](https://pypi.org/project/keyring/), using a default service name configured by the application. The application may configure a prefix that will be prepended to key-name, to define a unique namespace for the application.
- `none:`  To provide a `None` value for the passphrase (useful for chaining defaults)
- `empty:`  To provide an empty passphrase

## Command tool
A command tool, `get-passphrase`, is provided that will expand a smart passphrase descriptor provided as an argument.

### Usage:
```
usage: get-passphrase [-h] [--version] [passphrase [passphrase ...]]

Resolve a passphrase in a number of ways.

positional arguments:
  passphrase  A list of smart passphrase descriptors to be checked in order. The first one that produces a passphrase is used.

optional arguments:
  -h, --help  show this help message and exit
  --version   Display version
```

## Library

### Usage

```python
from get_passphrase import resolve_passphrase

descriptor = input("Enter smart passphrase descriptor:")

print("Passphrase is: ", resolve_passphrase(descriptor).get_cleartext())
```
