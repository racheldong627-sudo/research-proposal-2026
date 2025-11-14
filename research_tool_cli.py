#!/usr/bin/env python3
"""
Command-Line Interface for Research Proposal Tool
"""

import argparse
import sys
from pathlib import Path

from research_tool import (
    PaperProcessor,
    PaperSummarizer,
    ReferenceOrganizer,
    ProposalGenerator
)


def process_paper_command(args):
    """Process a research paper and extract information."""
    processor = PaperProcessor()
    
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            paper_text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return 1
    
    paper_data = processor.process_paper(paper_text)
    
    # Display extracted information
    print("\n" + "="*60)
    print("PAPER PROCESSING RESULTS")
    print("="*60)
    
    print("\n--- METADATA ---")
    print(f"Title: {paper_data['metadata']['title']}")
    print(f"Year: {paper_data['metadata']['year']}")
    print(f"Keywords: {', '.join(paper_data['metadata']['keywords'])}")
    
    if paper_data['abstract']:
        print("\n--- ABSTRACT ---")
        print(paper_data['abstract'][:500] + "..." if len(paper_data['abstract']) > 500 else paper_data['abstract'])
    
    if paper_data['methods']:
        print("\n--- METHODS ---")
        print(paper_data['methods'][:500] + "..." if len(paper_data['methods']) > 500 else paper_data['methods'])
    
    if paper_data['results']:
        print("\n--- RESULTS ---")
        print(paper_data['results'][:500] + "..." if len(paper_data['results']) > 500 else paper_data['results'])
    
    # Save to output if specified
    if args.output:
        import json
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(paper_data, f, indent=2, ensure_ascii=False)
        print(f"\n✓ Results saved to: {args.output}")
    
    return 0


def summarize_paper_command(args):
    """Summarize a research paper."""
    processor = PaperProcessor()
    summarizer = PaperSummarizer()
    
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            paper_text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return 1
    
    paper_data = processor.process_paper(paper_text)
    summary = summarizer.generate_paper_summary(paper_data)
    summary_text = summarizer.format_summary_text(summary)
    
    print("\n" + "="*60)
    print("PAPER SUMMARY")
    print("="*60)
    print(summary_text)
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(summary_text)
        print(f"\n✓ Summary saved to: {args.output}")
    
    return 0


def generate_proposal_command(args):
    """Generate a research proposal from papers."""
    processor = PaperProcessor()
    summarizer = PaperSummarizer()
    generator = ProposalGenerator()
    
    # Process all input papers
    paper_summaries = []
    for paper_file in args.papers:
        try:
            with open(paper_file, 'r', encoding='utf-8') as f:
                paper_text = f.read()
            paper_data = processor.process_paper(paper_text)
            summary = summarizer.generate_paper_summary(paper_data)
            paper_summaries.append(summary)
            print(f"✓ Processed: {paper_file}")
        except Exception as e:
            print(f"✗ Error processing {paper_file}: {e}")
    
    if not paper_summaries:
        print("Error: No papers were successfully processed.")
        return 1
    
    # Generate proposal
    proposal = generator.generate_from_papers(
        paper_summaries,
        title=args.title,
        author=args.author or "Research Team",
        research_type=args.research_type
    )
    
    # Save proposal
    output_file = args.output or "research_proposal.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(proposal)
    
    print(f"\n✓ Research proposal generated: {output_file}")
    return 0


def manage_references_command(args):
    """Manage research references."""
    organizer = ReferenceOrganizer()
    
    # Load existing references if file exists
    if args.references_file and Path(args.references_file).exists():
        organizer.load_from_file(args.references_file)
        print(f"✓ Loaded references from: {args.references_file}")
    
    if args.action == 'add':
        ref_id = organizer.add_reference(
            title=args.title,
            authors=args.authors or "",
            year=args.year or "",
            source=args.source or "",
            doi=args.doi or ""
        )
        print(f"✓ Added reference with ID: {ref_id}")
        
        if args.references_file:
            organizer.save_to_file(args.references_file)
            print(f"✓ Saved to: {args.references_file}")
    
    elif args.action == 'list':
        references = organizer.list_references(sort_by=args.sort or 'id')
        print("\n" + "="*60)
        print("REFERENCES")
        print("="*60)
        for ref in references:
            print(f"\n[{ref['id']}] {ref['title']}")
            if ref['authors']:
                print(f"    Authors: {ref['authors']}")
            if ref['year']:
                print(f"    Year: {ref['year']}")
    
    elif args.action == 'export':
        export_text = organizer.export_references(format=args.format or 'apa')
        output_file = args.output or f"references_{args.format or 'apa'}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(export_text)
        print(f"✓ References exported to: {output_file}")
    
    return 0


def main():
    """Main entry point for CLI."""
    parser = argparse.ArgumentParser(
        description="Research Proposal Tool - Process papers and generate proposals",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Process paper command
    process_parser = subparsers.add_parser('process', help='Process a research paper')
    process_parser.add_argument('input', help='Input paper file (text format)')
    process_parser.add_argument('-o', '--output', help='Output JSON file')
    
    # Summarize paper command
    summarize_parser = subparsers.add_parser('summarize', help='Summarize a research paper')
    summarize_parser.add_argument('input', help='Input paper file (text format)')
    summarize_parser.add_argument('-o', '--output', help='Output summary file')
    
    # Generate proposal command
    proposal_parser = subparsers.add_parser('generate', help='Generate a research proposal')
    proposal_parser.add_argument('papers', nargs='+', help='Input paper files')
    proposal_parser.add_argument('-t', '--title', required=True, help='Proposal title')
    proposal_parser.add_argument('-a', '--author', help='Author name')
    proposal_parser.add_argument('-r', '--research-type', 
                                choices=['qualitative', 'quantitative', 'mixed'],
                                default='mixed', help='Research type')
    proposal_parser.add_argument('-o', '--output', help='Output proposal file')
    
    # Manage references command
    ref_parser = subparsers.add_parser('references', help='Manage references')
    ref_parser.add_argument('action', choices=['add', 'list', 'export'], 
                           help='Reference action')
    ref_parser.add_argument('-f', '--references-file', help='References database file')
    ref_parser.add_argument('--title', help='Paper title (for add)')
    ref_parser.add_argument('--authors', help='Paper authors (for add)')
    ref_parser.add_argument('--year', help='Publication year (for add)')
    ref_parser.add_argument('--source', help='Source/journal (for add)')
    ref_parser.add_argument('--doi', help='DOI (for add)')
    ref_parser.add_argument('--sort', choices=['id', 'year', 'title', 'authors'],
                           help='Sort by field (for list)')
    ref_parser.add_argument('--format', choices=['apa', 'ieee'],
                           help='Citation format (for export)')
    ref_parser.add_argument('-o', '--output', help='Output file (for export)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    # Execute command
    if args.command == 'process':
        return process_paper_command(args)
    elif args.command == 'summarize':
        return summarize_paper_command(args)
    elif args.command == 'generate':
        return generate_proposal_command(args)
    elif args.command == 'references':
        return manage_references_command(args)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
