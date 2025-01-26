import qrcode as qr
image = qr.make("https://github.com/seenumehta?tab=repositories")
image.save("git_repos.png")

