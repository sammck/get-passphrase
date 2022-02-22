get-passphrase
---------

Extensible passphrase resolver, supporting prompting as well as passphrases stored in environment variables, files or keychains

Some examples of smart passwords:

    env:somevar to get the password from an environment variable
    file:somepathname to get the password from the first line of the file at location pathname
    fd:number to get the password from the file descriptor number.
    stdin to read from standard input
