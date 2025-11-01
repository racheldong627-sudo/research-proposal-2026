# Research Proposal Tool - User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Processing Research Papers](#processing-research-papers)
3. [Generating Summaries](#generating-summaries)
4. [Managing References](#managing-references)
5. [Creating Proposals](#creating-proposals)
6. [Advanced Usage](#advanced-usage)

## Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of research paper structure

### Installation
```bash
# Clone the repository
git clone https://github.com/racheldong627-sudo/research-proposal-2026.git
cd research-proposal-2026

# No additional dependencies needed - uses Python standard library
```

## Processing Research Papers

### What it does
The paper processor extracts key sections from research papers:
- Title, authors, year, keywords
- Abstract
- Methods/Methodology
- Results/Findings
- Conclusion

### How to use
```bash
python research_tool_cli.py process input_paper.txt -o output.json
```

### Expected Input Format
Your paper should be in plain text with recognizable section headers:
```
Title of the Paper

Author Names

Year

Keywords: keyword1, keyword2, keyword3

Abstract
The abstract text goes here...

Introduction
Introduction text...

Methods
Methodology description...

Results
Results and findings...

Conclusion
Concluding remarks...
```

### Output Format
JSON file containing all extracted information:
```json
{
  "metadata": {
    "title": "Paper Title",
    "year": "2023",
    "keywords": ["keyword1", "keyword2"]
  },
  "abstract": "...",
  "methods": "...",
  "results": "...",
  "conclusion": "..."
}
```

## Generating Summaries

### What it does
Creates concise summaries highlighting:
- Key points from abstract
- Main methodological approach
- Important findings (up to 5 key points)
- Brief conclusion

### How to use
```bash
python research_tool_cli.py summarize input_paper.txt -o summary.txt
```

### Output Example
```
TITLE: Machine Learning Approaches for Climate Change Prediction
YEAR: 2023
KEYWORDS: machine learning, climate change, prediction models

ABSTRACT SUMMARY:
Climate change poses significant challenges. This study explores machine learning for predicting patterns. We investigate neural networks and ensemble methods.

METHODS:
Collected climate data from multiple sources spanning 50 years. Implemented DNNs, Random Forests, and SVMs.

KEY FINDINGS:
1. LSTM networks showed 15% improvement over traditional models
2. Ensemble methods reduced prediction error by 23%
3. Including ocean temperature improved accuracy by 18%
...
```

## Managing References

### Adding References
```bash
python research_tool_cli.py references add \
    -f my_references.json \
    --title "Deep Learning in Healthcare" \
    --authors "Smith, J., Doe, A." \
    --year "2023" \
    --source "Journal of Medical AI" \
    --doi "10.1234/jmai.2023.001"
```

### Listing References
```bash
# List all references
python research_tool_cli.py references list -f my_references.json

# Sort by year
python research_tool_cli.py references list -f my_references.json --sort year

# Sort by title
python research_tool_cli.py references list -f my_references.json --sort title
```

### Exporting References
```bash
# Export in APA format
python research_tool_cli.py references export -f my_references.json --format apa -o refs_apa.txt

# Export in IEEE format
python research_tool_cli.py references export -f my_references.json --format ieee -o refs_ieee.txt
```

## Creating Proposals

### Basic Proposal Generation
```bash
python research_tool_cli.py generate \
    paper1.txt paper2.txt paper3.txt \
    -t "Machine Learning for Climate-Aware Medical Diagnostics" \
    -a "Your Name" \
    -o proposal.md
```

### Specifying Research Type
```bash
# For qualitative research
python research_tool_cli.py generate papers/*.txt \
    -t "Qualitative Study of AI Ethics" \
    -a "Your Name" \
    -r qualitative \
    -o proposal.md

# For quantitative research
python research_tool_cli.py generate papers/*.txt \
    -t "Statistical Analysis of ML Performance" \
    -a "Your Name" \
    -r quantitative \
    -o proposal.md

# For mixed methods (default)
python research_tool_cli.py generate papers/*.txt \
    -t "Mixed Methods Study" \
    -a "Your Name" \
    -r mixed \
    -o proposal.md
```

### Output Structure
The generated proposal includes:
1. **Executive Summary** - Overview of the proposal
2. **Introduction and Background** - Context setting
3. **Literature Review** - Automatically generated from input papers
4. **Research Gap** - Identified gaps based on literature
5. **Research Questions and Objectives** - To be customized
6. **Proposed Methodology** - Template based on research type
7. **Expected Outcomes** - To be completed
8. **Timeline and Milestones** - To be completed
9. **Budget and Resources** - To be completed
10. **References** - Bibliography
11. **Appendices** - Additional materials

## Advanced Usage

### Using the Python API

#### Process Multiple Papers
```python
from research_tool import PaperProcessor, PaperSummarizer

processor = PaperProcessor()
summarizer = PaperSummarizer()

papers = ['paper1.txt', 'paper2.txt', 'paper3.txt']
summaries = []

for paper_file in papers:
    with open(paper_file, 'r') as f:
        text = f.read()
    
    paper_data = processor.process_paper(text)
    summary = summarizer.generate_paper_summary(paper_data)
    summaries.append(summary)
```

#### Custom Proposal Generation
```python
from research_tool import ProposalGenerator

generator = ProposalGenerator()

# Set basic information
generator.set_title("My Research Proposal")
generator.set_author("John Doe")

# Customize sections
generator.set_section('executive_summary', """
This proposal outlines a comprehensive study on...
""")

generator.set_section('introduction', """
The field of X has seen significant advances...
""")

# Generate literature review from papers
lit_review = generator.generate_literature_review_from_papers(summaries)
generator.set_section('literature_review', lit_review)

# Generate complete proposal
proposal = generator.generate_proposal()

# Save to file
generator.save_proposal('my_proposal.md')
```

#### Custom Reference Formatting
```python
from research_tool import ReferenceOrganizer

organizer = ReferenceOrganizer()

# Add references from paper data
organizer.add_reference_from_paper_data(paper_data)

# Add manual reference
organizer.add_reference(
    title="Advanced Machine Learning",
    authors="Johnson, R., Smith, T.",
    year="2024",
    source="Nature Machine Intelligence",
    doi="10.1038/s42256-024-00001"
)

# Search references
results = organizer.search_references("machine learning")

# Export in different formats
apa_refs = organizer.export_references(format='apa')
ieee_refs = organizer.export_references(format='ieee')
```

## Best Practices

### For Paper Processing
1. Ensure papers have clear section headers
2. Use consistent formatting across papers
3. Include full text when possible (not just abstracts)

### For Proposal Generation
1. Process 5-10 related papers for comprehensive literature review
2. Review and edit generated content for accuracy
3. Fill in placeholder sections with specific details
4. Customize research questions based on identified gaps
5. Update methodology based on your specific approach

### For Reference Management
1. Add references as you process papers
2. Include DOIs for easy citation
3. Keep reference database file under version control
4. Export references in required format before submission

## Troubleshooting

### Problem: Sections not extracted correctly
**Solution**: 
- Check that your paper has clear section headings
- Section headers should be on their own lines
- Common patterns recognized: "Abstract", "Introduction", "Methods", "Methodology", "Results", "Findings", "Conclusion"

### Problem: Summary is too brief
**Solution**: 
Use the Python API to adjust parameters:
```python
summary = summarizer.summarize_abstract(abstract, max_sentences=5)
findings = summarizer.extract_key_findings(results, max_points=8)
```

### Problem: Generated proposal needs customization
**Solution**: 
- The tool generates a template with placeholders
- Edit the generated Markdown file to add specific details
- Use `set_section()` in Python API for programmatic customization

### Problem: References not formatted correctly
**Solution**:
- Ensure all required fields are provided (title, authors, year)
- Check that the format parameter is 'apa' or 'ieee'
- Manually review and edit exported reference list

## Tips for PhD Applications

1. **Start Early**: Process papers as you read them
2. **Organize**: Keep all papers in one directory for easy batch processing
3. **Iterate**: Generate multiple proposal drafts with different paper combinations
4. **Customize**: Always review and customize generated content
5. **Cite Properly**: Use the reference manager to maintain accurate citations
6. **Backup**: Keep your reference database file backed up

## Example Workflow

1. **Collect Papers**: Gather 10-15 relevant research papers
2. **Convert to Text**: Ensure papers are in plain text format
3. **Process**: Run processor on each paper
4. **Summarize**: Generate summaries to review quickly
5. **Build References**: Add all papers to reference database
6. **Generate Proposal**: Create initial draft from top 5-7 papers
7. **Refine**: Edit and customize the generated proposal
8. **Export References**: Get formatted bibliography
9. **Finalize**: Complete all placeholder sections
10. **Review**: Have advisors review the proposal

## Next Steps

After generating your initial proposal:
1. Fill in specific research questions
2. Detail your exact methodology
3. Add timeline with realistic milestones
4. Include budget if required
5. Add any appendices (preliminary data, code, etc.)
6. Proofread and format according to requirements
7. Get feedback from mentors/advisors

## Support

For issues or questions:
- Check existing examples in the `examples/` directory
- Review error messages carefully
- Open an issue on GitHub with:
  - Command used
  - Error message
  - Sample input (if possible)
