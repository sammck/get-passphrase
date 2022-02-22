# get-passphrase

Extensible passphrase resolver, supporting prompting as well as passphrases stored in environment variables, files or keychains

Some examples of smart passwords:

- `pass:<passphrase>`  to directly provide a passphrase inline
- `env:<env-var-name>` to get the passphrase from an environment variable
- `file:<file-name>` to get the passphrase from the file at location pathname
- `fd:<file-descriptor-number>` read the passphrase from the provided file descriptor number
- `stdin:` to read from standard input
- `prompt:` to prompt the user with "Password: " and read from console with typed characters hidden
- `prompt:<prompt-string>` to prompt the user with a custom prompt string and read from console with typed characters hidden
