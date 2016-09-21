Quickly `cd` to configured directory aliases:

    $ jump -h
    usage: jump <name>
           jump --add <name> <target>
           jump --list

    options:
      -l, --list   list all jump destinations
      -a, --add    add new destination

This uses insane and horrible hack from
http://stackoverflow.com/a/16694919/239247
and therefore works only for Linux.

### Status

* [ ] jump name  (hardcoded)
* [ ] jump name  (with config)
* [ ] jump -h    (also fail on Windows)
* [ ] jump --add (also document where config is saved)
* [ ] --list
