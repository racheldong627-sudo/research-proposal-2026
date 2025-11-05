#!/bin/bash
# Enhanced PDF to Markdown Conversion Script

echo "🔄 Converting PDFs to Markdown..."
echo "=================================="

# Check if papers pdf directory has PDFs
if [ ! "$(ls -A "papers pdf"/*.pdf 2>/dev/null)" ]; then
    echo "❌ No PDF files found in 'papers pdf' directory"
    echo "Please upload your PDF files to the 'papers pdf' folder first"
    exit 1
fi

# Ensure papers md directory exists
mkdir -p "papers md"

# Create conversion log
echo "Conversion started: $(date)" > conversion.log

# Create Python script for PDF extraction
cat > pdf_to_md.py << 'EOF'
#!/usr/bin/env python3
import sys
import os
import fitz  # PyMuPDF
from datetime import datetime

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using PyMuPDF"""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += f"\n\n## Page {page_num + 1}\n\n"
            text += page.get_text()
        
        doc.close()
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

def create_markdown_file(pdf_path, output_path):
    """Convert PDF to Markdown with proper formatting"""
    filename = os.path.basename(pdf_path).replace('.pdf', '')
    
    # Extract text
    content = extract_text_from_pdf(pdf_path)
    
    # Create markdown with header
    markdown = f"""# Literature Review: {filename}

**Source:** `{pdf_path}`  
**Converted:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Status:** Auto-converted from PDF using PyMuPDF  

---

{content}

---

## Notes
- Auto-converted from PDF
- Please review and clean up formatting as needed
- Add manual annotations and summaries above this line
"""
    
    # Write to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf_to_md.py input.pdf output.md")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    
    if create_markdown_file(pdf_path, output_path):
        print(f"✅ Successfully converted: {os.path.basename(pdf_path)}")
    else:
        print(f"❌ Failed to convert: {os.path.basename(pdf_path)}")
EOF

# Make Python script executable
chmod +x pdf_to_md.py

# Convert each PDF
converted_count=0
failed_count=0

for pdf in "papers pdf"/*.pdf; do
    if [ -f "$pdf" ]; then
        filename=$(basename "$pdf" .pdf)
        output_file="papers md/${filename}.md"
        
        echo "📄 Converting: $filename.pdf"
        
        # Use Python script for conversion
        if python3 pdf_to_md.py "$pdf" "$output_file" 2>> conversion.log; then
            ((converted_count++))
        else
            echo "❌ Failed: $filename.pdf conversion error"
            ((failed_count++))
        fi
    fi
done

echo ""
echo "📊 Conversion Summary:"
echo "====================="
echo "📁 Total PDFs found: $(ls "papers pdf"/*.pdf 2>/dev/null | wc -l)"
echo "✅ Successfully converted: $converted_count"
echo "❌ Failed conversions: $failed_count"
echo "📝 Markdown files created in: papers md/"
echo ""
echo "Next steps:"
echo "1. Review the converted markdown files in 'papers md/'"
echo "2. Clean up formatting and add manual annotations"
echo "3. Update literature-matrix.md with new entries"
echo "4. Add bibliography entries to bibliography.bib"

# Clean up temporary script
rm pdf_to_md.py