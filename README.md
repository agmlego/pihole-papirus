# pihole-papirus

I did not care for the ultra-simple options currently available, so for my Pi 3B+ running PiHole, with a PaPiRus HAT Medium attached, I wrote this.

## Requires

- [PiHole-api](https://pypi.org/project/PiHole-api/)
- [PaPiRus](https://github.com/PiSupply/PaPiRus) (currently cannot be installed with pip)
- [B612 font](https://b612-font.com/), also availavle as the `fonts-b612` APT package

## `secrets.ini`

You need to put your Pi-Hole administrative password into a `secrets.ini` file as below:

    [pihole]
    password = YOUR_PASSWORD_HERE
