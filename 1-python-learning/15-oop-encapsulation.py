from rishka_lib import Genome

praveens_genome=Genome('AAAA','Praveen','O+','AGCT')

praveens_genome.set_dna_sequence('AAGT')
praveens_genome.set_dna_sequence('aaaa')

if praveens_genome.hasMutation:
    print("Praveen is a mutant")

# praveens_dna_sequence=praveens_genome.get_dna_sequence()
# if praveens_dna_sequence:
#     print(f"Praveens dna sequence is {praveens_dna_sequence}")
  
praveens_genome.describe_genome()  
praveens_genome.dna_sequence='SLAY'
praveens_genome.describe_genome()  
print(praveens_genome.get_dna_sequence())
print(praveens_genome.dna_sequence)
