"""
Proposal Generator Module
Generates structured research proposal drafts.
"""

from typing import Dict, List, Optional
from datetime import datetime


class ProposalGenerator:
    """Generate structured research proposal drafts."""
    
    PROPOSAL_TEMPLATE = """
# Research Proposal: {title}

**Prepared by:** {author}
**Date:** {date}

---

## 1. Executive Summary

{executive_summary}

---

## 2. Introduction and Background

{introduction}

---

## 3. Literature Review

{literature_review}

---

## 4. Research Gap

{research_gap}

---

## 5. Research Questions and Objectives

{research_questions}

---

## 6. Proposed Methodology

{methodology}

---

## 7. Expected Outcomes and Significance

{expected_outcomes}

---

## 8. Timeline and Milestones

{timeline}

---

## 9. Budget and Resources

{budget}

---

## 10. References

{references}

---

## Appendices

{appendices}
"""
    
    def __init__(self):
        """Initialize the proposal generator."""
        self.proposal_data = {
            'title': '',
            'author': '',
            'executive_summary': '',
            'introduction': '',
            'literature_review': '',
            'research_gap': '',
            'research_questions': '',
            'methodology': '',
            'expected_outcomes': '',
            'timeline': '',
            'budget': '',
            'references': '',
            'appendices': ''
        }
    
    def set_title(self, title: str) -> None:
        """Set the proposal title."""
        self.proposal_data['title'] = title
    
    def set_author(self, author: str) -> None:
        """Set the proposal author."""
        self.proposal_data['author'] = author
    
    def generate_literature_review_from_papers(self, paper_summaries: List[Dict]) -> str:
        """
        Generate literature review section from paper summaries.
        
        Args:
            paper_summaries: List of paper summaries (from PaperSummarizer)
            
        Returns:
            Formatted literature review text
        """
        if not paper_summaries:
            return "No papers provided for literature review."
        
        review_parts = []
        review_parts.append("### Overview of Existing Research\n")
        review_parts.append("The following literature provides the foundation for this research proposal:\n")
        
        for i, paper in enumerate(paper_summaries, 1):
            review_parts.append(f"\n#### {i}. {paper.get('title', 'Unknown')}")
            
            if paper.get('year'):
                review_parts.append(f"*({paper['year']})*\n")
            else:
                review_parts.append("")
            
            if paper.get('abstract_summary'):
                review_parts.append(paper['abstract_summary'])
            
            if paper.get('key_findings'):
                review_parts.append("\n**Key Findings:**")
                for finding in paper['key_findings']:
                    review_parts.append(f"- {finding}")
        
        review_parts.append("\n### Synthesis")
        review_parts.append("The reviewed literature collectively demonstrates...")
        
        return '\n'.join(review_parts)
    
    def identify_research_gaps(self, paper_summaries: List[Dict]) -> str:
        """
        Suggest research gaps based on reviewed papers.
        
        Args:
            paper_summaries: List of paper summaries
            
        Returns:
            Research gap analysis text
        """
        gap_text = []
        gap_text.append("### Identified Gaps in Current Research\n")
        gap_text.append("Based on the literature review, the following gaps have been identified:\n")
        
        # Extract topics/keywords from papers
        all_keywords = []
        for paper in paper_summaries:
            all_keywords.extend(paper.get('keywords', []))
        
        gap_text.append("1. **Methodological Gaps**: [Describe limitations in existing methodologies]")
        gap_text.append("\n2. **Empirical Gaps**: [Identify areas lacking empirical evidence]")
        gap_text.append("\n3. **Theoretical Gaps**: [Highlight theoretical frameworks not yet explored]")
        gap_text.append("\n4. **Contextual Gaps**: [Note contexts or populations not yet studied]")
        
        if all_keywords:
            gap_text.append(f"\n*Note: Research areas covered include: {', '.join(list(set(all_keywords))[:10])}*")
        
        return '\n'.join(gap_text)
    
    def create_methodology_template(self, research_type: str = "mixed") -> str:
        """
        Create a methodology section template.
        
        Args:
            research_type: Type of research ('qualitative', 'quantitative', 'mixed')
            
        Returns:
            Methodology template text
        """
        method_text = []
        method_text.append("### Research Design\n")
        
        if research_type == "qualitative":
            method_text.append("This research will employ a qualitative approach using...")
        elif research_type == "quantitative":
            method_text.append("This research will employ a quantitative approach using...")
        else:
            method_text.append("This research will employ a mixed-methods approach combining...")
        
        method_text.append("\n### Data Collection")
        method_text.append("- **Sources**: [Specify data sources]")
        method_text.append("- **Instruments**: [Describe data collection instruments]")
        method_text.append("- **Sampling**: [Explain sampling strategy]")
        method_text.append("- **Timeline**: [Indicate data collection timeline]")
        
        method_text.append("\n### Data Analysis")
        method_text.append("- **Analytical Framework**: [Describe analytical approach]")
        method_text.append("- **Tools**: [Specify analytical tools and software]")
        method_text.append("- **Validation**: [Explain validation methods]")
        
        method_text.append("\n### Ethical Considerations")
        method_text.append("- Informed consent will be obtained from all participants")
        method_text.append("- Data confidentiality and privacy will be maintained")
        method_text.append("- Ethics approval will be sought from relevant committees")
        
        return '\n'.join(method_text)
    
    def set_section(self, section_name: str, content: str) -> None:
        """
        Set content for a specific section.
        
        Args:
            section_name: Name of the section
            content: Content for the section
        """
        if section_name in self.proposal_data:
            self.proposal_data[section_name] = content
    
    def generate_proposal(self) -> str:
        """
        Generate the complete proposal document.
        
        Returns:
            Formatted proposal text
        """
        # Fill in missing data with placeholders
        data = self.proposal_data.copy()
        data['date'] = datetime.now().strftime('%B %d, %Y')
        
        for key, value in data.items():
            if not value:
                data[key] = f"[TO BE COMPLETED: {key.replace('_', ' ').title()}]"
        
        return self.PROPOSAL_TEMPLATE.format(**data)
    
    def save_proposal(self, filename: str) -> None:
        """
        Save the proposal to a file.
        
        Args:
            filename: Output filename
        """
        proposal_text = self.generate_proposal()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(proposal_text)
    
    def generate_from_papers(self, paper_summaries: List[Dict], 
                            title: str, author: str,
                            research_type: str = "mixed",
                            references_text: str = "") -> str:
        """
        Generate a complete proposal from paper summaries.
        
        Args:
            paper_summaries: List of paper summaries
            title: Proposal title
            author: Author name
            research_type: Type of research methodology
            references_text: Formatted references
            
        Returns:
            Complete proposal text
        """
        self.set_title(title)
        self.set_author(author)
        
        # Generate literature review
        lit_review = self.generate_literature_review_from_papers(paper_summaries)
        self.set_section('literature_review', lit_review)
        
        # Generate research gap
        research_gap = self.identify_research_gaps(paper_summaries)
        self.set_section('research_gap', research_gap)
        
        # Generate methodology
        methodology = self.create_methodology_template(research_type)
        self.set_section('methodology', methodology)
        
        # Set references
        if references_text:
            self.set_section('references', references_text)
        
        return self.generate_proposal()
