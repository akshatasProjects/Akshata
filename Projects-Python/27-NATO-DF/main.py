import pandas

readCSV_data = pandas.read_csv("/Users/ajitjog/Desktop/Akshata/Projects-Python/27-NATO-DF/nato_phonetic_alphabet.csv")
# print(readCSV_data)
# # Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phoenetic_data = {row.letter:row.code for (index, row) in readCSV_data.iterrows()}
# print(phoenetic_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Word: ").upper()
output_list = [phoenetic_data[letter] for letter in user_input]
print(output_list)


