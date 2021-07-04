scientists = ["Marie Curie", "Albert Einstein", "Rosalind Franklin",
              "Niels Bohr", "Dian Fossey", "Isaac Newton",
              "Grace Hopper", "Charles Darwin", "Lise Meitner"]

sorted(scientists, key=lambda name: name.split()[-1])
