
### Translation of mRNA to Protein



## Project Overview
This project was developed as part of the end-semester evaluation for the course __21 BIO 201 Intelligence of Biological Systems 2__ at Amrita School of Engineering, Bangalore. The goal of this project is to bio-mimic the functionality of ribosomes and tRNA molecules by translating mRNA sequences into chains of amino acids (proteins).


## Abstract

The project aims to develop a Python-based system that simulates the translation process, converting mRNA sequences into their corresponding amino acid sequences. The code makes use of built-in Python functions, such as file reading and dictionary data structures, to accurately replicate the biological process of protein synthesis.
## Features

 - __mRNA Sequence Processing__: The system reads mRNA sequences from a text file, processes the sequence by removing unnecessary characters, and checks for proper codon structure.
 - __Translation to Protein__: The program translates the mRNA sequence into a chain of amino acids using a predefined genetic code dictionary.
 - __Error Handling__: The system checks whether the mRNA sequence has a complete number of codons and prompts the user if adjustments are needed.

## Program Flow
1. **Input**: The mRNA sequence is read from a text file and cleaned to remove empty lines or whitespace.
2. **Codon Validation**: The program checks if the sequence length is divisible by three, ensuring that it consists of whole codons.
3. **Translation**:
 - The mRNA sequence is split into codons (three nucleotides each).
 - Each codon is matched to its corresponding amino acid using a dictionary that maps codons to amino acids.
 - The amino acids are concatenated into a protein sequence, with adjacent amino acids separated by a hyphen (`-`) to represent peptide bonds.
4. **Output**:
 - The program prints the number of codons translated.
 - The resulting amino acid sequence (protein) is displayed.
## Conclusion
The Python code effectively replicates the functionality of ribosomes and tRNA molecules in cellular translation mechanisms. The translated amino acid sequence can be used for further downstream analysis of the protein's effects on the body. Future enhancements could include stopping the translation process upon encountering a stop codon, as occurs in biological systems.


## Authors
- [@AkhileshP06](https://github.com/AkhileshP06)
- [@Amalkrishnaaa](https://github.com/Amalkrishnaaa)
- [@Karthick-7014](https://github.com/Karthick-7014)

