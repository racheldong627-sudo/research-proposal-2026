#!/bin/bash
# PDF to Markdown Conversion Script for Literature Studies

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

# Convert each PDF
converted_count=0
for pdf in "papers pdf"/*.pdf; do
    if [ -f "$pdf" ]; then
        filename=$(basename "$pdf" .pdf)
        output_file="papers md/${filename}.md"
        
        echo "📄 Converting: $filename.pdf"
        
        # Convert with pandoc
        if pandoc "$pdf" -t gfm -o "$output_file" 2>> conversion.log; then
            echo "✅ Success: $filename.md created"
            ((converted_count++))
            
            # Add header to markdown file
            temp_file=$(mktemp)
            {
                echo "# Literature Review: $filename"
                echo ""
                echo "**Source:** \`papers pdf/$filename.pdf\`"
                echo "**Converted:** $(date)"
                echo "**Status:** Auto-converted from PDF"
                echo ""
                echo "---"
                echo ""
                cat "$output_file"
            } > "$temp_file"
            mv "$temp_file" "$output_file"
            
        else
            echo "❌ Failed: $filename.pdf conversion error"
        fi
    fi
done

echo ""
echo "📊 Conversion Summary:"
echo "====================="
echo "📁 Total PDFs processed: $(ls "papers pdf"/*.pdf 2>/dev/null | wc -l)"
echo "✅ Successfully converted: $converted_count"
echo "📝 Markdown files created in: papers md/"
echo ""
echo "Next steps:"
echo "1. Review the converted markdown files in papers md/"
echo "2. Edit and clean up the content as needed"
echo "3. Update literature-matrix.md with new entries"
echo "4. Add bibliography entries to bibliography.bib"