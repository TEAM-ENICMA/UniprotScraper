import UniprotScraper as us

uni_id = "P04418"

ident = us.get_identification(uni_id)
print(ident)

access = us.get_accession(uni_id)
print(access)

date = us.get_date(uni_id)
print(date)

desc = us.get_description(uni_id)
print(desc)

spec = us.get_species(uni_id)
print(spec)

classif = us.get_classification(uni_id)
print(classif)

tax = us.get_taxonomy_ref(uni_id)
print(tax)

info = us.get_information(uni_id)
print(info)

head = us.get_seq_header(uni_id)
print(head)

seq = us.get_sequence(uni_id)
print(seq)

first_three = us.get_first_three_aa(uni_id)
print(first_three)

first_five = us.get_first_five_aa(uni_id)
print(first_five)

first_ten = us.get_first_ten_aa(uni_id)
print(first_ten)

aa_content = us.get_aa_content(uni_id)
print(aa_content)
