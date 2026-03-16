# Clinical Genomic Analyst
class Genome:
    
    def __init__(self,dna_sequence,patient, blood_type,baseline_genome):
        self._dna_sequence=dna_sequence
        self._patient=patient
        self._blood_type=blood_type
        self._baseline_genome=baseline_genome
        
    def hasMutation(self):
        if self._dna_sequence!=self._baseline_genome:
            return True
        else:
            return False
        
    def set_dna_sequence(self,new_sequence):
        #input sanitation
        new_sequence=new_sequence.upper()
        
        #input validation
        valid_bases='AGCT'
        invalid_sequence=False
        for base in new_sequence:
            if not base in valid_bases:
                invalid_sequence=True
                print(f"Error: Only valid bases are {valid_bases}")
                return False
        
        self._dna_sequence=new_sequence
        print("New sequence coded in succesfully!")
        return True
    
    def get_dna_sequence(self):
        password='monkeypox'
        user_input=input('This information is protected. Please enter password: ')
        if user_input==password:
            return self._dna_sequence
        else:
            return False
        
    def describe_genome(self):
        print(f"This {self._dna_sequence} belongs to {self._patient} who has a blood type of {self._blood_type}")
        
        
rishka_genome= Genome('ACCT','Rishka Raj','O+','AGCT')
if rishka_genome.hasMutation:
    print("Rishka is a mutant")


# class Patient():  
#     def __init__(self, weight):
#         self.set_weight(weight)

#     # SETTER: controls stored value
#     def set_weight(self, weight):
#         if weight < 0:
#             return
#         self._weight = weight   # stored in KG

#     # GETTER: controlled access
#     def get_weight(self):
#         return self._weight

#     def weight_kg(self):
#         print(f"patient's weight is {self.get_weight()} kg")

#     def weight_g(self):
#         g = self.get_weight() * 1000
#         print(f"patient's weight is {g} g")

# patient2=Weight(23)
# patient2.set_weight(56)
# patient2.get_weight()
# patient2.weight_kg()
# patient2.weight_g() 


