import os
import ghostscript

def convert_spl_to_pdf(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    # Set up Ghostscript arguments
    args = [
        "pdf2spl",  # Program name
        "-dNOPAUSE",  # No pause after each page
        "-dBATCH",  # Exit after processing all pages
        "-sDEVICE=pdfwrite",  # Output device
        f"-sOutputFile={output_file}",  # Output file
        input_file  # Input file
    ]

    # Convert using Ghostscript
    ghostscript.Ghostscript(*args)

if __name__ == "__main__":
    input_spl = ".spl"  # Change this to your .spl file path
    output_pdf = "output.pdf"  # Change this to your desired .pdf file path
    convert_spl_to_pdf(input_spl, output_pdf)
    print(f"Converted {input_spl} to {output_pdf}")