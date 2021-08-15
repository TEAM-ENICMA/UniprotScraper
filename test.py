import UniprotScraper as us

fasta = us.get_with_header("P04418")
print(fasta)

sequence = us.get_without_header("P04418")
print(sequence)

header = us.get_only_header("P04418")
print(header)

three_aa = us.get_first_three_aa("P04418")
print(three_aa)

five_aa = us.get_first_five_aa("P04418")
print(five_aa)

ten_aa = us.get_first_ten_aa("P04418")
print(ten_aa)