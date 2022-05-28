def sanatizeOutput(output):
    output = output.replace("gpg", "cgp")

    output = output.replace("GnuPG", "CMU PGP")

    output = output.replace("gnupg", "cmupgp")

    return output
