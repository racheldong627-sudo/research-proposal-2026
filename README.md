# Research Proposal Tool 2026

A comprehensive Python tool for processing research papers and generating structured research proposals for PhD applications.

## Features

- **Paper Processing**: Extract key information from research papers including abstracts, methods, results, and findings
- **Paper Summarization**: Generate concise summaries of research papers with key findings
- **Reference Management**: Organize and format references in APA or IEEE style
- **Proposal Generation**: Create structured research proposal drafts with templates for:
  - Literature review
  - Research gaps identification
  - Proposed methodology
  - Expected outcomes
  - Timeline and milestones

## Installation

1. Clone the repository:
```bash
git clone https://github.com/racheldong627-sudo/research-proposal-2026.git
cd research-proposal-2026
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### 1. Process a Research Paper

Extract information from a research paper:

```bash
python research_tool_cli.py process examples/sample_paper1.txt -o paper1_data.json
```

### 2. Summarize a Paper

Generate a concise summary:

```bash
python research_tool_cli.py summarize examples/sample_paper1.txt -o summary.txt
```

### 3. Generate a Research Proposal

Create a complete research proposal from multiple papers:

```bash
python research_tool_cli.py generate examples/sample_paper1.txt examples/sample_paper2.txt \
    -t "Machine Learning for Climate-Aware Medical Diagnostics" \
    -a "Your Name" \
    -r mixed \
    -o my_proposal.md
```

### 4. Manage References

Add references:
```bash
python research_tool_cli.py references add \
    -f references.json \
    --title "Machine Learning in Healthcare" \
    --authors "Smith, J." \
    --year "2023" \
    --source "Journal of AI"
```

List references:
```bash
python research_tool_cli.py references list -f references.json --sort year
```

Export references:
```bash
python research_tool_cli.py references export -f references.json --format apa -o references.txt
```

## Module Overview

### PaperProcessor
Extracts structured information from research papers:
- Metadata (title, authors, year, keywords)
- Abstract
- Methods/Methodology
- Results/Findings
- Conclusion

### PaperSummarizer
Generates concise summaries:
- Abstract summarization
- Key findings extraction
- Methods overview
- Formatted summary output

### ReferenceOrganizer
Manages bibliographic references:
- Add, search, and list references
- Format in APA or IEEE style
- Import/export reference databases
- Sort by various fields

### ProposalGenerator
Creates structured research proposals:
- Literature review generation
- Research gap identification
- Methodology templates
- Complete proposal formatting

## Usage Examples

### Python API

```python
from research_tool import PaperProcessor, PaperSummarizer, ProposalGenerator

# Process a paper
processor = PaperProcessor()
with open('paper.txt', 'r') as f:
    paper_text = f.read()

paper_data = processor.process_paper(paper_text)
print(f"Title: {paper_data['metadata']['title']}")
print(f"Abstract: {paper_data['abstract']}")

# Generate summary
summarizer = PaperSummarizer()
summary = summarizer.generate_paper_summary(paper_data)
print(summarizer.format_summary_text(summary))

# Generate proposal
generator = ProposalGenerator()
generator.set_title("My Research Proposal")
generator.set_author("John Doe")
generator.set_section('literature_review', "...")
proposal = generator.generate_proposal()
```

## Project Structure

```
research-proposal-2026/
├── research_tool/
│   ├── __init__.py
│   ├── paper_processor.py
│   ├── paper_summarizer.py
│   ├── reference_organizer.py
│   └── proposal_generator.py
├── research_tool_cli.py
├── examples/
│   ├── sample_paper1.txt
│   └── sample_paper2.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Input Format

Papers should be in plain text format with clear section headings. The tool can recognize common section patterns:
- Abstract, Introduction, Methods/Methodology, Results/Findings, Discussion, Conclusion

## Output Format

- **Processed papers**: JSON format with extracted sections
- **Summaries**: Markdown or plain text
- **Proposals**: Markdown format with structured sections
- **References**: Formatted citation lists

## Customization

### Proposal Template

The proposal template includes these sections:
1. Executive Summary
2. Introduction and Background
3. Literature Review
4. Research Gap
5. Research Questions and Objectives
6. Proposed Methodology
7. Expected Outcomes and Significance
8. Timeline and Milestones
9. Budget and Resources
10. References
11. Appendices

Each section can be customized using the `set_section()` method.

### Research Types

Choose from three methodology templates:
- `qualitative`: Qualitative research approach
- `quantitative`: Quantitative research approach
- `mixed`: Mixed-methods approach (default)

## Tips for Best Results

1. **Paper Format**: Ensure papers have clear section headings
2. **Multiple Papers**: Include 5-10 papers for comprehensive literature review
3. **Manual Editing**: Review and edit generated proposals for accuracy and completeness
4. **Reference Management**: Maintain a reference database for easy citation management

## Troubleshooting

**Issue**: Section not extracted correctly
- **Solution**: Check that section headings match common patterns or add custom patterns

**Issue**: Summary too brief/verbose
- **Solution**: Adjust `max_sentences` or `max_points` parameters in the API

## Contributing

This is a PhD application tool. For suggestions or improvements, please open an issue.

## License

This project is open source and available for academic use.

## Contact

For questions or support, please open an issue in the repository.
