file_input = r'C:\Users\gaeta\Documents\Uni&Lavoro\Studio\Tesi\Datasets\New\output4o_cleaned.txt'
file_output = r'C:\Users\gaeta\Documents\Uni&Lavoro\Studio\Tesi\Datasets\New\V2_output4o_cleaned.txt'

with open(file_input, 'r', encoding='utf-8') as infile, open(file_output, 'w', encoding='utf-8') as outfile:
    for line in infile:
        if "LIS" not in line:
            outfile.write(line)