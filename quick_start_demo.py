#!/usr/bin/env python3
"""
Quick Start Example - Research Proposal Tool
Demonstrates the main features of the tool
"""

from research_tool import (
    PaperProcessor,
    PaperSummarizer,
    ReferenceOrganizer,
    ProposalGenerator
)

def main():
    print("="*70)
    print("Research Proposal Tool - Quick Start Demo")
    print("="*70)
    
    # Sample paper text
    sample_paper = """
Machine Learning for Healthcare: A Review

Authors: Smith J., Johnson R.

2024

Keywords: machine learning, healthcare, medical diagnosis, AI

Abstract

Machine learning has transformed healthcare by enabling automated diagnosis,
personalized treatment, and predictive analytics. This review examines recent
advances in ML applications across various medical domains.

Methods

We conducted a systematic review of 200 papers published between 2020-2024.
Papers were analyzed for methodology, performance metrics, and clinical impact.

Results

ML models achieved 90% accuracy in medical image classification. Deep learning
showed particular promise for early disease detection. Key findings include
improved diagnostic accuracy and reduced processing time.

Conclusion

Machine learning represents a significant advancement in healthcare technology,
with potential to improve patient outcomes and reduce costs.
"""
    
    print("\n1. PROCESSING A PAPER")
    print("-" * 70)
    processor = PaperProcessor()
    paper_data = processor.process_paper(sample_paper)
    
    print(f"Title: {paper_data['metadata']['title']}")
    print(f"Keywords: {', '.join(paper_data['metadata']['keywords'])}")
    print(f"Abstract length: {len(paper_data['abstract'])} characters")
    print("✓ Paper processed successfully")
    
    print("\n2. GENERATING A SUMMARY")
    print("-" * 70)
    summarizer = PaperSummarizer()
    summary = summarizer.generate_paper_summary(paper_data)
    
    print(f"Title: {summary['title']}")
    print(f"Year: {summary['year']}")
    print(f"Abstract summary (first 100 chars): {summary['abstract_summary'][:100]}...")
    print(f"Key findings: {len(summary['key_findings'])} identified")
    print("✓ Summary generated successfully")
    
    print("\n3. MANAGING REFERENCES")
    print("-" * 70)
    organizer = ReferenceOrganizer()
    
    # Add reference from processed paper
    ref_id = organizer.add_reference_from_paper_data(paper_data)
    print(f"✓ Added reference with ID: {ref_id}")
    
    # Add another manual reference
    ref_id2 = organizer.add_reference(
        title="Deep Learning in Medicine",
        authors="Chen, M., Williams, E.",
        year="2023",
        source="Medical AI Journal"
    )
    print(f"✓ Added reference with ID: {ref_id2}")
    
    # Export in APA format
    apa_refs = organizer.export_references(format='apa')
    print("\nAPA Formatted References:")
    print(apa_refs)
    
    print("\n4. GENERATING A RESEARCH PROPOSAL")
    print("-" * 70)
    generator = ProposalGenerator()
    
    # Set basic information
    generator.set_title("AI-Enhanced Medical Diagnosis System")
    generator.set_author("PhD Candidate")
    
    # Generate literature review from the paper
    lit_review = generator.generate_literature_review_from_papers([summary])
    generator.set_section('literature_review', lit_review)
    
    # Set introduction
    generator.set_section('introduction', """
This proposal aims to develop an AI-enhanced medical diagnosis system that 
leverages machine learning to improve diagnostic accuracy and efficiency in 
clinical settings.
""")
    
    # Set research questions
    generator.set_section('research_questions', """
### Main Research Question
How can machine learning improve diagnostic accuracy in clinical practice?

### Specific Objectives
1. Develop ML models for multi-disease detection
2. Evaluate model performance in clinical settings
3. Assess impact on patient outcomes
4. Identify implementation challenges
""")
    
    # Generate methodology
    methodology = generator.create_methodology_template('mixed')
    generator.set_section('methodology', methodology)
    
    # Set references
    generator.set_section('references', apa_refs)
    
    # Generate complete proposal
    proposal = generator.generate_proposal()
    
    print("✓ Proposal generated successfully")
    print(f"Proposal length: {len(proposal)} characters")
    print(f"Proposal sections: 12 main sections included")
    
    # Save proposal to file
    output_file = 'demo_proposal.md'
    generator.save_proposal(output_file)
    print(f"✓ Proposal saved to: {output_file}")
    
    print("\n" + "="*70)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nNext steps:")
    print("1. Review the generated proposal: demo_proposal.md")
    print("2. Try processing your own papers with: python research_tool_cli.py process <file>")
    print("3. Generate your proposal with: python research_tool_cli.py generate <papers>")
    print("4. Read USAGE_GUIDE.md for detailed instructions")
    print("\n")

if __name__ == '__main__':
    main()
